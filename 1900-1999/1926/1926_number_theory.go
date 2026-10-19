package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 614889782588491410

type query struct {
	kind   int
	first  int64
	second int64
}

func processQueries(number string, queries []query) []int64 {
	digits := []byte(number)
	weights := make([]int64, len(digits))
	weights[0] = 1
	for index := 1; index < len(weights); index++ {
		weights[index] = weights[index-1] * 10 % modulus
	}
	var remainder int64
	for _, digit := range digits {
		remainder = (remainder*10 + int64(digit-'0')) % modulus
	}
	answers := make([]int64, 0)
	for _, entry := range queries {
		if entry.kind == 0 {
			answers = append(answers, remainder%entry.first)
		} else {
			place := int(entry.first)
			index := len(digits) - place
			difference := entry.second - int64(digits[index]-'0')
			digits[index] = '0' + byte(entry.second)
			remainder = (remainder + difference*weights[place-1]) % modulus
			if remainder < 0 {
				remainder += modulus
			}
		}
	}
	return answers
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var number string
	var count int
	fmt.Fscan(input, &number, &count)
	queries := make([]query, count)
	for index := range queries {
		fmt.Fscan(input, &queries[index].kind, &queries[index].first)
		if queries[index].kind == 1 {
			fmt.Fscan(input, &queries[index].second)
		}
	}
	for _, answer := range processQueries(number, queries) {
		fmt.Fprintln(output, answer)
	}
}
