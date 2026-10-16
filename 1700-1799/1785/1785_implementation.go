package main

import "fmt"

// the smallest number for each word, from the largest down
var from = []int{1000, 500, 250, 100, 50, 20, 10, 5, 1}
var words = []string{
	"legion", "zounds", "swarm", "throng", "horde", "lots", "pack", "several", "few",
}

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	i := 0
	for n < from[i] {
		i++
	}
	fmt.Println(words[i])
}
