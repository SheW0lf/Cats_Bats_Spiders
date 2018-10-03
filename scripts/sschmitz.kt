// Author: Scott Schmitz
// Language: Kotlin
// Github: https://github.com/scottschmitz

fun main(args: Array<String>) {
    for (i in 1..100) {
        when {
            (i % 3 == 0 && i % 5 == 0) -> println("spiders")
            (i % 3 == 0) -> println("cats")
            (i % 5 == 0) -> println("bats")
            else -> println(i)
        }
    }
}
