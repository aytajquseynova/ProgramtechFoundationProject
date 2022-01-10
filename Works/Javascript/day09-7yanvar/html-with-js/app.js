let ul=document.createElement('ul')
document.body.appendChild(ul)
for(i=0; i<6;i++){
    ul.innerHTML+=`<li onclick="removeSelf(this)">Lorem ipsum dolor sit amet 0${i}</li>`

}
function removeSelf(elem){
    let ul=elem.parentElement
    ul.removeChild(elem)

}