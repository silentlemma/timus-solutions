package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// the fuses burn on the odd days; (x + 1) / 2 odd days are in 1..x
	fmt.Println((b+1)/2 - a/2)
}
