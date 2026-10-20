package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
)

type query struct {
	u, v, cut, index int
}

type fraction struct {
	numerator, denominator int64
}

func (value fraction) text() string {
	result := strconv.FormatInt(value.numerator/value.denominator, 10)
	remainder := value.numerator % value.denominator
	if remainder == 0 {
		return result
	}
	digits := []byte(result)
	digits = append(digits, '.')
	for remainder != 0 {
		remainder *= 10
		digits = append(digits, byte('0'+remainder/value.denominator))
		remainder %= value.denominator
	}
	return string(digits)
}

func solve(next []int, length, cut int) fraction {
	best := fraction{0, 1}
	denominator := int64(1)
	position := cut
	remaining := int64(length - cut)
	for {
		position = next[position]
		numerator := int64(position - cut)
		if numerator*best.denominator > best.numerator*denominator {
			best = fraction{numerator, denominator}
		}
		if position == length {
			break
		}
		position++
		denominator *= 2
		// An answer is at least 1/2, so at most 18 mismatches need consideration.
		// Even the whole remaining word cannot improve the current answer.
		if remaining*best.denominator <= best.numerator*denominator {
			break
		}
	}
	return best
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	token := func() []byte {
		for position < len(data) && data[position] <= ' ' {
			position++
		}
		start := position
		for position < len(data) && data[position] > ' ' {
			position++
		}
		return data[start:position]
	}
	integer := func() int {
		result := 0
		for _, digit := range token() {
			result = result*10 + int(digit-'0')
		}
		return result
	}
	count, queryCount := integer(), integer()
	words := make([][]byte, count)
	maximumLength := 0
	for i := range words {
		words[i] = token()
		word := words[i]
		for left, right := 0, len(word)-1; left < right; left, right = left+1, right-1 {
			word[left], word[right] = word[right], word[left]
		}
		if len(word) > maximumLength {
			maximumLength = len(word)
		}
	}
	queries := make([]query, queryCount)
	for i := range queries {
		u, v, cut := integer()-1, integer()-1, integer()
		if u > v {
			u, v = v, u
		}
		queries[i] = query{u, v, cut, i}
	}
	sort.Slice(queries, func(i, j int) bool {
		if queries[i].u != queries[j].u {
			return queries[i].u < queries[j].u
		}
		return queries[i].v < queries[j].v
	})
	answers := make([]fraction, queryCount)
	next := make([]int, maximumLength+1)
	for begin := 0; begin < queryCount; {
		end := begin + 1
		u, v := queries[begin].u, queries[begin].v
		for end < queryCount && queries[end].u == u && queries[end].v == v {
			end++
		}
		length := len(words[u])
		if len(words[v]) < length {
			length = len(words[v])
		}
		if u != v {
			// Reuse one mismatch table for every query of this word pair.
			next[length] = length
			for i := length - 1; i >= 0; i-- {
				next[i] = next[i+1]
				if words[u][i] != words[v][i] {
					next[i] = i
				}
			}
		}
		for _, current := range queries[begin:end] {
			if u == v {
				answers[current.index] = fraction{int64(length - current.cut), 1}
			} else {
				answers[current.index] = solve(next, length, current.cut)
			}
		}
		begin = end
	}
	output := bufio.NewWriter(os.Stdout)
	for _, answer := range answers {
		output.WriteString(answer.text())
		output.WriteByte('\n')
	}
	output.Flush()
}
