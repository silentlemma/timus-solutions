package main

import "fmt"

func main() {
	var harry, larry int
	fmt.Scan(&harry, &larry)
	// the last can was shot by both, so each missed the other's count minus one
	fmt.Println(larry-1, harry-1)
}
