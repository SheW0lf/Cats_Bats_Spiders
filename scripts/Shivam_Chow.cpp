//Author: Shivam175
//Language: C++ 14
//Github: https://github.com/Shivam175
#include <iostream>
using namespace std;

int main(){
    int i{1};
    while(i<101){
        if(i%15==0)
            cout<<"spiders"<<endl;
        else if(i%3==0)
            cout<<"cats"<<endl;
        else if(i%5==0)
            cout<<"bats"<<endl;
        else
            cout<<i<<endl;
        i++;
    }return 0;
}