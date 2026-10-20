package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const maxValue = 100000
const baseSize = 16

type solver struct {
	values, limit, minimum, maximum, frequency []int
}

func smaller(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func larger(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func (s *solver) mixed(left, middle, right, sign int) int64 {
	low, high, offset := s.minimum, s.maximum, 0
	if sign == -1 {
		low, high, offset = s.maximum, s.minimum, maxValue
	}
	lower, upper, threshold, current := middle, middle-1, middle-1, middle
	var answer int64
	for i := middle - 1; i >= left; i-- {
		for lower < right && sign*low[lower] >= sign*low[i] {
			lower++
		}
		for threshold+1 < right && sign*high[threshold+1] < sign*high[i] {
			threshold++
		}
		target := smaller(threshold, s.limit[i])
		for upper < target {
			upper++
			if upper >= current {
				s.frequency[sign*low[upper]+upper+offset]++
			}
		}
		for upper > target {
			if upper >= current {
				s.frequency[sign*low[upper]+upper+offset]--
			}
			upper--
		}
		for current < lower {
			if current <= upper {
				s.frequency[sign*low[current]+current+offset]--
			}
			current++
		}
		answer += int64(s.frequency[sign*high[i]+i+offset])
	}
	for j := middle; j < right; j++ {
		s.frequency[sign*low[j]+j+offset] = 0
	}
	return answer
}

func (s *solver) count(left, right int) int64 {
	var answer int64
	if right-left <= baseSize {
		for i := left; i < right; i++ {
			low, high := s.values[i], s.values[i]
			for j := i; j < right && j <= s.limit[i]; j++ {
				low = smaller(low, s.values[j])
				high = larger(high, s.values[j])
				if high-low == j-i {
					answer++
				}
			}
		}
		return answer
	}
	middle := left + (right-left)/2
	answer = s.count(left, middle) + s.count(middle, right)
	for left < middle && s.limit[left] < middle {
		left++
	}
	right = smaller(right, s.limit[middle-1]+1)
	if left == middle || right == middle {
		return answer
	}
	s.minimum[middle-1], s.maximum[middle-1] = s.values[middle-1], s.values[middle-1]
	for i := middle - 2; i >= left; i-- {
		s.minimum[i] = smaller(s.minimum[i+1], s.values[i])
		s.maximum[i] = larger(s.maximum[i+1], s.values[i])
	}
	s.minimum[middle], s.maximum[middle] = s.values[middle], s.values[middle]
	for j := middle + 1; j < right; j++ {
		s.minimum[j] = smaller(s.minimum[j-1], s.values[j])
		s.maximum[j] = larger(s.maximum[j-1], s.values[j])
	}
	// Extrema in one half determine the opposite endpoint.
	for i := left; i < middle; i++ {
		j := i + s.maximum[i] - s.minimum[i]
		if j >= middle && j < right && j <= s.limit[i] &&
			s.maximum[j] < s.maximum[i] && s.minimum[j] > s.minimum[i] {
			answer++
		}
	}
	for j := middle; j < right; j++ {
		i := j - s.maximum[j] + s.minimum[j]
		if i >= left && i < middle && j <= s.limit[i] &&
			s.maximum[i] < s.maximum[j] && s.minimum[i] > s.minimum[j] {
			answer++
		}
	}
	return answer + s.mixed(left, middle, right, 1) + s.mixed(left, middle, right, -1)
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	readInt := func() int {
		for position < len(data) && (data[position] < '0' || data[position] > '9') {
			position++
		}
		value := 0
		for position < len(data) && data[position] >= '0' && data[position] <= '9' {
			value = value*10 + int(data[position]-'0')
			position++
		}
		return value
	}
	n := readInt()
	s := solver{
		values: make([]int, n), limit: make([]int, n),
		minimum: make([]int, n), maximum: make([]int, n),
		frequency: make([]int, maxValue+n+1),
	}
	for i := range s.values {
		s.values[i] = readInt()
	}
	next := make([]int, maxValue+1)
	for i := range next {
		next[i] = n
	}
	end := n - 1
	for i := n - 1; i >= 0; i-- {
		end = smaller(end, next[s.values[i]]-1)
		s.limit[i] = end
		next[s.values[i]] = i
	}
	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(output, s.count(0, n))
	output.Flush()
}
