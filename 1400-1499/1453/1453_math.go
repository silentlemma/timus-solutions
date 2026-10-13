package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const base = 1000000000 // a long number in decimal limbs of nine digits

// number * factor + add, on limbs from the lowest
func mulAdd(number []int64, factor, add int64) []int64 {
	carry := add
	for i := range number {
		v := number[i]*factor + carry
		number[i], carry = v%base, v/base
	}
	for carry > 0 {
		number = append(number, carry%base)
		carry /= base
	}
	return number
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, s int
	fmt.Fscan(reader, &n, &s)
	c := make([]int, n)
	for i := range c {
		fmt.Fscan(reader, &c[i])
	}
	rook := int64(n) * int64(s-1)
	if n == 1 { // in one dimension a bishop moves exactly like a rook
		fmt.Println(rook)
		return
	}
	// t bishop steps need room t on the chosen side of every coordinate
	both := make([]int, s) // both[m]: coordinates with room m on each side
	reach := s             // beyond this some coordinate has no room
	for _, x := range c {
		lo, hi := s-x, x-1
		if lo > hi {
			lo, hi = hi, lo
		}
		both[lo]++
		if hi < reach {
			reach = hi
		}
	}
	count := make([]int64, n+1) // count[k]: lengths t with 2^k directions
	k := n - both[0]
	for t := 1; t <= reach; t++ {
		count[k]++
		k -= both[t]
	}
	ways := []int64{0} // the sum of count[k] 2^k, doubling from the top
	for j := n; j >= 0; j-- {
		ways = mulAdd(ways, 2, count[j])
	}
	ways = mulAdd(ways, 1, rook)
	var sb strings.Builder
	sb.WriteString(fmt.Sprint(ways[len(ways)-1]))
	for i := len(ways) - 2; i >= 0; i-- {
		sb.WriteString(fmt.Sprintf("%09d", ways[i]))
	}
	fmt.Println(sb.String())
}
