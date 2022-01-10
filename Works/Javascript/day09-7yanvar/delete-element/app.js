/*function myFunction(elem){
  elem.style.display="none";
}*/
/*
function removeSelf(elem){
  let ul =document.querySelector('ul')
  ul.removeChild(elem)
}*/

function removeSelf(elem){
  let ul=elem.parentElement
ul.removeChild(elem)}