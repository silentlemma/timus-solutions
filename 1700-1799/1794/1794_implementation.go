package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Split(bufio.ScanWords)
	next := func() int {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return v
	}
	n := next()
	// votes[k]: how many students get their wish if student k starts
	votes := make([]int, n+1)
	for i := 1; i <= n; i++ {
		want := next()
		// student i speaks want-th when student i - want + 1 starts
		votes[((i-want)%n+n)%n+1]++
	}
	best := 1
	for k := 2; k <= n; k++ {
		if votes[k] > votes[best] {
			best = k
		}
	}
	fmt.Println(best)
}
