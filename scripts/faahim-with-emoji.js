// Author: Afiur Rahman Fahim
// Language: JavaScript
// Github: https://github.com/faahim


let number = 1;

while (number <= 100) {
  // Check whether the number is a multiples of 3
  (number % 3 === 0) ? (
    // Check whether the number is also a multiples of 5
    number % 5 === 0 ? console.log('Spiders 🕷️') : console.log('Cats 😺')
  ) : (
    // If not mutiples of 3, or both 3 & 5, check if it's a multiple of 5
    // If not, print out the number
    number % 5 === 0 ? console.log('Bats 🦇') : console.log(number)
  );

  number = number + 1;
 }