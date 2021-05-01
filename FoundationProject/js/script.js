/* Animation */
const section = () => {
    if (window.scrollY >= 0) {
        let animes = document.querySelector('.about-section-title');
        animes.classList.add('_active')

    }
}

section();

window.addEventListener('scroll', function() {
    let header = document.querySelector(".row-nav");
    header.style.transition = "all 0.3s ease";
    header.classList.toggle('navbar-fixed', window.scrollY >= 132);
})


/* Current Page */

// let currentLocation = window.location.href;
// const menuItem = document.querySelectorAll('.nav-ul a');
// const menuLength = menuItem.length
// console.log(currentLocation);

// for(let i = 0; i< menuLength; i++) {
//     if(menuItem[i].href === currentLocation) {
//         menuItem[i].className = 'selected';
//     }
//     else {
//         menuItem[i].className = 'non-selected';
//     }
// } 


