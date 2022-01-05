var opeartors={
    "+": function(a,b){return a+b},
    "-": function(a,b){return a-b},
    "*": function(a,b){return a*b},
    "/": function(a,b){return a/b}
}
calculate =function(val1, val2, sign){
    if (sign in opeartors){
        return opeartors[sign](val1, val2);
    }
}
document.write(calculate(8,4647,"*"))