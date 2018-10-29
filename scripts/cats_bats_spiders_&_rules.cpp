#include <iostream>
#include <functional>
#include <algorithm>


const int LOOPS = 100;

struct Rule {
	std::function<bool(int)> condition;
	std::function<void(int)> action;
};

void apply_rules(int n, std::initializer_list<Rule> rules) {
	const auto it = std::find_if(rules.begin(), rules.end(), [n](auto e) { return e.condition(n); });
	if(it != rules.end())
		it->action(n);
}

int main() {

	std::initializer_list<Rule> rules = { 
		Rule{
			[](int n) { return n % 3 == 0 && n % 5 == 0;  },
			[](int n) { std::cout << "Spiders" << '\n'; }
		},
		Rule{
			[](int n) { return n % 3 == 0; },
			[](int n) { std::cout << "Cats" << '\n'; }
		},
		Rule{
			[](int n) { return n % 5 == 0; },
			[](int n) { std::cout << "Bats" << '\n'; }
		},
		Rule{
			[](int n) { return true;  },
			[](int n) { std::cout << n << '\n'; }
		}
	};


	for (int i = 1; i <= LOOPS; i++)
		apply_rules(i, rules);
	

	getchar();

}