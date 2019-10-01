//Author:Adityadesle adityadesle
//Language:case
//Github:https://github.com/adityadesle

#include<stdio.h>
#include<conio.h>

void main()
{
    int i;
    clrscr();
    for ( i =1 ; i <=100; i++) {
      {
        if(i%3==0)
        {
           printf("%d",i);

        }
        else if(i%5==0)
        {
          printf("%d",i);
        }
        else if(i%3==0 && i%5==0)
        {
          printf("%d",i);
        }
        else
        {
          printf("%d",i);
        }
      }
      /* code */
    }
}
