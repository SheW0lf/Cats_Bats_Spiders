// Author: dumblole
// Language: Java
// Github: https://github.com/dumblole

import java.lang.Math; 


public class CatsBatsSpiders
{
  
  public static void main(String[] args)
  {
    for (int i=1; i<=100; i++) {
      if (i%5 == 0 && i%3 == 0) {
        System.out.println("spiders");
      } else if (i%3 == 0) {
        System.out.println("cats");
      } else if (i%5 == 0) {
        System.out.println("bats");
      } else {
        System.out.println(i);
      }
}
  }
}

