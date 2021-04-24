let move = 0;
let sliderLine = document.querySelector(".slider-line");


document.querySelector('.arrow-r').addEventListener('click', () => {
    sliderLine.style.transition = 'all 1.1s ease 0s';
    move += 50;
    if (move > 50) {
        //sliderLine.style.transition = 'none';
        move = 0
    }
    sliderLine.style.left = -move + '%';
})

document.querySelector('.arrow-l').addEventListener('click', ()=> {
    sliderLine.style.transition = 'all 1.1s ease 0s';
    move -= 50;
    if (move < 0) {
        move = 50
    }
    sliderLine.style.left = -move + '%';
})

