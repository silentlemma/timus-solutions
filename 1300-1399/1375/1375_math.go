package main

import (
	"bufio"
	"os"
	"strconv"
)

const four uint64 = 4
const decimalBase = 10
const outputReserve = 32

func power(value, exponent, modulus uint64) uint64 {
	result := uint64(1)
	for exponent != 0 {
		if exponent&1 != 0 {
			result = result * value % modulus
		}
		value = value * value % modulus
		exponent /= 2
	}
	return result
}

func solve(key, p uint64) (uint64, uint64) {
	if p == 2 || key == 0 {
		return key, 0
	}
	if p%four == 1 {
		z := uint64(2)
		for power(z, (p-1)/2, p) != p-1 {
			z++
		}
		imaginary := power(z, (p-1)/four, p)
		odd := key
		if odd%2 == 0 {
			odd += p
		}
		return ((odd + 1) / 2) % p, ((odd - 1) / 2) * imaginary % p
	}
	for x := uint64(0); x <= p/2; x++ {
		residue := (key + p - x*x%p) % p
		y := power(residue, (p+1)/four, p)
		if y*y%p == residue {
			return x, y
		}
	}
	panic("prime modulus must have a sum-of-squares representation")
}

func number(in *bufio.Reader) uint64 {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := uint64(0)
	for c >= '0' && c <= '9' {
		value = value*decimalBase + uint64(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	key, p := number(in), number(in)
	x, y := solve(key, p)
	output := make([]byte, 0, outputReserve)
	output = strconv.AppendUint(output, x, decimalBase)
	output = append(output, ' ')
	output = strconv.AppendUint(output, y, decimalBase)
	output = append(output, '\n')
	os.Stdout.Write(output)
}
