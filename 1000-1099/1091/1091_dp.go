package main

import (
	"bufio"
	"os"
	"strconv"
)

const capacity = 10000
const maxS = 50
const decimalBase = 10

func count(k, s int) int {
	if k > s/2 {
		return 0
	}
	var choose, exact [maxS/2 + 1]int
	coefficient := 1
	choose[k] = coefficient
	for m := k + 1; m <= s/2; m++ {
		coefficient = coefficient * m / (m - k)
		if coefficient >= capacity {
			return capacity
		}
		choose[m] = coefficient
	}
	limit, total := s/k, 0
	for divisor := limit; divisor >= 2; divisor-- {
		value := choose[s/divisor]
		for multiple := 2 * divisor; multiple <= limit; multiple += divisor {
			value -= exact[multiple]
		}
		exact[divisor] = value
		total += value
		if total >= capacity {
			return capacity
		}
	}
	return total
}

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	k, s := number(in), number(in)
	os.Stdout.WriteString(strconv.Itoa(count(k, s)) + "\n")
}
