package main

import (
	"fmt"
	"strings"
)

const (
	disks  = 4
	petals = 3
	bits   = disks + petals
)

// petal j lies in every disk except disk j
func valid(word []int) bool {
	total := 0
	for d := 0; d < disks; d++ {
		total += word[d]
	}
	for j := 0; j < petals; j++ {
		if (total-word[j])%2 != word[disks+j] {
			return false
		}
	}
	return true
}

func main() {
	word := make([]int, bits)
	for i := range word {
		if _, err := fmt.Scan(&word[i]); err != nil {
			return
		}
	}
	// try the word as it is, then each single change
	for k := -1; k < bits; k++ {
		if k >= 0 {
			word[k] ^= 1
		}
		if valid(word) {
			break
		}
		if k >= 0 {
			word[k] ^= 1
		}
	}
	fmt.Println(strings.Trim(fmt.Sprint(word), "[]"))
}
