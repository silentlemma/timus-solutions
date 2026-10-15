package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	bits     = 8 // bits of a character, the lowest first
	oneFreq  = 2 // a one is sin(2 pi k / t), a zero sin(4 pi k / t)
	zeroFreq = 4
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, t int
	fmt.Fscan(in, &n, &t)
	samples := make([]float64, n)
	for i := range samples {
		fmt.Fscan(in, &samples[i])
	}
	// over a whole number of periods sin(2 pi k / t) and sin(4 pi k / t) are
	// orthogonal to each other and to a constant, so the correlation of a bit's
	// samples with each wave picks the wave that was sent
	var got []int
	for start := 0; start < n; start += t {
		one, zero := 0.0, 0.0
		for k := 0; k < t; k++ {
			x := math.Pi * float64(k) / float64(t)
			one += samples[start+k] * math.Sin(oneFreq*x)
			zero += samples[start+k] * math.Sin(zeroFreq*x)
		}
		bit := 0
		if one > zero {
			bit = 1
		}
		got = append(got, bit)
	}
	text := make([]byte, 0, len(got)/bits)
	for start := 0; start < len(got); start += bits {
		c := 0
		for j := 0; j < bits; j++ {
			c |= got[start+j] << uint(j)
		}
		text = append(text, byte(c))
	}
	fmt.Println(string(text))
}
