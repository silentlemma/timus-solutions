package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const limit = 1000000000 // the largest absolute mood

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	next := func() int64 {
		scanner.Scan()
		value, _ := strconv.Atoi(scanner.Text())
		return int64(value)
	}
	n := int(next())
	a := make([]int64, n)
	smallest := int64(limit)
	for i := range a {
		a[i] = next()
		if a[i] < smallest {
			smallest = a[i]
		}
	}
	possible := func(x int64) bool {
		// Every mood below x must be flipped, so the shortest segment covers
		// them all, and every mood inside must become at least x.
		first, last := -1, -1
		for i, v := range a {
			if v < x {
				if first < 0 {
					first = i
				}
				last = i
			}
		}
		if first < 0 {
			return smallest <= -x // some single mood can still be flipped
		}
		for _, v := range a[first : last+1] {
			if v > -x {
				return false
			}
		}
		return true
	}
	lo, hi := int64(-limit), int64(limit)
	for lo < hi {
		middle := lo + (hi-lo+1)/2
		if possible(middle) {
			lo = middle
		} else {
			hi = middle - 1
		}
	}
	fmt.Println(lo)
}
