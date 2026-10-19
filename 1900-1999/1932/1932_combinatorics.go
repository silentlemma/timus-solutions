package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	digitCount   = 4
	hexBase      = 16
	digitBits    = 4
	digitMask    = hexBase - 1
	pairDomain   = hexBase * hexBase
	tripleDomain = pairDomain * hexBase
	pairGroups   = digitCount * (digitCount - 1) / 2
)

func newBuckets(groups, domain int) [][]int {
	buckets := make([][]int, groups)
	for index := range buckets {
		buckets[index] = make([]int, domain)
	}
	return buckets
}

func distanceHistogram(numbers []int) [digitCount]int64 {
	singles := newBuckets(digitCount, hexBase)
	pairs := newBuckets(pairGroups, pairDomain)
	triples := newBuckets(digitCount, tripleDomain)
	var singlePairs, doublePairs, triplePairs int64
	for _, number := range numbers {
		first := number >> (digitBits * (digitCount - 1))
		second := (number >> (2 * digitBits)) & digitMask
		third := (number >> digitBits) & digitMask
		fourth := number & digitMask
		singleKeys := [digitCount]int{first, second, third, fourth}
		for index, key := range singleKeys {
			singlePairs += int64(singles[index][key])
			singles[index][key]++
		}
		pairKeys := [pairGroups]int{number >> (2 * digitBits), first*hexBase + third,
			first*hexBase + fourth, (number >> digitBits) & (pairDomain - 1),
			second*hexBase + fourth, number & (pairDomain - 1)}
		for index, key := range pairKeys {
			doublePairs += int64(pairs[index][key])
			pairs[index][key]++
		}
		tripleKeys := [digitCount]int{number >> digitBits,
			(number>>(2*digitBits))*hexBase + fourth,
			first*pairDomain + (number & (pairDomain - 1)), number & (tripleDomain - 1)}
		for index, key := range tripleKeys {
			triplePairs += int64(triples[index][key])
			triples[index][key]++
		}
	}
	count := int64(len(numbers))
	distanceOne := triplePairs
	distanceTwo := doublePairs - (digitCount-1)*distanceOne
	distanceThree := singlePairs - 2*distanceTwo - (digitCount-1)*distanceOne
	distanceFour := count*(count-1)/2 - distanceOne - distanceTwo - distanceThree
	return [digitCount]int64{distanceOne, distanceTwo, distanceThree, distanceFour}
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(input, &count)
	numbers := make([]int, count)
	for index := range numbers {
		var token string
		fmt.Fscan(input, &token)
		number, _ := strconv.ParseUint(token, hexBase, digitBits*digitCount)
		numbers[index] = int(number)
	}
	answer := distanceHistogram(numbers)
	for index, value := range answer {
		if index > 0 {
			fmt.Print(" ")
		}
		fmt.Print(value)
	}
	fmt.Println()
}
