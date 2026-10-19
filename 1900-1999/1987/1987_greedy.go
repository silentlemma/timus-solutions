package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func locate(left, right, queries []int) []int {
	stack := make([]int, 0, len(left))
	answers := make([]int, 0, len(queries))
	index := 0
	for _, point := range queries {
		for index < len(left) && left[index] <= point {
			for len(stack) > 0 && right[stack[len(stack)-1]] < left[index] {
				stack = stack[:len(stack)-1]
			}
			stack = append(stack, index)
			index++
		}
		for len(stack) > 0 && right[stack[len(stack)-1]] < point {
			stack = stack[:len(stack)-1]
		}
		answer := -1
		if len(stack) > 0 {
			answer = stack[len(stack)-1] + 1
		}
		answers = append(answers, answer)
	}
	return answers
}

type scanner struct {
	data []byte
	at   int
}

func (s *scanner) next() int {
	for s.at < len(s.data) && s.data[s.at] <= ' ' {
		s.at++
	}
	value := 0
	for s.at < len(s.data) && s.data[s.at] > ' ' {
		value = value*10 + int(s.data[s.at]-'0')
		s.at++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n := in.next()
	left, right := make([]int, n), make([]int, n)
	for i := range left {
		left[i] = in.next()
		right[i] = in.next()
	}
	m := in.next()
	queries := make([]int, m)
	for i := range queries {
		queries[i] = in.next()
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, answer := range locate(left, right, queries) {
		fmt.Fprintln(out, answer)
	}
}
