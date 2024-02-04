from modelos import db, Lista, Usuario
from flask import Flask

# Create the Flask app
app = Flask('app')

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()

# Now, let's create an example Lista and Usuario
with app.app_context():
    # Create a Lista instance
    nueva_lista = Lista(titulo='Ejemplo de Lista', parrafo='Contenido de la lista')
    
    # Add the Lista instance to the database session
    db.session.add(nueva_lista)
    
    # Commit the changes to the database
    db.session.commit()

    # Create a Usuario instance
    nuevo_usuario = Usuario(username='ejemplo_usuario', password='contrasena', email='usuario@example.com')
    
    # Add the Usuario instance to the database session
    db.session.add(nuevo_usuario)
    
    # Commit the changes to the database
    db.session.commit()
