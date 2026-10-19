package main

import "fmt"

// page i open is bit i - 1 of a Gray code word: F1 flips bit 0, the other
// move flips the bit above the lowest set one; these are the reflected Gray
// code steps, so the states form one path ordered by the decoded word
func rank(pages string) int64 {
	var gray, place int64
	for i := len(pages) - 1; i >= 0; i-- {
		gray = gray*2 + int64(pages[i]-'0')
	}
	for ; gray != 0; gray >>= 1 {
		place ^= gray
	}
	return place
}

func main() {
	var n int
	var start, goal string
	if _, err := fmt.Scan(&n, &start, &goal); err != nil {
		return
	}
	diff := rank(start) - rank(goal)
	if diff < 0 {
		diff = -diff
	}
	fmt.Println(diff)
}
