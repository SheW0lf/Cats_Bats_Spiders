// Author: Dario
// Language: C++
// Github: DDTyphos
#include <iostream>
using namespace std;

int main()
{
	for(int num=1; num <=100; ++num)
	{
		if((num % 5 == 0) && (num % 3 == 0))
			cout << "Spider " << endl;
		else if(num % 5 == 0)
			cout << "Bats " << endl;
		else if(num % 3 == 0)
			cout << "Cats" << endl;
		else
			cout << num << ' ' << endl;
	}
	return 0;
}