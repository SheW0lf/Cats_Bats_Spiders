// Author: Shubham Bhandari
// Language: Python 3.7
// Github: https://github.com/dev-SB


class Main {
    public static void main(String args[]) {
        for (int i = 1; i < 101; i++) {
            if (i % 15 == 0) {
                System.out.println("spiders");
            } else if (i % 3 == 0) {
                System.out.println("cats");
            } else if (i % 5 == 0) {
                System.out.println("bats");
            } else {
                System.out.println(i);
            }
        }
    }
}
