package main

import "fmt"

const (
	flows   = 12
	minutes = 10
	nibble  = 4 // a need is at most 10 minutes, four bits in the memo key
)

// crosses lists the flows each flow crosses or merges with, read off the
// crossing: 1-3 come from the south, 4-6 from the east, 7-9 from the north
// and 10-12 from the west, each turning right, going straight on and left.
var crosses = [flows][]int{
	{9, 11}, {4, 5, 6, 9, 11, 12}, {5, 6, 7, 8, 11, 12}, {2, 12}, {2, 3, 7, 8, 9, 12},
	{2, 3, 8, 9, 10, 11}, {3, 5}, {3, 5, 6, 10, 11, 12}, {1, 2, 5, 6, 11, 12},
	{6, 8}, {1, 2, 3, 6, 8, 9}, {2, 3, 4, 5, 8, 9},
}

var (
	sets   [][]int
	widest int
	memo   = map[uint64]bool{}
)

// fits tells whether left green phases can serve every flow its need.
func fits(need [flows]int, left int) bool {
	top, total, key := 0, 0, uint64(left)
	for i, x := range need {
		total += x
		key = key<<nibble | uint64(x)
		if x > need[top] {
			top = i
		}
	}
	if need[top] > left || total > widest*left {
		return false
	}
	if total == 0 {
		return true
	}
	if v, ok := memo[key]; ok {
		return v
	}
	// some minute must open the flow that still needs the most
	ok := false
	for _, set := range sets {
		opens := false
		for _, i := range set {
			opens = opens || i == top
		}
		if !opens || ok {
			continue
		}
		rest := need
		for _, i := range set {
			if rest[i] > 0 {
				rest[i]--
			}
		}
		ok = fits(rest, left-1)
	}
	memo[key] = ok
	return ok
}

func main() {
	var cars, speed [flows]int
	for i := range cars {
		fmt.Scan(&cars[i])
	}
	for i := range speed {
		fmt.Scan(&speed[i])
	}
	var conflict [flows]int
	for flow, others := range crosses {
		for _, other := range others {
			conflict[flow] |= 1 << uint(other-1)
		}
	}
	// a minute lets through a set of flows that cross nowhere; it never hurts
	// to open more, so only the maximal such sets matter
	for mask := 1; mask < 1<<flows; mask++ {
		free, maximal := true, true
		var set []int
		for i := 0; i < flows; i++ {
			in, cross := mask>>uint(i)&1 == 1, conflict[i]&mask != 0
			free = free && !(in && cross)
			maximal = maximal && (in || cross)
			if in {
				set = append(set, i)
			}
		}
		if free && maximal {
			sets = append(sets, set)
			if len(set) > widest {
				widest = len(set)
			}
		}
	}
	lo, hi := 0, 0
	for _, c := range cars {
		if c > hi {
			hi = c
		}
	}
	for lo < hi {
		mid := (lo + hi) / 2
		var need [flows]int
		small := true
		for i := range need {
			if cars[i] > mid {
				need[i] = (cars[i] - mid + speed[i] - 1) / speed[i]
			}
			small = small && need[i] <= minutes
		}
		if small && fits(need, minutes) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	fmt.Println(lo)
}
