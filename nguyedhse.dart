#!/usr/bin/dart
# Author: Nguyen Do
# Language: Dart
# Github : nguyendhse


void main() {
    for (var i = 1; i < 101; i ++) {
        if (i % 15 == 0) print("spiders");
	else if (i % 3 == 0) print("cats");
	else if (i % 5 == 0) print("bats");
	else print(i);
    }
}
