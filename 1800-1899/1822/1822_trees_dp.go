package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const coordinateBits = 32

const (
	percent     = 100
	outputScale = 100000000
	precision   = 8
)

type fraction struct {
	num, den int32
}

func maximumShare(head, sibling, days []int32, deadline int32) fraction {
	n := len(head)
	order := make([]int32, 1, n)
	for i := 0; i < len(order); i++ {
		node := order[i]
		for child := head[node]; child != 0; child = sibling[child] {
			days[child] += days[node]
			order = append(order, child)
		}
	}

	limits := make([]fraction, n)
	var ranked []fraction
	for i := len(order) - 1; i >= 0; i-- {
		node := order[i]
		if days[node] > deadline {
			limits[node] = fraction{0, 1}
			continue
		}
		limits[node] = fraction{1, 1}
		ranked = ranked[:0]
		for child := head[node]; child != 0; child = sibling[child] {
			ranked = append(ranked, limits[child])
		}
		if len(ranked) > 1 {
			sort.Slice(ranked, func(i, j int) bool {
				return ranked[i].num*ranked[j].den > ranked[j].num*ranked[i].den
			})
		}
		count := int32(len(ranked))
		for index, limit := range ranked {
			rank := int32(index + 1)
			// At rank r, the share is bounded by r/count and this child's limit.
			if rank*limit.den >= limit.num*count {
				if (rank-1)*limit.den < limit.num*count {
					limits[node] = limit
				} else {
					limits[node] = fraction{rank - 1, count}
				}
				break
			}
		}
	}
	return limits[0]
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	number := func() int32 {
		input.Scan()
		value, _ := strconv.ParseInt(input.Text(), 10, coordinateBits)
		return int32(value)
	}
	n, deadline := number(), number()
	head := make([]int32, n)
	sibling := make([]int32, n)
	days := make([]int32, n)
	for node := int32(1); node < n; node++ {
		parent := number() - 1
		days[node] = number()
		sibling[node] = head[parent]
		head[parent] = node
	}
	share := maximumShare(head, sibling, days, deadline)
	den := int64(share.den)
	value := (int64(share.num)*percent*outputScale + den/2) / den
	answer := strconv.FormatInt(value/outputScale, 10)
	decimals := strconv.FormatInt(value%outputScale+outputScale, 10)
	os.Stdout.WriteString(answer + "." + decimals[1:precision+1] + "\n")
}
