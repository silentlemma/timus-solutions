package main

import (
	"bufio"
	"math/big"
	"os"
	"strconv"
)

const alphabetSize = 10

func nextInt(input *bufio.Scanner) int64 {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return int64(value)
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	length, sum := nextInt(input), nextInt(input)
	maximum := length * (alphabetSize - 1)
	target := sum / 2
	if sum%2 != 0 || target > maximum {
		os.Stdout.WriteString("0\n")
		return
	}
	if maximum-target < target {
		target = maximum - target
	}

	// Count digit strings by excluding assignments with a digit at least ten.
	var count, subsets, compositions big.Int
	for excluded := int64(0); excluded <= target/alphabetSize; excluded++ {
		subsets.Binomial(length, excluded)
		compositions.Binomial(target-excluded*alphabetSize+length-1, length-1)
		compositions.Mul(&compositions, &subsets)
		if excluded%2 == 0 {
			count.Add(&count, &compositions)
		} else {
			count.Sub(&count, &compositions)
		}
	}
	count.Mul(&count, &count)
	os.Stdout.WriteString(count.String() + "\n")
}
