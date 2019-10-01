# Author: Pranit Brahmbhatt
# Language: Dart
# Github : pb-10


void main() {
    for (var i = 1; i <= 100; i++) {
        if (i % 3 == 0) {
            print("cats");
        }
	    else if (i % 5 == 0) {
            print("bats");
        }
        else if (i % 15 == 0) {
            print("spiders");
        }
	    else {
            print(i);
        }
    }
}