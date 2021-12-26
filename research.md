1. Javascriptdə keçmədiyimiz məlumat növləri

1) Bigİnt- istəyə bağlı uzunkuqdakı tam rəqəmləri təmsil edən məlumat növüdür. Bir tam sayının sonuna n əlavə edərək Bigİnt dəyəri yaratmaq mümkündür nadirən ehtiyac duyulur(kriptoqrafik və ya mikrosaniyə həssasiyyətli zaman damğaları üçün)
   const bigInt = 1234567890123456789012345678901234567890n;
   sondakı n bu dəyərin Bigİnt olduğunu göstərir

2)Array - birdən çox dəyər olur içərisində və [ ] istifadə olunur, dəyərlər (,) ilə ayrılır
var sehir=[“İstanbul”,” Ankara”, ”İzmir”]; // Yazı dizisi

var sayi=[ 11111, 222222, 333333]; // Sayı dizisi

3)Javascript obyektləri əyri mötərizələrlə yazılır. Obyekt xassələri vergüllə ayrılan ad:dəyər cütü kimi yazılır
const person = {
firstName : "Aytac",
lastName : "Hüseynova",
age : 20,
eyeColor : "black"
}; 4) type of operatoru 2 cür yazılır
1.operator olaraq: typeof x.
2)funskional tipdə: typeof(x)
