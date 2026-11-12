package main

import (
	"bufio"
	"os"
	"strconv"
)

const limit = 32768
const bufferSize = 8192
const numberReserve = 16
const modFour uint32 = 4
const modEight uint32 = 8
const classThree uint32 = 3
const classFive uint32 = 5

func power(base, exponent, modulus uint32) uint32 {
	result := uint32(1)
	for ; exponent > 0; exponent, base = exponent>>1, base*base%modulus {
		if exponent&1 != 0 {
			result = result * base % modulus
		}
	}
	return result
}

func root(a, p uint32, cache *[limit]uint16) uint32 {
	if p == 2 {
		return 1
	}
	if p%modFour == classThree {
		r := power(a, (p+1)/modFour, p)
		if r*r%p == a {
			return r
		}
		return 0
	}
	if p%modEight == classFive {
		r := power(a, (p+classThree)/modEight, p)
		if r*r%p != a {
			if cache[p] == 0 {
				cache[p] = uint16(power(2, (p-1)/modFour, p))
			}
			r = r * uint32(cache[p]) % p
		}
		if r*r%p == a {
			return r
		}
		return 0
	}
	q, s := p-1, uint32(0)
	for q&1 == 0 {
		q >>= 1
		s++
	}
	// Initialize r²=a*t from a single modular exponentiation.
	b := power(a, (q-1)/2, p)
	r := a * b % p
	t := r * b % p
	c := uint32(0)
	for t != 1 {
		i, square := uint32(0), t
		for square != 1 && i < s {
			square = square * square % p
			i++
		}
		if i == s {
			return 0
		}
		if c == 0 {
			if cache[p] == 0 {
				z := uint32(2)
				for power(z, (p-1)/2, p) != p-1 {
					z++
				}
				cache[p] = uint16(power(z, q, p))
			}
			c = uint32(cache[p])
		}
		b = c
		for j := uint32(0); j < s-i-1; j++ {
			b = b * b % p
		}
		c = b * b % p
		r = r * b % p
		t = t * c % p
		s = i
	}
	return r
}

func number(in *bufio.Reader) uint32 {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := uint32(0)
	for c >= '0' && c <= '9' {
		value = value*10 + uint32(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	var cache [limit]uint16
	output := make([]byte, 0, bufferSize)
	for count := number(in); count > 0; count-- {
		a, p := number(in), number(in)
		r := root(a%p, p, &cache)
		if len(output)+numberReserve > cap(output) {
			os.Stdout.Write(output)
			output = output[:0]
		}
		if r == 0 {
			output = append(output, "No root\n"...)
			continue
		}
		if p == 2 {
			output = append(output, '1', '\n')
			continue
		}
		other := p - r
		if r > other {
			r, other = other, r
		}
		output = strconv.AppendUint(output, uint64(r), 10)
		output = append(output, ' ')
		output = strconv.AppendUint(output, uint64(other), 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
