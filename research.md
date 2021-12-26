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

2)funksiyanin teyin olunma uslublari

1.parametrsiz funksiyalar.
Hər hansı parametrə ehtiyac duymadan, funksiyadakı kodların yerinə yetirilməsi ilə çalışan funksiyalardır

<script>
   function topla(){
   var istifadecisayi1=prompt("zehmet olmasa ilk sayi daxil edin:" ,"");
   var istifadecisayi2=prompt("zehmet olmasa ikinci sayi elave edin"; "");
   alert(parseInt(istifadecisayi1)+parseInt(istifadecisayi2));}
   topla();

   </script>

function yazandan sonra funksiyaya ad verdim ve scope hissesine islemesini istediyim kodlari yazib sonda topla() funksiyasini calisdirdim. Funksiyani daxili bir js qovlugunda islede bilerem.

2.Parametrli funksiyalar

<script>
   function topla(ilk reqem, ikinci reqem){
alert(ilk reqem+ ikinci reqem);
topla(4,5);
   }
</script>

Tez-tez istifadə olunan özəllikdir. JQuery kimi kitabxanada ya da ki node.js ilə proqlama zamanı daha çox istifadəsinə rast gələ bilərsiz 3. Return deyimi
Bəzən kodlarımızda çalışmasını istəmədiyimiz hissələr ola bilir.continue-da çalışmasını istəmədiyimiz kodlar çalışmır. return-də isə kodların çalışmasını istəmədiyimiz qisminə gələndə funksiyadan çıxılır və altındakı kodları çalışdırmır. Aralarındakı fərq budur.

<script>
    function farkHesaplama(ilk,son) {
        if (ilk < son) {
            alert("İlk değer ikinci değerden küçüktü.");
            return;
        } else {
            alert(ilk - son);
        }
    }
    farkHesaplama(15, 20);
</script>

4. Hazır funksiyalar
   write(), alert(), prompt() kimi hazır funksiyalarla tanış olduq, hansı ki onlar bizim kod yazmağımızı asanlaşdırmağa kömək edir.
   string( ) - string veriyi string növünə, number( ) isə number növünə çevirir
