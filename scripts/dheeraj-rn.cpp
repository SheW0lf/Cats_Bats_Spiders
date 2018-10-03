//AUTHOR: Dheeraj
//LANGUAGE: C++
//GITHUB: https://github.com/dheeraj-rn

#include <iostream>
using namespace std;

int main() {
	for(int i=1; i<=100; i++) {
        if(i % 3 == 0){
            if(i % 5 == 0){
                cout<<"spiders\n";
            }else{
            cout<<"cats\n";
            }
        }else if(i % 5 == 0){
            cout<<"bats\n";
        }else{
            cout<<i<<"\n";
        }
    }
	return 0;
}
