class Person{
    constructor(ad){
        this.ad=ad;
    }
    salam(){
        document.write("Hello "+this.ad);
    }
}
var person= new Person("Aytac");
person.salam();
