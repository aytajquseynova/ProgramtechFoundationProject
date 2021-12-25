let a=0
function repeat(){
    a++
    console.log(a)
    if(a<3000){
        repeat()
    }
}

repeat()