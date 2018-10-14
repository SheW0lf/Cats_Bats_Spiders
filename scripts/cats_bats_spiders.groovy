// Author: Ravi
// Language: Groovy
// Github: https://github.com/ksr1122

def get(number) {
  switch (number) {
      case { it % 15 == 0 }: return "spiders"
      case { it % 3 == 0 }: return "cats"
      case { it % 5 == 0 }: return "bats"
      default: return number
  }     
}

(1..100).each{ 
    println get(it)
}