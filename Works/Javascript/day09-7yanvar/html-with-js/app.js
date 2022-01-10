let ul = document.createElement('ul')
document.body.appendChild(ul)
for (let i = 0; i < 5; i++) {
    //let li = document.createElement('li')
   // ul.appendChild(li)
   //  li.setAttribute('onclick', 'removeSelf(this)')
    //li.innerHTML = `Lorem ipsum dolor sit amet 0${i}`
    // document.body.appendChild(ul)

    ul.innerHTML += ` <li onclick="removeSelf(this)">Lorem ipsum dolor sit amet 0${i}</li>`
}

function removeSelf(elem) {
    let ul = elem.parentElement

    ul.removeChild(elem)

}