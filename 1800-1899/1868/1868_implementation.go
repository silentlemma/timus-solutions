package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	perMedal = 4
	prize    = 5
)

var medals = []string{"gold", "silver", "bronze"}

func main() {
	reader := bufio.NewReader(os.Stdin)
	medal := map[string]string{}
	for _, kind := range medals {
		for i := 0; i < perMedal; i++ {
			var team string
			fmt.Fscan(reader, &team)
			medal[team] = kind
		}
	}
	var n int
	fmt.Fscan(reader, &n)
	scores := make([]int, n)
	best := 0
	for p := range scores {
		var k int
		fmt.Fscan(reader, &k)
		for i := 0; i < k; i++ {
			var team, colon, kind string
			fmt.Fscan(reader, &team, &colon, &kind)
			if got, ok := medal[team]; ok && got == kind {
				scores[p]++
			}
		}
		if scores[p] > best {
			best = scores[p]
		}
	}
	winners := 0
	for _, s := range scores {
		if s == best {
			winners++
		}
	}
	fmt.Println(prize * winners)
}
