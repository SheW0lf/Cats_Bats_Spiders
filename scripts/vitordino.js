// Author: Vitor Dino
// Language: JavaScript (ES6)
// Github: http://github.com/vitordino

[...Array(101).keys()]
  .slice(1)
  .map(x => !(x % 15) ? '🕷' : !(x % 5) ? '🦇' : !(x % 3) ? '🐱' : x)
  .forEach(x => console.log(x))
