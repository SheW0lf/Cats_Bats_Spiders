<?php

	//AUTHOR: Matt Keith
	//LANGUAGE: PHP
	//GITHUB: https://github.com/RedYetiCo

	for( $i = 1; $i <= 100; $i ++ ) {
		if( $i % 3 == 0 && $i % 5 == 0 ) {
			echo "\nSpider!";
			continue;
		}
		if( $i % 3 == 0 ) {
			echo "\nCat!";
			continue;
		}
		if( $i % 5 == 0 ) {
			echo "\nBat!";
			continue;
		}
		echo "\n".$i;
	}
