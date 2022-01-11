categories = ['Medeniyyet', 'Siyaset', 'Idman', 'Sou Biznes']
xeberler = [{
        basliq: 'Azərbaycan neftinin bu günə olan qiyməti AÇIQLANDI',
        sekil: 'images/neftdgfhn.jpg',
        category: categories[0],
        detal: `lorem ipsum dolor sit amet`
    },
    {
        basliq: 'Tikinti şirkəti “Azərsu”yu məhkəməyə verib',
        sekil: 'images/2.jpg',
        category: categories[1]
    },
    {
        basliq: 'Mənzili köhnə, yoxsa yeni binadan almaq sərfəlidir?',
        sekil: 'images/3.jpg',
        category: categories[1]
    },
    {
        basliq: 'Dünyanın bir nömrəli tennisçisinin apellyasiya şikayəti təmin edildi',
        sekil: 'images/4.jpg',
        category: categories[2]
    }
]
let nav = document.querySelector('nav ul')
let news = document.querySelector('.news-container')

for (let category of categories) {
    nav.innerHTML += `<li onclick="showNews(this)">${category}</li>`
}

for (let xeber of xeberler) {
    news.innerHTML += `
    
    <div class="news-item">
            <img src="${xeber.sekil}" alt="">
            <h1>${xeber.basliq}</h1>
        </div>
    `
}

function showNews(elem) {
    let catName = elem.innerHTML;
    news.innerHTML = ""
    for (let xeber of xeberler) {
        if (xeber.category == catName) {
            news.innerHTML += `
        
        <div class="news-item">
                <img src="${xeber.sekil}" alt="">
                <h1 onclick="this.parentNode.parentNode.detail()">${xeber.basliq}</h1>
                
      
}
                
            </div>
        `
        }
    }
}

function showAll() {
    for (let xeber of xeberler) {
        news.innerHTML += `
        
        <div class="news-item">
                <img src="${xeber.sekil}" alt="">
                <h1>${xeber.basliq}</h1>
            </div>
        `
    }
}