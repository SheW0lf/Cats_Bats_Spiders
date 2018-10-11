#include <iostream>
using namespace std;

int main()
{
	for (int i = 1; i <= 100; i++) {
		if (i % 15 == 0) {
			cout << "spider" << endl; 
		}
		else if(i % 5 == 0){
			cout << "bats" << endl;
		}
		else if (i % 3 == 0) {
			cout << "cats" << endl;
		}
		else {
			cout << i << endl;
		}
	}
    return 0;
}
