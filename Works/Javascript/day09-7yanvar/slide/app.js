let sliderWidth = 1000;

let slider = document.querySelector('.slider')
let slides = document.querySelector('.slider-items')
let allSlides = document.querySelectorAll('.slider-item')
let btns = document.querySelector('.btns')

slider.style.width = `${sliderWidth}px`
slides.style.width = `${allSlides.length*(sliderWidth / 1)}px`

for (let slide of allSlides) {
    slide.style.width = `${sliderWidth / 1 - 20}px`
}

function move(leftPos) {
    slides.style.left = `${leftPos}px`
}



for (let i = 0; i < allSlides.length / 1; i++) {
    btns.innerHTML += `<div class="btn" onclick="move(${-i*sliderWidth})"></div>`
}