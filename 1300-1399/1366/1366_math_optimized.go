package main

import "syscall"

const (
	base        int64 = 1000000000
	limbDigits        = 9
	maxLimbs          = 334
	maxDigits         = 3001
	readSize          = 128
	decimalBase       = 10
	firstPair         = 4
)

func number() int {
	var block [readSize]byte
	value := 0
	started := false
	for {
		count, err := syscall.Read(syscall.Stdin, block[:])
		if count > 0 {
			for _, c := range block[:count] {
				if c >= '0' && c <= '9' {
					started = true
					value = value*decimalBase + int(c-'0')
				} else if started {
					return value
				}
			}
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return value
		}
	}
}

func writeOutput(output []byte) {
	for len(output) > 0 {
		count, err := syscall.Write(syscall.Stdout, output)
		if count > 0 {
			output = output[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
	}
}

func main() {
	n := number()
	var limbs [maxLimbs]uint32
	used := 1
	if n > 1 {
		limbs[0] = 1
	}
	scale := func(factor, offset int64) {
		carry := -offset
		for i := 0; i < used; i++ {
			value := int64(limbs[i])*factor + carry
			limbs[i] = uint32(value % base)
			carry = value / base
		}
		if carry != 0 {
			limbs[used] = uint32(carry)
			used++
		}
	}
	for k := firstPair; k <= n; k += 2 {
		scale(int64(k*(k-1)), int64(k-1))
	}
	if n > 1 && n%2 != 0 {
		scale(int64(n), 1)
	}

	// Write the least significant digits into the tail of the output buffer.
	var output [maxDigits]byte
	start := len(output) - 1
	output[start] = '\n'
	for _, limb := range limbs[:used-1] {
		for i := 0; i < limbDigits; i++ {
			start--
			output[start] = '0' + byte(limb%decimalBase)
			limb /= decimalBase
		}
	}
	for limb := limbs[used-1]; ; limb /= decimalBase {
		start--
		output[start] = '0' + byte(limb%decimalBase)
		if limb < decimalBase {
			break
		}
	}
	writeOutput(output[start:])
}
