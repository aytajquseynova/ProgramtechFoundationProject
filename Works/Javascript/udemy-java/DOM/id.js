// id erisimi ucun document.getElementById istifade olunur
document.getElementById("change").onclick= function(){
    var ust= document.getElementById("content").innerHTML;
    var alt=document.getElementById("content2").innerHTML;
    document.getElementById("content").innerHTML=alt;
    document.getElementById("content2").innerHTML=ust;
}