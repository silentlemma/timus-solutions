package main

import (
	"bufio"
	"os"
	"strconv"
)

const modulus = 2007
const residueDigits = 4

func inverse(x int) int {
	a, b, u, v := x, modulus, 1, 0
	for b != 0 {
		q := a / b
		a, b = b, a-q*b
		u, v = v, u-q*v
	}
	return (u%modulus + modulus) % modulus
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	in.Scan()
	n, _ := strconv.Atoi(in.Text())
	f := make([]uint16, n+1)
	for i := 1; i <= n; i++ {
		in.Scan()
		value, _ := strconv.Atoi(in.Text())
		f[i] = uint16((value%modulus + modulus) % modulus)
	}
	first := inverse(int(f[1]))
	acc := make([]uint16, n+1)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var digits [residueDigits]byte
	for d := 1; d <= n; d++ {
		g := first
		if d > 1 {
			g = (modulus - first*int(acc[d])%modulus) % modulus
			out.WriteByte(' ')
		}
		out.Write(strconv.AppendInt(digits[:0], int64(g), 10))
		// A zero coefficient contributes nothing to any later multiple.
		if g != 0 {
			for k, multiple := 2, d+d; multiple <= n; k, multiple = k+1, multiple+d {
				acc[multiple] = uint16((int(acc[multiple]) + int(f[k])*g) % modulus)
			}
		}
	}
	out.WriteByte('\n')
}
