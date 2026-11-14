package main

import "syscall"

const (
	decimal              = 10
	offsetProductDivisor = 6
	inputSize            = 64
	outputSize           = 24
)

type input struct {
	data       [inputSize]byte
	start, end int
}

func (in *input) nextByte() byte {
	for in.start == in.end {
		n, err := syscall.Read(syscall.Stdin, in.data[:])
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return 0
		}
		in.start, in.end = 0, n
	}
	c := in.data[in.start]
	in.start++
	return c
}

func (in *input) number() int64 {
	c := in.nextByte()
	for c != 0 && c <= ' ' {
		c = in.nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = decimal*value + int64(c-'0')
		c = in.nextByte()
	}
	return value
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func pairs(n, page int64) int64 {
	last := n % page
	return (n/page*page*(page-1) + last*(last-1)) / 2
}

func answer(a, b, n int64) int64 {
	large, small := a, b
	if large < small {
		large, small = small, large
	}
	stride := large % small
	loss := int64(0)
	if stride != 0 {
		unit := gcd(large, small)
		count := small / unit
		period := large * count
		// Within a period, the nonzero cut offsets are unit, 2*unit, ...
		if period <= n {
			perPeriod := unit * unit * count * (count - 1) * (count + 1) / offsetProductDivisor
			loss = n / period * perPeriod
		}
		tail := n % period
		for cut, left := large, stride; cut < tail; cut, left = cut+large, left+stride {
			if left >= small {
				left -= small
			}
			right := small - left
			if remaining := tail - cut; remaining < right {
				right = remaining
			}
			loss += left * right
		}
	}
	return pairs(n, a) - pairs(n, small) + loss
}

func main() {
	var input input
	a, b, n := input.number(), input.number(), input.number()
	value := answer(a, b, n)
	var digits [outputSize]byte
	end := len(digits) - 1
	digits[end] = '\n'
	for {
		end--
		digits[end] = '0' + byte(value%decimal)
		value /= decimal
		if value == 0 {
			break
		}
	}
	output := digits[end:]
	for len(output) > 0 {
		size, err := syscall.Write(syscall.Stdout, output)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		output = output[size:]
	}
}
