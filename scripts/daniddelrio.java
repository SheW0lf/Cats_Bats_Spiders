/*
Author: Daniel Del Rio
Language: Java
Github: https://github.com/daniddelrio
*/

public class daniddelrio {

	public static void main(String[] args) {
		recursion(1);
	}

	public static void recursion(int counter) {
		if(counter == 101) {
			return;
		}

		if(counter % 5 == 0) {
			if(counter % 3 == 0) {
				System.out.println("spiders");
			}
			else {
				System.out.println("bats");
			}
		}
		else if (counter % 3 == 0) {
			System.out.println("cats");
		}
		else {
			System.out.println(counter);
		}
		
		recursion(counter+1);
	}
}