package main

import (
	"fmt"
	"sort"
)

func main() {
	var k int
	fmt.Scan(&k)
	size := make([]int, k)
	for i := range size {
		fmt.Scan(&size[i])
	}
	// win a majority of the groups, choosing the smallest ones; a group of s
	// voters needs s / 2 + 1 supporters
	sort.Ints(size)
	supporters := 0
	for _, s := range size[:k/2+1] {
		supporters += s/2 + 1
	}
	fmt.Println(supporters)
}
