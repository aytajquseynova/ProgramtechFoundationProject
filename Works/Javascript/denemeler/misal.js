let a=0
function repeat(){
    a++;
    if( a<200){
                if((a&13) ===0){
                    console.log(a)
                }
                repeat()
    }
}
repeat()