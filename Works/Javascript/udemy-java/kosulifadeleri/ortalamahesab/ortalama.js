var giris=41;
var final=85;
 var ortalama=(giris*0.4)+(final*0.6);
 document.write(ortalama+"<br>")
 if (ortalama>=50&& ortalama<=70){
     document.write('Adicisiniz')
 }else if(ortalama>=71&& ortalama<=90)
{
    document.write('zerbesiniz')
}else if(ortalama>=91 && ortalama<=100){
    document.write('elacisiniz')
}else{
    document.write('kesilmisiniz')
}