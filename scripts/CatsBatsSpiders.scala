/**
* Author: Damian Dabrowski
* Language: Scala
* Github:
*/

object CatsBatsSpiders {
   def main(args: Array[String]) {
      var i = 0;

      // for loop execution with a range
      for( i <- 1 to 100){
         if (i % 3 == 0) {
             if (i % 5 == 0 ) {
                 println("Spiders")
             } else {
                 println("Cats")
             }
         } else if (i % 5 == 0) {
             println("Bats")
         } else {
             println(i)
         }
      }
   }
}