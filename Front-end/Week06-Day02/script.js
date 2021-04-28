 /*window.addEventListener('scroll', () => {
    //document.querySelector('nav').clientHeight - blokun icinde elementin hundurluyu
    if (window.scrollY > window.innerHeight / 4 - document.querySelector('nav').clientHeight) {
        document.querySelector('nav').style.opacity = 1;
    } else {
        document.querySelector('nav').style.opacity = 0;
    }
    // getBoundingClientRect().top - gorunen hisseden elementin yuxari hissesine geder olan mesafe
    if ((window.innerHeight + window.scrollY) > document.querySelector('.first__main').getBoundingClientRect().top) {
        document.querySelector('.first__main').classList.add('_active')
    } else {
        document.querySelector('.first__main').classList.remove('_active')
    }
    if ((window.innerHeight + window.scrollY) > document.querySelector('.second__main').offsetTop + document.querySelector('.second__main').clientHeight / 3) {
        for (let i = 0; i < document.querySelectorAll('.second__main p').length; i++) {
            document.querySelectorAll('.second__main p')[i].classList.add('_active')
        }
    } else {
        for (let i = 0; i < document.querySelectorAll('.second__main p').length; i++) {
            document.querySelectorAll('.second__main p')[i].classList.remove('_active')
        }
    }
})*/
const header = () => {
    if (window.scrollY == 0) {
        document.querySelectorAll('.header').forEach(e => {
            e.classList.add('_active');
        })
    }
}
header(); 