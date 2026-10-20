package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n, k int
	fmt.Fscan(reader, &n, &k)
	s := make([]int, n)
	total, largest := 0, 0
	for i := range s {
		fmt.Fscan(reader, &s[i])
		total += s[i]
		if s[i] > largest {
			largest = s[i]
		}
	}
	// Every sponsor needs its own problems, and no problem holds more than k.
	m := (total + k - 1) / k
	if largest > m {
		m = largest
	}
	// Write the sponsors one after another and deal the copies round robin:
	// a sponsor's copies are consecutive and at most m, so they land in
	// different problems, and every problem gets at most ceil(total / m) <= k.
	problems := make([][]int, m)
	position := 0
	for i := 0; i < n; i++ {
		for c := 0; c < s[i]; c++ {
			problems[position%m] = append(problems[position%m], i+1)
			position++
		}
	}
	fmt.Fprintln(writer, m)
	for _, p := range problems {
		writer.WriteString(strconv.Itoa(len(p)))
		for _, x := range p {
			writer.WriteByte(' ')
			writer.WriteString(strconv.Itoa(x))
		}
		writer.WriteByte('\n')
	}
}
