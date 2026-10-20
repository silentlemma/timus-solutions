package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	ternaryBase = 3
	wordBits    = 64
	maxDPSum    = 50000000
)

func collectBeautiful(value, pattern, mask, limit int, beautiful *[]int) {
	for remaining := value; remaining >= pattern; remaining >>= 1 {
		if remaining&mask == pattern {
			*beautiful = append(*beautiful, value)
			break
		}
	}

	for digit := 0; digit < 2; digit++ {
		child := value*ternaryBase + digit
		if child <= limit {
			collectBeautiful(child, pattern<<1|digit, mask<<1|1, limit, beautiful)
		}
	}
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()

	var count int
	fmt.Fscan(input, &count)
	queries := make([]int, count)
	limit := 0
	for index := range queries {
		fmt.Fscan(input, &queries[index])
		if queries[index] > limit {
			limit = queries[index]
		}
	}

	beautiful := []int{}
	collectBeautiful(1, 1, 1, limit, &beautiful)
	sort.Ints(beautiful)
	smallTotal, split := 0, 0
	for split < len(beautiful) && smallTotal+beautiful[split] <= maxDPSum {
		smallTotal += beautiful[split]
		split++
	}

	reachable := make([]uint64, smallTotal/wordBits+1)
	reachable[0] = 1
	currentTotal := 0
	for _, value := range beautiful[:split] {
		whole, part := value/wordBits, uint(value%wordBits)
		currentTotal += value
		// Descending updates use each beautiful number at most once.
		for target := currentTotal / wordBits; target >= whole; target-- {
			source := target - whole
			shifted := reachable[source] << part
			if part != 0 && source > 0 {
				shifted |= reachable[source-1] >> (wordBits - part)
			}
			reachable[target] |= shifted
		}
	}

	highSums := []int{0}
	for _, value := range beautiful[split:] {
		previousSize := len(highSums)
		for subset := 0; subset < previousSize; subset++ {
			highSums = append(highSums, highSums[subset]+value)
		}
	}
	sort.Ints(highSums)

	for _, value := range queries {
		found := false
		for _, highSum := range highSums {
			lowSum := value - highSum
			if lowSum < 0 {
				break
			}
			if lowSum <= smallTotal &&
				(reachable[lowSum/wordBits]>>uint(lowSum%wordBits))&1 != 0 {
				found = true
				break
			}
		}
		if found {
			fmt.Fprintln(output, "YES")
		} else {
			fmt.Fprintln(output, "NO")
		}
	}
}
