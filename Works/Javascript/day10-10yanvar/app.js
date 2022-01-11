function getUserData(event) {
    event.preventDefault()
    let table = document.querySelector('table')
    let ad = document.querySelector('input[name=ad]').value
    let soyad = document.querySelector('input[name=soyad]').value
    let email = document.querySelector('input[name=email]').value
    let date = document.querySelector('input[name=date]').value
    table.innerHTML += ` 
    <tr >
                <td>${ad}</td>
                <td>${soyad}</td>
                <td>${email}</td>
                <td>${date}</td>
                <td onclick="this.parentNode.parentNode.style.display = 'none';"><a href=#' ">Sil</a></td></tr>`// trnin icindeki th`in icindeki td


}