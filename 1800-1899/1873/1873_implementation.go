package main

import "fmt"

// contests played by players 0 to 13, counted from the story
var contests = []int{5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1}

func main() {
	var player int
	fmt.Scan(&player)
	fmt.Println(contests[player])
}
