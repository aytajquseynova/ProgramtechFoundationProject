// class ile erisim 
document.getElementById("paragraf").onclick= function() { 
    document.getElementsByClassName("text")[0].innerHTML="Bura ilk paragrafdir";
    document.getElementsByClassName("text2")[0].innerHTML="Bura ise 2ci paragrafdir";
}