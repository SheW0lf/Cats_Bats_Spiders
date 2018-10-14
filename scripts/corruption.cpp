//Author: Sandeep Pillai
//Language: C++ 11
//Github: github.com/corruption13

#include <iostream>

int main(){
for(int i=1; i<=100; i++)
{
	if(i % 15 == 0) 
       	    std::cout<<"Spiders" ;

	else if(i % 3 == 0)
 	    std::cout<<"Cats" ;

	else if(i % 5 == 0)
	    std::cout<<"Bats" ;

	else
	    std::cout<<i ;

	std::cout<<'\n' ;




return 0 ;

}
//@san.pai_
