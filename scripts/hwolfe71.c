// Author: Herb Wolfe
// Language: C
// Github: github.com/hwolfe71

#include <stdio.h>

void main() {
	int cats = 3;
	int bats = 5;
	int spiders = 15;
	int max = 100;

	for(int i = 1; i <= max; i++) {
		if (i % spiders == 0) {
			printf("spiders\n");
		} else if (i % cats == 0) {
			printf("cats\n");
		} else if (i % bats == 0) {
			printf("bats\n");
		} else {
			printf("%d\n", i);
		}
	}
}
