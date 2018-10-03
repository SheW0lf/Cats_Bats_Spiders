/*
Author: Dhanraj Acharya
Language: NodeJS
Github: http://github.com/drex44
*/

catsBatsAndSpiders();
function catsBatsAndSpiders() {
  for (let i = 1; i <= 100; i++) {
    if (i % 5 == 0 && i % 3 == 0) {
      console.log("spiders");
    } else if (i % 5 == 0) {
      console.log("bats");
    } else if (i % 3 == 0) {
      console.log("cats");
    } else {
      console.log(i);
    }
  }
}
