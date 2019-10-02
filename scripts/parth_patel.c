// Author: Parth Patel
// Language: C Language
// Github: https://github.com/parth2102

#include<conio.h>
#include<stdio.h>

void main()
{
    int i;
    clrscr();
    for(i=1;i<=100;i++)
    {
      if(i%3==0)
      {
        printf("cats");
      }
      elseif(i%5==0)
      {
        printf("bats");
      }
      else(i%3==0 && i%5==0)
          {
            printf("spiders");
          }
    }
    getch();  
}
