const rotateBtn = document.querySelector('.rotate-btn');
const slides = document.querySelectorAll('.bg-slider');
const mainHeader = document.querySelector("header");
const totalSlides = slides.length;
let index = 0;

rotateBtn.addEventListener('click', () => {
    rotateBtn.classList.add('active');
    setTimeout(()=>{
        rotateBtn.classList.remove('active');
    }, 2100)

    slides.forEach(slide =>{
        if (slide.classList.contains('active')){
            slide.classList.add('after-active');
        }
        else{
            slide.classList.remove('after-active');
        }
       
    })

    slides [index].classList.remove('active');

    index++;

    if (index == totalSlides) {
        index = 0;
    }

    slides [index].classList.add('active');
});



window.addEventListener("scroll", function(){
    mainHeader.classList.toggle("sticky", window.scrollY > 0);
});

let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('open');

};

window.onscroll = () =>{
    menu.classList.remove('bx-x');
    navbar.classList.remove('open')
};