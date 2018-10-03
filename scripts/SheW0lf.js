//AUTHOR: Amber Cyr
//LANGUAGE: JavaScript
//GITHUB: https://github.com/SheW0lf

for(i = 1; i <= 100; i++){
    if(i % 3 === 0){
      if(i % 5 === 0){
        console.log('spiders');
      }
      console.log('cats');
    }else if(i % 5 === 0){
      console.log('bats');
    }else{
      console.log(i);
    }
  }