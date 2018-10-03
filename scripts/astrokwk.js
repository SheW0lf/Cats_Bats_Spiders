//Author: Amy K
//Language: Javascript
//Github: AstroKwk


for (var i = 1; i <= 100; i++) {
		if (i % 3 === 0 && i % 5 === 0) {
			console.log('Spider');
		} else if (i % 3 === 0) {
			console.log('Cat');
		} else if (i % 5 === 0) {
			console.log('Bat');
		} else {
			console.log(i);
		}
	}