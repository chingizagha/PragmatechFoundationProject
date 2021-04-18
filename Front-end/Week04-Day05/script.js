let container = document.createElement('div');
container.classList.add('container');
container.setAttribute('style', "width:100%; max-width:1200px; margin:0 auto; background-color:#F8F9FA;");

document.querySelector('body').appendChild(container);

let block = document.createElement('div');
block.classList.add('block');
block.setAttribute('style', "width:500px; height:500px; background-color:orange!important; margin:0 auto; display:flex; flex-wrap:wrap; gap:25px; cursor:pointer;");

document.querySelector('.container').appendChild(block); 


for (let i= 0; i< 49; i++) {
    let miniBlock = document.createElement('div');
    miniBlock.classList.add('miniBlock');
    miniBlock.setAttribute('style', "width:50px; height:50px; background-color:red;");
    document.querySelector('.block').appendChild(miniBlock); 
}

    let x = Math.floor(Math.random() * 256);
    let y = Math.floor(Math.random() * 256);
    let z = Math.floor(Math.random() * 256);
    let bgColor = "rgb(" + x +  "," + y + "," + z + ")";



 


    block.addEventListener('click', (event) => {
        console.log(event.target);
        event.target.style.backgroundColor =  bgColor
}
)






