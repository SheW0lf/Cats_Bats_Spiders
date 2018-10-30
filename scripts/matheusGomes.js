/**
 * Author: Matheus Gomes
 * Language: JS
 * Github: https://github.com/matheus-gomes
 */

 for (let i = 1 ; i <= 100 ; i++) {
     if(divisibleBy3(i) && divisibleBy5(i)) console.log(i + " : spiders");
     else if(divisibleBy3(i)) console.log(i + " : cats");
     else if(divisibleBy5(i)) console.log(i + " : bats");
 }

 function divisibleBy3(num) {
    return num % 3 == 0;
 }

 function divisibleBy5(num) {
    return num % 5 == 0;
 }