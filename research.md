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

... 3) Functional scope, global scope, block scope, local scope anlayışları
Functional scope- yazılan funksiyanın içərisində keçərlidir.
Block scope- yazılan bəzəkli { } mötərizələr içərisində keçərlidir.
let və const block scope tabanlı olub ona ən yaxın bəzəkli mötərizələr arasında əlçatandır
Local Scope- variable bir funksiya içərisindədirsə bunun yerləşdiyi əraziyə Local Scope adı verilir. Tanımlanan variable də local variabledir.
Global scope- Proqram içərisində funksiyaların xaricində tanımlanmış və hər yerdən əlçatan olan scope tipidir. Global scope`da tanınmlanmış bir variable-ə qovluq içərisində hər yerdən erişilebilir.Global variable deyilir bunlara. Amma global variable istifadəsi çox da tövsiyə olunmur. Çünki local variables iş bitdikdə silinsə də global variables varlığını davam etdirir və bu da gələcəkdə memory problemlərinə yol aça bilir.

5. Pyhton dilində funksiyanın təyin olunması
   Pyhton dilində funksiyanı təyin etmək üçün def əmrindən istifadə olunur. Digər bəzi dillərdən fərqli olaraq parametrlərinin hansı tipdə olduğu bildirilmir.Məlumat tiplərilə işi asanlaşdırsa da bu məlumat dipləri uyumlu olmalıdır ki xətaya yol verilməsin
   def hello():
   print("Merhaba")
   Funksiyanı çağırmaq üçün funksiyanın adı ilə birlikdə mötərizələr də istifadə olunmalıdır
   def hello():
   print("Merhaba")

hello() # Merhaba

Pyhtonda void funksiyasinin işlənməsinı baxaq

def ortalama_hesapla(sayi1,sayi2,sayi3):
ortalama = (sayi1+sayi2+sayi3)/3.0 # ortalama alinma islemi ve "ortalama" adli degiskene ortalamanin atanmasi
print ortalama # ortalamanin yazdirilmasi
Funksiya içərisində print{} ilə bilgi yazdırmaq yerinə bilgini geri də döndürə bilərik
def hello(name):
return "Merhaba "+ name

print(hello("Arda")) # Merhaba Arda

Başqa nümunəyə baxaq
def toplama(a,b):
return a+b

sonuc = toplama(10,20)
print(sonuc) # 30

toplama funksiyasi xaricdən a və b parametrlərini gözləyir və göndərdiyimiz dəyərləri funksiya içərisində toplayıb nəticəni 30 olaraq geri döndürür.

Pyhtonda void funksiyasi

1 def add(num1, num2):

2 print("Sum is", num1 + num2)

3

4 return_val = add(300, 500)

5 print(return_val)
output:

1 Sum is 800

2 None

C# funksiya teyini:
<görünürlük> <dönüş tipi> <ad>(<parametreler>)
{
<fonksiyon kodları>
}
Void funksiya
public void Yap()
{
MessageBox.Show("Selam Arkadaşım...");
}

int yapida deger donduren funksiya
public int topla(int sayi1, int sayi2)
{
int sonuc = sayi1 + sayi2;
return sonuc;
}
