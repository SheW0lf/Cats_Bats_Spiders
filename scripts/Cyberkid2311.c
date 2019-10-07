//Author:Cyberkid2311
//Language:C
//Github:https://github.com/Cyberkid2311

#include<stdio.h>
#include<conio.h>

void main()
{
    int i;
    for(i=1;i<=100;i++)
    {
        if(i%3==0&&i%5==0)
        {
            printf("spiders\n");
        }
        else if(i%3==0)
        {
            printf("cats\n");
        }
        else if(i%5==0)
        {
            printf("bats\n");
        }
        else
        {
            printf("%d\n",i);
        }
    }
}
