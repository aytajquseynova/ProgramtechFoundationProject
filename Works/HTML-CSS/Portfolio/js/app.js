categories=['ALL', 'BRANDING','ILLUSTRATION','WORDPRESS','SITE TEMPLATE']
let menu=document.querySelector('menu span')
for (let category of categories){
menu.innerHTML+=`<span>${category}</span>`
}