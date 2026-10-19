package main

import (
	"bufio"
	"bytes"
	"io/ioutil"
	"os"
	"strconv"
)

func solve(word []byte) []byte {
	n := len(word)
	infinity := int32(n + 1)
	data := make([]byte, n+1)
	copy(data[1:], word)
	length, link := make([]int32, n+2), make([]int32, n+2)
	difference, series := make([]int32, n+2), make([]int32, n+2)
	cacheOdd, cacheEven := make([]int32, n+2), make([]int32, n+2)
	odd, even := make([]int32, n+1), make([]int32, n+1)
	for i := range cacheOdd {
		cacheOdd[i], cacheEven[i] = infinity, infinity
	}
	for i := range odd {
		odd[i], even[i] = infinity, infinity
	}
	first, next, label := make([]int32, n+2), make([]int32, n+2), make([]int32, n+2)
	lookup := func(node, code int32) int32 {
		child := first[node]
		for child != 0 && label[child] != code {
			child = next[child]
		}
		return child
	}
	length[0], even[0] = -1, 0
	nodes, last := int32(2), int32(1)
	output := make([]byte, 0)
	for end := 1; end <= n; end++ {
		letter, node := data[end], last
		code := int32(letter - 'a')
		for data[end-int(length[node])-1] != letter {
			node = link[node]
		}
		found := lookup(node, code)
		if found == 0 {
			found = nodes
			nodes++
			length[found] = length[node] + 2
			suffix := int32(1)
			if length[found] != 1 {
				candidate := link[node]
				for data[end-int(length[candidate])-1] != letter {
					candidate = link[candidate]
				}
				suffix = lookup(candidate, code)
			}
			link[found] = suffix
			difference[found] = length[found] - length[suffix]
			series[found] = suffix
			if difference[found] == difference[suffix] {
				series[found] = series[suffix]
			}
			next[found] = first[node]
			first[node] = found
			label[found] = code
		}
		last = found
		for node = last; length[node] > 0; node = series[node] {
			suffix := link[node]
			before := end - int(length[series[node]]+difference[node])
			cacheOdd[node], cacheEven[node] = odd[before], even[before]
			if difference[node] == difference[suffix] {
				if cacheOdd[suffix] < cacheOdd[node] {
					cacheOdd[node] = cacheOdd[suffix]
				}
				if cacheEven[suffix] < cacheEven[node] {
					cacheEven[node] = cacheEven[suffix]
				}
			}
			if cacheEven[node]+1 < odd[end] {
				odd[end] = cacheEven[node] + 1
			}
			if cacheOdd[node]+1 < even[end] {
				even[end] = cacheOdd[node] + 1
			}
		}
		a, b := odd[end], even[end]
		if a == infinity {
			a = -1
		}
		if b == infinity {
			b = -2
		}
		output = strconv.AppendInt(output, int64(a), 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(b), 10)
		output = append(output, '\n')
	}
	return output
}

func main() {
	raw, _ := ioutil.ReadAll(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	output.Write(solve(bytes.TrimSpace(raw)))
	output.Flush()
}
