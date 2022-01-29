// static metodu istifade etmeden 2 ededin vurulmasina baxaq
class bolmeHesabi{
    static bolme(eded1, eded2){
        return eded1/eded2;
    }
}
var alinannetice=bolmeHesabi.bolme(121,11);
document.write("Bolmeden alinan netice: "+alinannetice+"<br>")
//static metodu olmadan hesablama emeliyyatina baxaq
class Vurma{
    vur(eded1, eded2){
        return eded1*eded2
}
}
var hesabla= new Vurma();
var netice=hesabla.vur(7,464);
document.write(netice)