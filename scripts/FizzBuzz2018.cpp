#include <stdio.h>

int main()
{	
	int i;
	
	for(i = 1; i <= 100; i++){
		if(i % 3 == 0 && i % 5 == 0){
			printf("spiders\n");
		}
		else if(i % 3 == 0){
			printf("cats\n");
		}else if(i % 5 == 0){
			printf("bats\n");
		}else{
			printf("%d\n",i);
		}
	}
	return 0;
}