let move = 0;
let sliderLine = document.querySelector('.slider-line');

document.querySelector('.next').addEventListener('click', () => {
    sliderLine.style.transition = 'all 0.8s ease 0s';
    move += 291;
    if (move > 873) {
        sliderLine.style.transition = 'none';
        move = 0
    }
    sliderLine.style.left = -move + 'px';
})

document.querySelector('.prev').addEventListener('click', () => {
    sliderLine.style.transition = 'all 0.8s ease 0s';
    move -= 291;
    if (move < 0) {
        sliderLine.style.transition = 'none';
        move = 873
    }
    sliderLine.style.left = -move + 'px';
})