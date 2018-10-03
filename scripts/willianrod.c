#include <stdio.h>

int main () {
    for(int i=1; i<=100; i++) {
        if(i % 3 == 0){
            if(i % 5 == 0){
                printf("spiders\n");
            }
            printf("cats\n");
        }else if(i % 5 == 0){
            printf("bats\n");
        }else{
            printf("%d\n", i);
        }
    }
    return 0;
}