// Author: Jarrod Yellets
// Language: JavaScript
//Github:  https://github.com/jarrodyellets

for (i = 1; i <= 100; i++){
  if (i % 3 === 0 && i % 5 === 0){
    console.log('spiders');
  } else if (i % 3 === 0){
    console.log('cats');
  } else if (i % 5 === 0){
    console.log('bats');
  } else {
    console.log(i);
  }
}
