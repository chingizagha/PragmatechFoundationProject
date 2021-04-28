/* Animation */
const section = () => {
    if (window.scrollY >= 0) {
        let animes = document.querySelector('.about-section-title');
        animes.classList.add('_active')

    }
}

section();



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

console.log("hello world");
