# Author: jwon114
# Language: Ruby
# Github: https://github.com/jwon114

def cats_bats_spiders
	(1..100).each do |num|
		if num % 5 == 0 && num % 3 == 0
			puts 'spiders'
		elsif num % 5 == 0
			puts 'bats'
		elsif num % 3 == 0  
			puts 'cats'
		else
			puts num
		end
	end
end

cats_bats_spiders