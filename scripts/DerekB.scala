/**
 * Author: derekb
 * Language: Scala
 * Github: https://github.com/derekb
 */
object CatBatSpider {
  def main(args : Array[String]): Unit = {
    (1 to 100).map(catBatSpider).foreach(println)
  }

  def catBatSpider(num: Int) : String = {
    num match {
      case i if i % 15 == 0 => "spiders"
      case i if i % 5 == 0  => "bats"
      case i if i % 3 == 0  => "cats"
      case i => s"${i}"
    }
  }
}