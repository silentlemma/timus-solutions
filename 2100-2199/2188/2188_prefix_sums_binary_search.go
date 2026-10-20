package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

type scanner struct {
	data []byte
	pos  int
}

func (s *scanner) nextInt() int64 {
	for s.data[s.pos] <= ' ' {
		s.pos++
	}
	var value int64
	for s.pos < len(s.data) && s.data[s.pos] >= '0' && s.data[s.pos] <= '9' {
		value = value*10 + int64(s.data[s.pos]-'0')
		s.pos++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n, q := int(in.nextInt()), int(in.nextInt())
	prefix := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		prefix[i] = in.nextInt()
	}
	for i := 1; i <= n; i++ {
		prefix[i] += prefix[i-1] - in.nextInt()
	}

	suffix := make([]int64, n+1)
	suffix[n] = prefix[n]
	for i := n - 1; i > 0; i-- {
		suffix[i] = suffix[i+1]
		if prefix[i] < suffix[i] {
			suffix[i] = prefix[i]
		}
	}

	thresholds := make([]int64, 0, n)
	times := make([]int, 0, n)
	var previousMaximum int64
	for i := 1; i <= n; i++ {
		// Slowing down before this second costs the previous excess over the query.
		if suffix[i] > previousMaximum {
			thresholds = append(thresholds, suffix[i])
			times = append(times, i)
		}
		if prefix[i] > previousMaximum {
			previousMaximum = prefix[i]
		}
	}

	output := make([]byte, 0)
	for i := 0; i < q; i++ {
		distance := in.nextInt()
		left, right := 0, len(thresholds)
		for left < right {
			middle := left + (right-left)/2
			if thresholds[middle] <= distance {
				left = middle + 1
			} else {
				right = middle
			}
		}
		answer := -1
		if left < len(times) {
			answer = times[left]
		}
		output = strconv.AppendInt(output, int64(answer), 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
