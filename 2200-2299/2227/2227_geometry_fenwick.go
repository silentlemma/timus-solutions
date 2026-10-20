package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const bufferSize = 1 << 16

type Scanner struct {
	data []byte
	pos  int
}

func (s *Scanner) token() byte {
	for s.data[s.pos] <= ' ' {
		s.pos++
	}
	value := s.data[s.pos]
	s.pos++
	return value
}

func (s *Scanner) integer() int64 {
	for s.data[s.pos] <= ' ' {
		s.pos++
	}
	sign := int64(1)
	if s.data[s.pos] == '-' {
		sign = -1
		s.pos++
	}
	value := int64(0)
	for s.data[s.pos] >= '0' && s.data[s.pos] <= '9' {
		value = value*10 + int64(s.data[s.pos]-'0')
		s.pos++
	}
	return value * sign
}

func sum(tree []int64, end int) int64 {
	result := int64(0)
	for end > 0 {
		result += tree[end]
		end -= end & -end
	}
	return result
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	scan := Scanner{data: append(data, ' ')}
	n, q := int(scan.integer()), int(scan.integer())
	x, y := make([]int64, n), make([]int64, n)
	for i := range x {
		x[i], y[i] = scan.integer(), scan.integer()
	}
	cross := func(a, b int) int64 { return x[a]*y[b] - y[a]*x[b] }
	prefix, removed := make([]int64, n+1), make([]int64, n+1)
	for i := range x {
		prefix[i+1] = prefix[i] + cross(i, (i+1)%n)
	}
	total := prefix[n]
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer out.Flush()
	for ; q > 0; q-- {
		kind := scan.token()
		left, right := int(scan.integer())-1, int(scan.integer())-1
		if left > right {
			left, right = right, left
		}
		part := prefix[right] - prefix[left] + cross(right, left)
		part -= sum(removed, right) - sum(removed, left)
		other := total - part
		answer := part
		if other > answer {
			answer = other
		}
		if kind == 'c' {
			edge := right
			answer = other
			if part < other {
				edge, answer = left, part
			}
			// Charge the discarded area to the first edge of its original arc.
			for i := edge + 1; i <= n; i += i & -i {
				removed[i] += answer
			}
			total -= answer
		}
		if answer%2 == 0 {
			fmt.Fprintf(out, "%d.0\n", answer/2)
		} else {
			fmt.Fprintf(out, "%d.5\n", answer/2)
		}
	}
}
