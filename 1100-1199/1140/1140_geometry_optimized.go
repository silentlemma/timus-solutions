package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	outputSize = 32
	axes       = 3
)

func number(in *bufio.Scanner) int {
	in.Scan()
	value, _ := strconv.Atoi(in.Text())
	return value
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	n := number(in)
	var total [axes]int
	for i := 0; i < n; i++ {
		in.Scan()
		direction := in.Bytes()[0] - 'X'
		total[direction] += number(in)
	}
	a, b := total[0]+total[1], total[2]+total[1]
	lo, hi := a, b
	if lo > hi {
		lo, hi = hi, lo
	}
	// The median of a, 0 and b is zero clamped to the interval [lo, hi].
	m := 0
	if lo > 0 {
		m = lo
	} else if hi < 0 {
		m = hi
	}
	lengths := [axes]int{m - a, -m, m - b}
	var count byte
	var storage [outputSize]byte
	output := storage[:2]
	for direction, length := range lengths {
		if length == 0 {
			continue
		}
		count++
		output = append(output, 'X'+byte(direction), ' ')
		output = strconv.AppendInt(output, int64(length), 10)
		output = append(output, '\n')
	}
	output[0], output[1] = '0'+count, '\n'
	os.Stdout.Write(output)
}
