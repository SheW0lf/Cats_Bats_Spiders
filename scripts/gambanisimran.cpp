// Author: Simran Gambani
// Language: C++
// Github: https://github.com/gambani-simran

#include<iostream>
using namespace std;

int main(){
	for(int i=1;i<=100;i++)
	{	//using ternary conditional operator	
		(i%3==0) ? ((i%5==0) ? cout<<"spiders\n" : cout<<"cats\n") : ((i%5==0) ? cout<<"bats\n" : cout<<i<<endl);	
	}
	return 0;
}
