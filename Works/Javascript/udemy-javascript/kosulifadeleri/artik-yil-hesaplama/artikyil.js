/*
400un kati olan yillar artik yillardir
bunun disinda 4un kati olan yillar icerisinde yalniz
100un kati olmayan yillar artik yillardir

 */
var year=prompt('ili daxil edin')
if((year%400===0) || (year%4===0)&& (year%100!==0)){
    document.write(year+' daxil edilen il artiq ildir')
}else{
    document.write(year+'daxil edilen il artiq il deyil' )
}