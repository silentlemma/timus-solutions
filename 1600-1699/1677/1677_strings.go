package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int64
	var word string
	fmt.Fscan(in, &n, &word)
	size := len(word)
	// prefix function: pi[i] is the longest border of word[:i+1]
	pi := make([]int, size)
	for i := 1; i < size; i++ {
		j := pi[i-1]
		for j > 0 && word[i] != word[j] {
			j = pi[j-1]
		}
		if word[i] == word[j] {
			j++
		}
		pi[i] = j
	}
	// the expected time is the sum of n^k over the lengths k of the word's
	// borders, the whole word included: a number whose base-n digits are 0
	// and 1, built by Horner's rule from the top digit down
	border := make([]bool, size+1)
	for k := size; k > 0; k = pi[k-1] {
		border[k] = true
	}
	base, one := big.NewInt(n), big.NewInt(1)
	total := new(big.Int)
	for k := size; k > 0; k-- {
		total.Mul(total, base)
		if border[k] {
			total.Add(total, one)
		}
	}
	total.Mul(total, base)
	fmt.Println(total.String())
}
