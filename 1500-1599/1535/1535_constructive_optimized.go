package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

const outputSize = 8192
const numberReserve = 16

var output = make([]byte, 0, outputSize)
var first = true

func flush() {
	remaining := output
	for len(remaining) > 0 {
		count, err := os.Stdout.Write(remaining)
		remaining = remaining[count:]
		if err != nil || count == 0 {
			break
		}
	}
	output = output[:0]
}

func number(value int) {
	if len(output)+numberReserve >= cap(output) {
		flush()
	}
	if !first {
		output = append(output, ' ')
	}
	first = false
	output = strconv.AppendInt(output, int64(value), 10)
}

func line() {
	output = append(output, '\n')
	first = true
}

func main() {
	input, _ := ioutil.ReadAll(os.Stdin)
	n := 0
	for _, c := range input {
		if c >= '0' && c <= '9' {
			n = n*10 + int(c-'0')
		}
	}
	number(1)
	number(n)
	const pairPeriod = 4
	pairs := (n - 1) / 2
	// Each arm entry is determined by its index; there is no visited array.
	for k := 1; k <= pairs; k++ {
		if k%2 == 1 {
			number(k + 1)
		} else {
			number(n - k)
		}
	}
	if n%2 == 0 && n > 2 {
		number(2*(n/pairPeriod) + 1)
	}
	for k := pairs; k >= 2; k-- {
		if k%2 == 1 {
			number(k)
		} else {
			number(n - k + 1)
		}
	}
	line()
	for value := 1; value <= n; value += 2 {
		number(value)
	}
	for value := n - n%2; value >= 2; value -= 2 {
		number(value)
	}
	line()
	flush()
}
