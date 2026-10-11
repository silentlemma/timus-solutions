package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	top   = 1000000 // 10000.00 in cents
	cents = 100
)

// toCents reads a price with at most two decimals
func toCents(s string) int {
	whole, frac := s, ""
	if dot := strings.IndexByte(s, '.'); dot >= 0 {
		whole, frac = s[:dot], s[dot+1:]
	}
	w, _ := strconv.Atoi("0" + whole)
	f, _ := strconv.Atoi((frac + "00")[:2])
	return w*cents + f
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() string {
		in.Scan()
		return in.Text()
	}
	// bids counted by price, indexed from the highest price down, so that
	// "at least X" is a Fenwick prefix sum
	tree := make([]int, top+1)
	var sold int64
	for kind := next(); kind != "QUIT" && kind != ""; kind = next() {
		r := top + 1 - toCents(next())
		if kind == "SALE" {
			k, _ := strconv.ParseInt(next(), 10, 0)
			count := int64(0)
			for ; r > 0; r &= r - 1 {
				count += int64(tree[r])
			}
			if count < k {
				k = count
			}
			sold += k
		} else {
			step := 1
			if kind == "DEL" {
				step = -1
			}
			for ; r <= top; r += r & -r {
				tree[r] += step
			}
		}
	}
	// the exchange earns one cent per piece sold
	fmt.Printf("%d.%02d\n", sold/cents, sold%cents)
}
