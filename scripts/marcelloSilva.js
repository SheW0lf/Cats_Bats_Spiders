/*
Author: Marcello Victor
Language: JS
Github: https://github.com/MarcelloVSilva
*/

let number = 1;
let divisiblePer3 = false
let divisiblePer5 = false
let animal = ""

while(number <= 100){
    if(divisiblePer3Fn(number)) 
        divisiblePer3 = true
    if(divisiblePer5Fn(number)) 
        divisiblePer5 = true

    if(divisiblePer3 && divisiblePer5){
        animal = "spiders"
    } else if(divisiblePer3 && !divisiblePer5){
        animal = "cats"
    } else if(!divisiblePer3 && divisiblePer5){
        animal = "bats"
    }

    animal ? console.log({animal}) : console.log({number}) 

    resetVars();
    number++
}

function resetVars(){
    divisiblePer3 = false
    divisiblePer5 = false
    animal = ""
}
function divisiblePer3Fn(value){
    return value % 3 === 0
}

function divisiblePer5Fn(value){
    return  value % 5 === 0
}