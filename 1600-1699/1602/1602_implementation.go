package main

import (
	"fmt"
	"strconv"
	"strings"
)

const (
	hundred = 100          // times are kept in hundredths of a second, exactly
	stand   = 15 * hundred // the lift stands this long on the first floor
	board   = 5 * hundred  // getting into the lift
	digits  = 2
)

// hundredths turns a number with at most two decimals into an exact integer of hundredths.
func hundredths(word string) int64 {
	parts := strings.SplitN(word, ".", 2)
	whole, _ := strconv.Atoi(parts[0])
	frac := "00"
	if len(parts) == 2 {
		frac = (parts[1] + "00")[:digits]
	}
	f, _ := strconv.Atoi(frac)
	return int64(whole*hundred + f)
}

func main() {
	var n, k int64
	var us, vs string
	if _, err := fmt.Scan(&n, &k, &us, &vs); err != nil {
		return
	}
	u, v := hundredths(us), hundredths(vs)
	// walking all the way down needs no lift
	bestFloor, bestTime := int64(1), (n-1)*u
	ready := (k-1)*v + stand // the lift may leave the first floor from then on
	for f := int64(2); f <= n; f++ {
		// Petya calls the lift on reaching floor f; it comes up, waits for
		// the boarding and goes down again
		start := ready
		if (n-f)*u > start {
			start = (n - f) * u
		}
		total := start + (f-1)*v + board + (f-1)*v
		// a later floor means less walking, so ties go to it
		if total <= bestTime {
			bestFloor, bestTime = f, total
		}
	}
	fmt.Println(bestFloor)
}
