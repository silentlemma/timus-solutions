package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
	"strings"
)

const (
	digits = 12
	bits64 = 64
)

var bases = []uint64{2, 3, 5, 7, 11, 13} // enough for every number below 3 * 10^12

func mulmod(a, b, n uint64) uint64 {
	hi, lo := bits.Mul64(a, b)
	return bits.Rem64(hi, lo, n)
}

func powmod(a, e, n uint64) uint64 {
	r := uint64(1)
	for a %= n; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = mulmod(r, a, n)
		}
		a = mulmod(a, a, n)
	}
	return r
}

// Miller-Rabin with fixed bases, exact for all 12-digit numbers
func isPrime(n uint64) bool {
	if n < 2 {
		return false
	}
	for _, p := range bases {
		if n%p == 0 {
			return n == p
		}
	}
	d, s := n-1, 0
	for d%2 == 0 {
		d /= 2
		s++
	}
	for _, a := range bases {
		x := powmod(a, d, n)
		witness := x != 1 && x != n-1
		for i := 1; i < s && witness; i++ {
			x = mulmod(x, x, n)
			witness = x != n-1
		}
		if witness {
			return false
		}
	}
	return true
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	sc.Scan()
	count, _ := strconv.Atoi(sc.Text())
	var all strings.Builder
	for sc.Scan() {
		all.WriteString(sc.Text()) // the digits, together or apart
	}
	prefix := all.String()
	if len(prefix) > count {
		prefix = prefix[:count]
	}
	number := uint64(0)
	if prefix != "" {
		number, _ = strconv.ParseUint(prefix, 10, bits64)
	}
	for i := count; i < digits; i++ {
		number *= 10
	}
	if count < digits {
		for !isPrime(number) {
			number++
		}
	}
	fmt.Printf("%0*d\n", digits, number)
}
