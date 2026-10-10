package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	cents = 100
	bits  = 64
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var k int64
	fmt.Fscan(in, &n, &k)
	// lengths have exactly two decimals, so in centimetres they are exact
	cables := make([]int64, n)
	var high int64
	for i := range cables {
		var s string
		fmt.Fscan(in, &s)
		cables[i], _ = strconv.ParseInt(strings.Replace(s, ".", "", 1), 10, bits)
		if cables[i] > high {
			high = cables[i]
		}
	}
	// more pieces come out of shorter ones, so the longest length that still
	// gives k pieces is found by binary search; 0 means even 1 cm is too long
	low := int64(0)
	for low < high {
		mid := (low + high + 1) / 2
		var pieces int64
		for _, c := range cables {
			pieces += c / mid
		}
		if pieces >= k {
			low = mid
		} else {
			high = mid - 1
		}
	}
	fmt.Printf("%d.%02d\n", low/cents, low%cents)
}
