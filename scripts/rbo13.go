//AUTHOR: Richard Burk
//LANGUAGE: Golang
//GITHUB: https://github.com/rbo13

package main

import "fmt"

func main() {
	catsBatsSpiders()
}

func catsBatsSpiders() {
	for i := 1; i <= 100; i++ {
		if i%3 == 0 {
			if i%5 == 0 {
				fmt.Println("spiders")
			}
			fmt.Println("cats")
		} else if i%5 == 0 {
			fmt.Println("bats")
		} else {
			fmt.Println(i)
		}
	}
}
