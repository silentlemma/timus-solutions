package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	shift       = 300
	columns     = 450
	significant = 19
	decimal     = 10
	roundUp     = 5
)

func add(sums *[columns]int, token []byte) {
	end, point := len(token), len(token)
	for i, ch := range token {
		if ch == '.' {
			point = i
		}
		if ch == 'e' || ch == 'E' {
			end = i
			break
		}
	}
	if point > end {
		point = end
	}
	exponent := 0
	if end < len(token) {
		exponent, _ = strconv.Atoi(string(token[end+1:]))
	}
	start, sign := 0, 1
	if token[0] == '-' {
		sign = -1
	}
	if token[0] == '+' || token[0] == '-' {
		start++
	}
	column := shift + exponent + point - start - 1
	for _, ch := range token[start:end] {
		if ch != '.' {
			sums[column] += sign * int(ch-'0')
			column--
		}
	}
}

func settle(sums *[columns]int) int {
	carry := 0
	for i, value := range sums {
		value += carry
		digit := value % decimal
		if digit < 0 {
			digit += decimal
		}
		sums[i], carry = digit, (value-digit)/decimal
	}
	return carry
}

func format(sums *[columns]int) []byte {
	negative := settle(sums) < 0
	if negative {
		for i := range sums {
			sums[i] = -sums[i]
		}
		settle(sums)
	}
	top := 0
	for i := range sums {
		if sums[i] != 0 {
			top = i
		}
	}
	if sums[top] == 0 {
		return []byte("0.000000000000000000e0\n")
	}
	var kept [significant + 1]byte
	for i := 0; i < significant && i <= top; i++ {
		kept[i+1] = byte(sums[top-i])
	}
	if top >= significant && sums[top-significant] >= roundUp {
		// The extra digit takes a carry out of the mantissa.
		for i := significant; ; i-- {
			kept[i]++
			if kept[i] < decimal {
				break
			}
			kept[i] = 0
		}
	}
	start := 1
	exponent := top - shift
	if kept[0] != 0 {
		start--
		exponent++
	}
	var buffer [significant + significant]byte
	output := buffer[:0]
	if negative {
		output = append(output, '-')
	}
	output = append(output, '0'+kept[start], '.')
	for _, digit := range kept[start+1 : start+significant] {
		output = append(output, '0'+digit)
	}
	output = strconv.AppendInt(append(output, 'e'), int64(exponent), decimal)
	return append(output, '\n')
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	var sums [columns]int
	for i := 0; i < count && input.Scan(); i++ {
		add(&sums, input.Bytes())
	}
	os.Stdout.Write(format(&sums))
}
