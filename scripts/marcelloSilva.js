/*
Author: Marcello Victor
Language: JS
Github: https://github.com/MarcelloVSilva
*/

count = 1;
divisiblePer3 = false
divisiblePer5 = false
animals = ""

while(count <= 100){
    if(divisiblePer3Fn(count)) 
        divisiblePer3 = true
    if(divisiblePer5Fn(count)) 
        divisiblePer5 = true

    if(divisiblePer3 && divisiblePer5){
        animals = "spiders"
    } else if(divisiblePer3 && !divisiblePer5){
        animals = "cats"
    } else if(!divisiblePer3 && divisiblePer5){
        animals = "bats"
    }

    animals ? console.log({animals}) : console.log({count}) 
    
    resetVars();
    count++
}

function resetVars(){
    divisiblePer3 = false
    divisiblePer5 = false
    animals = ""
}
function divisiblePer3Fn(value){
    return value % 3 === 0
}

function divisiblePer5Fn(value){
    return  value % 5 === 0
}