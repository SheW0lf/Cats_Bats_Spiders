// Author: stocky89
// Language: C++
// Github: https://github.com/stocky89

#include <iostream>
using namespace std;

int main()
{
  for(int i=1; i<=100; i++) {
    if (!(i % 3) && !(i % 5)) std::cout << "spiders" << endl;
    else if (!(i % 3)) std::cout << "cats" << endl;
    else if (!(i % 5)) std::cout << "bats" << endl;
    else std::cout << i << endl;
  }

  return 0;
}
