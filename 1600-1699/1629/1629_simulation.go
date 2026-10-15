package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	day  = 1440
	hour = 60
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	now := 0
	for i := 1; i < n; i++ {
		var q, delay, flight int
		fmt.Fscan(in, &q, &delay, &flight)
		best := -1
		for j := 0; j < q; j++ {
			var word string
			fmt.Fscan(in, &word)
			parts := strings.Split(word, ":")
			hours, _ := strconv.Atoi(parts[0])
			minutes, _ := strconv.Atoi(parts[1])
			leave := hours*hour + minutes + delay
			if leave < now { // the same flight on a later day
				leave += (now - leave + day - 1) / day * day
			}
			if best < 0 || leave < best {
				best = leave
			}
		}
		now = best + flight
	}
	fmt.Println(now)
}
