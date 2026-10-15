package main

import "fmt"

var (
	k, longest int
	word       []int
	counts     [][]int64
)

// repetitionAtEnd tells whether some k-repetition ends at the last letter
// of word.
func repetitionAtEnd() bool {
	size := len(word)
	for block := 1; block*k <= size; block++ {
		i := size - k*block
		for i < size-block && word[i] == word[i+block] {
			i++
		}
		if i == size-block {
			return true
		}
	}
	return false
}

// properRepetition tells whether w^k has a k-repetition other than itself:
// w has none, and w^k repeats with period |w|, so only windows that start
// in the first copy and leave it need a look.
func properRepetition() bool {
	size := len(word)
	total := size * k
	for block := 1; block <= size; block++ {
		span := k * block
		for start := 0; start < size && start <= total-span; start++ {
			if start+span <= size || span == total {
				continue
			}
			i, end := start, start+span-block
			for i < end && word[i%size] == word[(i+block)%size] {
				i++
			}
			if i == end {
				return true
			}
		}
	}
	return false
}

func extend(distinct int) {
	// w^k may fail while a longer w still works, so this only skips counting
	if len(word) > 0 && !properRepetition() {
		counts[len(word)][distinct]++
	}
	if len(word) == longest {
		return
	}
	for c := 0; c <= distinct; c++ {
		word = append(word, c)
		// a k-repetition inside w is one inside the killer word too
		if !repetitionAtEnd() {
			next := distinct
			if c == distinct {
				next++
			}
			extend(next)
		}
		word = word[:len(word)-1]
	}
}

func main() {
	var m, n int
	fmt.Scan(&m, &k, &n)
	// a killer word is w repeated k times; whether it works does not depend
	// on which letters w uses, so count the words w with letters numbered in
	// order of first appearance, by their number of different letters
	longest = n / k
	counts = make([][]int64, longest+1)
	for i := range counts {
		counts[i] = make([]int64, longest+1)
	}
	extend(0)
	total := int64(0)
	for length := 1; length <= longest; length++ {
		ways := int64(1)
		for distinct := 1; distinct <= length; distinct++ {
			factor := m - distinct + 1
			if factor < 0 {
				factor = 0
			}
			ways *= int64(factor)
			total += counts[length][distinct] * ways
		}
	}
	fmt.Println(total)
}
