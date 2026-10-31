package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	// sieving this range gives 15000 primes, enough for every statement query.
	limit         = 163842
	primeCount    = 15000
	firstOddPrime = 3
	// refillable buffers bound memory independently of the input and output sizes.
	bufferSize = 4096
)

func main() {
	// index i represents 2*i+1, so even composite numbers need no storage.
	composite := make([]bool, limit/2)
	for p := firstOddPrime; p*p < limit; p += 2 {
		if !composite[p/2] {
			for i := p * p / 2; i < len(composite); i += p {
				composite[i] = true
			}
		}
	}
	// all computed primes are below limit, so uint32 halves their storage on x64.
	primes := make([]uint32, primeCount)
	primes[0] = 2
	count := 1
	for p := firstOddPrime; p < limit; p += 2 {
		if !composite[p/2] {
			primes[count] = uint32(p)
			count++
		}
	}
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer out.Flush()
	// decimal byte parsing avoids fmt's per-token reflection and temporary objects.
	readInt := func() int {
		c, err := in.ReadByte()
		for err == nil && c <= ' ' {
			c, err = in.ReadByte()
		}
		value := 0
		for err == nil && c >= '0' && c <= '9' {
			value = value*10 + int(c-'0')
			c, err = in.ReadByte()
		}
		return value
	}
	queries := readInt()
	for i := 0; i < queries; i++ {
		out.WriteString(strconv.Itoa(int(primes[readInt()-1])))
		out.WriteByte('\n')
	}
}
