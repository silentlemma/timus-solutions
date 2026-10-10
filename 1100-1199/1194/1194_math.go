package main

import "fmt"

func main() {
	var n, k int64
	fmt.Scan(&n, &k)
	// every two hobbits shake hands exactly once, when their groups part,
	// except the married couples, who go home together and never part
	fmt.Println(n*(n-1)/2 - k)
}
