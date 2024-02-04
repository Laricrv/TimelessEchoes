from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Lista, Usuario

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/home')
def index():
    listas = Lista.query.all()
    return render_template('index.html', listas=listas)

@app.route('/')
def landing():
    return render_template('landing-page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.query.filter_by(username=username, password=password).first()

        if usuario:
            return redirect(url_for('index'))
        else:
            return "Credenciales inválidas. Inténtalo de nuevo."

    return render_template('login.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        nuevo_usuario = Usuario(username=username, password=password, email=email)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('sign-up.html')

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        parrafo = request.form.get('parrafo')


        nueva_lista = Lista(titulo=titulo, parrafo=parrafo)

        db.session.add(nueva_lista)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('crear.html')

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    lista = Lista.query.get(id)
    if request.method == 'POST':
        lista.titulo = request.form.get('titulo')
        lista.parrafo = request.form.get('parrafo')

        db.session.commit()

        return redirect(url_for('index'))
    return render_template('editar.html', lista=lista)

@app.route('/eliminar/<id>')
def eliminar(id):
    lista = Lista.query.get_or_404(id)

    db.session.delete(lista)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5005)
