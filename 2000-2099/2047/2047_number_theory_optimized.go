package main

import "syscall"

func readInput(buffer []byte) int {
	for {
		count, err := syscall.Read(syscall.Stdin, buffer)
		if count > 0 {
			return count
		}
		if err != syscall.EINTR {
			return 0
		}
	}
}

func writeAll(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			return
		}
	}
}

const inputSize = 8192

var input [inputSize]byte
var position, length int

func nextByte() byte {
	if position == length {
		length = readInput(input[:])
		position = 0
		if length == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

const outputSize = 8192

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	used += copy(output[used:], digits[first:])
}

const maxTerm = 300
const blockSize = 1 << 16
const ringSize = maxTerm + 1
const termWidth = 4

var remaining [blockSize]uint32

func primesUpTo(bound int) []uint16 {
	composite := make([]bool, bound+1)
	var primes []uint16
	for p := 2; p <= bound; p++ {
		if !composite[p] {
			primes = append(primes, uint16(p))
			for multiple := p * p; multiple <= bound; multiple += p {
				composite[multiple] = true
			}
		}
	}
	return primes
}

func divisorBlock(left, right int, primes []uint16) []uint16 {
	counts := make([]uint16, right-left+1)
	for i := range counts {
		remaining[i] = uint32(left + i)
		counts[i] = 1
	}
	for _, small := range primes {
		p := int(small)
		if p*p > right {
			break
		}
		for offset := (p - left%p) % p; offset < len(counts); offset += p {
			exponent := uint16(0)
			for remaining[offset]%uint32(p) == 0 {
				remaining[offset] /= uint32(p)
				exponent++
			}
			counts[offset] *= exponent + 1
		}
	}
	for i, value := range remaining[:len(counts)] {
		if value > 1 {
			counts[i] *= 2
		}
	}
	return counts
}

func solve(n int) []uint16 {
	limit, root := maxTerm*n, 1
	for (root+1)*(root+1) <= limit {
		root++
	}
	primes := primesUpTo(root)
	var history [][]uint16
	var depth [ringSize]uint32
	for left := 1; left <= limit; left += blockSize {
		right := left + blockSize - 1
		if right > limit {
			right = limit
		}
		counts := divisorBlock(left, right, primes)
		history = append(history, counts)
		for offset, raw := range counts {
			total, term := left+offset, int(raw)
			current := uint32(0)
			if total <= maxTerm {
				current = 1
			}
			if term <= maxTerm && total > term {
				previous := depth[(total-term)%ringSize]
				if previous > 0 && previous+1 > current {
					current = previous + 1
				}
			}
			depth[total%ringSize] = current
			if current >= uint32(n) {
				answer := make([]uint16, n)
				for i := n - 1; i > 0; i-- {
					index := total - 1
					answer[i] = history[index/blockSize][index%blockSize]
					total -= int(answer[i])
				}
				answer[0] = uint16(total)
				return answer
			}
		}
	}
	return nil
}

func main() {
	answer := solve(number())
	if answer == nil {
		writeAll([]byte("Impossible\n"))
		return
	}
	for i, value := range answer {
		if len(output)-used < termWidth {
			writeAll(output[:used])
			used = 0
		}
		writeNumber(int(value))
		if i+1 == len(answer) {
			output[used] = '\n'
		} else {
			output[used] = ' '
		}
		used++
	}
	writeAll(output[:used])
}
