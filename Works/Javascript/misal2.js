let a=0;
function repeat(){
    a++;
    if(a<500){
        if((a&9) !==0){
            console.log(a)}
           repeat() 
    }

}
repeat()