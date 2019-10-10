//Author: Ajay Bhave
//Language:CPP
//Github:LusiferAjay
#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    for(int i=1;i<=100;i++)
    {
        if(i%15==0)
            cout<<"spiders";
        else if(i%5==0)
            cout<<"bats";
        else if(i%3==0)
            cout<<"cats";
        else
            cout<<i;
        cout<<endl;
    }
    return(0);
}
