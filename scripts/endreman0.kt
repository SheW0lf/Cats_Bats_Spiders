// Author: Ian W
// Language: Kotlin
// GitHub: endreman0

fun main(args: Array<String>) {
    (1..100).map(::substitute).forEach { println(it) }
}

fun substitute(n: Int): String = if (n % 15 == 0) "spiders"
		else if (n % 3 == 0) "cats"
		else if (n % 5 == 0) "bats"
		else "$n"
