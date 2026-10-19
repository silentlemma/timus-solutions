package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const trio = 3

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	times := make([]int, n)
	for i := range times {
		fmt.Fscan(in, &times[i])
	}
	sort.Ints(times)
	total := 0
	// move the two slowest across each round, in whichever of two ways is
	// cheaper: the fastest escorts each of them, or the two fastest cross,
	// one comes back, the two slowest cross together and the other returns
	for len(times) > trio {
		a, b, y, z := times[0], times[1], times[len(times)-2], times[len(times)-1]
		escort, pair := 2*a+y+z, a+2*b+z
		if escort < pair {
			total += escort
		} else {
			total += pair
		}
		times = times[:len(times)-2]
	}
	if len(times) == trio {
		total += times[0] + times[1] + times[2]
	} else {
		total += times[len(times)-1]
	}
	fmt.Println(total)
}
