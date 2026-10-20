package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	at := 0
	read := func() int64 {
		for at < len(data) && data[at] <= ' ' {
			at++
		}
		var value int64
		for at < len(data) && data[at] >= '0' && data[at] <= '9' {
			value = value*10 + int64(data[at]-'0')
			at++
		}
		return value
	}
	n, days, length, moves := int(read()), int(read()), int(read()), int(read())
	positions := n - length + 1
	dp := [][]int64{make([]int64, positions)}
	prefix := make([]int64, n+1)
	weight := make([]int64, positions)
	key := make([]int64, positions)
	queue := make([]int, positions)
	previousLow := 0
	for day := 1; day <= days; day++ {
		for j := 0; j < n; j++ {
			prefix[j+1] = prefix[j] + read()
		}
		for x := 0; x < positions; x++ {
			weight[x] = prefix[x+length] - prefix[x]
		}
		low := moves - (days - day)
		if low < 0 {
			low = 0
		}
		high := moves
		if day < high {
			high = day
		}
		next := make([][]int64, high-low+1)
		for used := low; used <= high; used++ {
			current := make([]int64, positions)
			next[used-low] = current
			if used < day {
				stay := dp[used-previousLow]
				for x := range current {
					current[x] = stay[x] + weight[x]
				}
			}
			if used == 0 {
				continue
			}
			previous := dp[used-1-previousLow]
			for x := range key {
				key[x] = previous[x] - prefix[x]
			}
			head, tail := 0, 0
			var best int64
			for y := 0; y < positions; y++ {
				if y >= length {
					x := y - length
					candidate := previous[x] + weight[x]
					if candidate > best {
						best = candidate
					}
				}
				for head < tail && key[queue[tail-1]] <= key[y] {
					tail--
				}
				queue[tail] = y
				tail++
				if queue[head] <= y-length {
					head++
				}
				candidate := key[queue[head]] + prefix[y+length]
				if disjoint := best + weight[y]; disjoint > candidate {
					candidate = disjoint
				}
				if candidate > current[y] {
					current[y] = candidate
				}
			}
			for x := range key {
				key[x] = previous[x] + prefix[x+length]
			}
			head, tail = 0, 0
			best = 0
			for y := positions - 1; y >= 0; y-- {
				if y+length < positions {
					x := y + length
					candidate := previous[x] + weight[x]
					if candidate > best {
						best = candidate
					}
				}
				for head < tail && key[queue[tail-1]] <= key[y] {
					tail--
				}
				queue[tail] = y
				tail++
				if queue[head] >= y+length {
					head++
				}
				candidate := key[queue[head]] - prefix[y]
				if disjoint := best + weight[y]; disjoint > candidate {
					candidate = disjoint
				}
				if candidate > current[y] {
					current[y] = candidate
				}
			}
		}
		dp = next
		previousLow = low
	}
	var answer int64
	for _, value := range dp[0] {
		if value > answer {
			answer = value
		}
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, answer)
	out.Flush()
}
