package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const (
	percent  = 100
	maxPrice = 50000
)

type scanner struct {
	data []byte
	pos  int
}

func (in *scanner) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

func upperBound(values []int, limit int) int {
	left, right := 0, len(values)
	for left < right {
		middle := (left + right) / 2
		if values[middle] <= limit {
			left = middle + 1
		} else {
			right = middle
		}
	}
	return left
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n, m := in.nextInt(), in.nextInt()
	var prices [percent + 1][]int
	var prefix [percent + 1][]int64
	var count [percent + 1]int
	var priceSum, weightedSum [percent + 1]int64
	var minimum [percent + 1]int
	var singles int64
	for i := 0; i < n; i++ {
		price, discount := in.nextInt(), in.nextInt()
		prices[discount] = append(prices[discount], price)
		singles += int64(price) * int64(percent-discount)
	}
	for p := 0; p <= percent; p++ {
		minimum[p] = n + 1
	}
	for i := 0; i < m; i++ {
		needed, discount := in.nextInt(), in.nextInt()
		if needed < minimum[discount] {
			minimum[discount] = needed
		}
	}
	for d := 0; d <= percent; d++ {
		sort.Ints(prices[d])
		prefix[d] = make([]int64, len(prices[d])+1)
		for i, price := range prices[d] {
			prefix[d][i+1] = prefix[d][i] + int64(price)
		}
		groupSum := prefix[d][len(prices[d])]
		count[d] = len(prices[d])
		priceSum[d] = groupSum
		weightedSum[d] = groupSum * int64(d)
		if d > 0 {
			count[d] += count[d-1]
			priceSum[d] += priceSum[d-1]
			weightedSum[d] += weightedSum[d-1]
		}
	}
	best, smallestRequirement := singles, n+1
	for p := percent; p > 0; p-- {
		if minimum[p] >= smallestRequirement {
			continue
		}
		smallestRequirement = minimum[p]
		candidate := singles + weightedSum[p] - int64(p)*priceSum[p]
		if candidate >= best {
			continue
		}
		needed := minimum[p] - count[p]
		if needed > 0 {
			// Find the last penalty among the required cheapest extra tickets.
			left, right := 0, maxPrice*(percent-p)
			for left < right {
				middle := (left + right) / 2
				taken := 0
				for d := p + 1; d <= percent; d++ {
					taken += upperBound(prices[d], middle/(d-p))
				}
				if taken >= needed {
					right = middle
				} else {
					left = middle + 1
				}
			}
			taken := 0
			for d := p + 1; d <= percent; d++ {
				amount := upperBound(prices[d], left/(d-p))
				taken += amount
				candidate += prefix[d][amount] * int64(d-p)
			}
			candidate -= int64(taken-needed) * int64(left)
		}
		if candidate < best {
			best = candidate
		}
	}
	fmt.Printf("%d.%02d\n", best/percent, best%percent)
}
