package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const daySlots = 32
const hoursPerDay = 24
const minutesPerHour = 60

type reader struct {
	data []byte
	at   int
}

func (r *reader) number() int64 {
	for r.at < len(r.data) && (r.data[r.at] < '0' || r.data[r.at] > '9') &&
		r.data[r.at] != '-' && r.data[r.at] != '+' {
		r.at++
	}
	sign := int64(1)
	if r.data[r.at] == '-' {
		sign = -1
		r.at++
	} else if r.data[r.at] == '+' {
		r.at++
	}
	value := int64(0)
	for r.at < len(r.data) && r.data[r.at] >= '0' && r.data[r.at] <= '9' {
		value = value*10 + int64(r.data[r.at]-'0')
		r.at++
	}
	return sign * value
}

func solve(keys []int, amounts []int64) []int64 {
	n := len(keys)
	order, ranks := make([]int, n), make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool { return keys[order[i]] < keys[order[j]] })
	for rank, event := range order {
		ranks[event] = rank
	}
	size := 1
	for size < n {
		size <<= 1
	}
	sums, prefixes := make([]int64, 2*size), make([]int64, 2*size)
	result := make([]int64, 0, n)
	for i, amount := range amounts {
		index := size + ranks[i]
		sums[index] = amount
		if amount < 0 {
			prefixes[index] = amount
		}
		for index >>= 1; index > 0; index >>= 1 {
			left, right := index<<1, index<<1|1
			sums[index] = sums[left] + sums[right]
			best, cross := prefixes[left], sums[left]+prefixes[right]
			if cross < best {
				best = cross
			}
			prefixes[index] = best
		}
		result = append(result, prefixes[1])
	}
	return result
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := reader{data: data}
	n := int(in.number())
	keys, amounts := make([]int, n), make([]int64, n)
	for i := range keys {
		amounts[i] = in.number()
		day, month := int(in.number()), int(in.number())
		hour, minute := int(in.number()), int(in.number())
		keys[i] = ((month*daySlots+day)*hoursPerDay+hour)*minutesPerHour + minute
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, value := range solve(keys, amounts) {
		fmt.Fprintln(out, value)
	}
}
