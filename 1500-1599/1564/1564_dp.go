package main

import "syscall"

const (
	decimal       = 10
	places        = 18
	inputCapacity = 64
)

func floorFor(target int64) (int64, bool) {
	var floor, prefixOnes int64
	var width int64 = 1
	for i := 1; i < places; i++ {
		width *= decimal
	}
	for remaining := int64(places - 1); remaining >= 0; remaining-- {
		// Count ones over all completions of each potential next digit.
		fixedCost := prefixOnes*width + remaining*(width/decimal)
		digit := int64(0)
		if target > fixedCost {
			target -= fixedCost // Skip the block prefixed by digit 0.
			if target <= fixedCost+width {
				digit = 1
				prefixOnes++
			} else {
				target -= fixedCost + width
				// Digits 2 through 9 have equal block sizes.
				digit = 2 + (target-1)/fixedCost
				target = (target-1)%fixedCost + 1
			}
		}
		floor = decimal*floor + digit
		width /= decimal
	}
	return floor, target == prefixOnes
}

func readTarget() int64 {
	var input [inputCapacity]byte
	var target int64
	reading := false
	for {
		n, err := syscall.Read(syscall.Stdin, input[:])
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return target
		}
		for _, ch := range input[:n] {
			if ch >= '0' && ch <= '9' {
				target = target*decimal + int64(ch-'0')
				reading = true
			} else if reading {
				return target
			}
		}
	}
}

func write(data []byte) {
	for len(data) > 0 {
		n, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		data = data[n:]
	}
}

func main() {
	floor, ok := floorFor(readTarget())
	if !ok {
		write([]byte("Petr lies\n"))
		return
	}
	var output [places + 1]byte
	start := len(output) - 1
	output[start] = '\n'
	for {
		start--
		output[start] = '0' + byte(floor%decimal)
		floor /= decimal
		if floor == 0 {
			break
		}
	}
	write(output[start:])
}
