package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxFloors, maxEggs = 1000, 10

func main() {
	var best [maxEggs + 1][maxFloors + 1]int
	for floors := 1; floors <= maxFloors; floors++ {
		best[1][floors] = floors
	}
	// Ten eggs suffice for binary search. The direct recurrence tries
	// every first floor and minimizes the worse of the two outcomes.
	for eggs := 2; eggs <= maxEggs; eggs++ {
		for floors := 1; floors <= maxFloors; floors++ {
			best[eggs][floors] = floors
			for first := 1; first <= floors; first++ {
				worse := best[eggs-1][first-1]
				if best[eggs][floors-first] > worse {
					worse = best[eggs][floors-first]
				}
				if worse+1 < best[eggs][floors] {
					best[eggs][floors] = worse + 1
				}
			}
		}
	}
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	for {
		var eggs, floors int
		if _, err := fmt.Fscan(input, &eggs, &floors); err != nil || eggs == 0 && floors == 0 {
			break
		}
		if eggs > maxEggs {
			eggs = maxEggs
		}
		fmt.Fprintln(output, best[eggs][floors])
	}
}
