//sinif- nesne yapisi
// sinifimiz- telebeler
// nesneler(obyektler) yas adi
//consturctor sinife gondereceyimiz parametrleri tutur
class Telebeler{
    constructor(adi, yasi, vezifesi)
    {
        this.adi=adi;
        this.yasi=yasi;
        this.vezifesi=vezifesi;
    }
        ad ()
        {
            return this.adi;
        }
        age()
        {
            return this.yasi;
        }
        job()
        {
            return this.vezifesi;
        }


    }

 
  var obj=new Telebeler("Aytac",20,'developer');
  document.write(obj.ad()+" adli telebenin yasi ve vezifesi:"+obj.age()+" ,"+obj.job()+'<br>')
  
  var obj2=new Telebeler("Gulsen",24,'back-end-developer');
  document.write(obj2.ad()+" adli telebenin yasi ve vezifesi:"+obj2.age()+" ,"+obj2.job())


