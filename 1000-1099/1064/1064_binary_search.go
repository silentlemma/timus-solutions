package main

import "syscall"

const (
	maxLength   = 10000
	maxDepth    = 14
	decimal     = 10
	inputSize   = 64
	initialRuns = 16
	outputSize  = 192
	digitsInInt = 20
)

type search struct {
	target, steps int
	path          [maxDepth]bool
	runs          [][2]int
}

func (s *search) pivot(length, depth int) int {
	start, gaps := 0, length+1
	for _, right := range s.path[:depth-1] {
		left := gaps / 2
		if right {
			start += left
			gaps -= left
		} else {
			gaps = left
		}
	}
	return start + gaps/2 - 1
}

func (s *search) firstAtLeast(lo, hi, value, depth int) int {
	for lo < hi {
		mid := lo + (hi-lo)/2
		if s.pivot(mid, depth) < value {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func (s *search) visit(lo, hi, depth int) {
	if lo >= hi {
		return
	}
	// Along the same path the pivot is nondecreasing as the length grows.
	first := s.firstAtLeast(lo, hi, s.target, depth)
	after := s.firstAtLeast(first, hi, s.target+1, depth)
	if depth < s.steps {
		s.path[depth-1] = true
		s.visit(lo, first, depth+1)
		s.path[depth-1] = false
		s.visit(after, hi, depth+1)
		return
	}
	if first < after {
		last := len(s.runs) - 1
		if last >= 0 && s.runs[last][1]+1 == first {
			s.runs[last][1] = after - 1
		} else {
			s.runs = append(s.runs, [2]int{first, after - 1})
		}
	}
}

func main() {
	var input [inputSize]byte
	var values [2]int
	index, reading := 0, false
read:
	for {
		size, err := syscall.Read(syscall.Stdin, input[:])
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			break
		}
		for _, c := range input[:size] {
			if c >= '0' && c <= '9' {
				values[index] = values[index]*decimal + int(c-'0')
				reading = true
			} else if reading {
				index++
				if index == len(values) {
					break read
				}
				reading = false
			}
		}
		if err != nil {
			break
		}
	}
	var initial [initialRuns][2]int
	s := search{target: values[0], steps: values[1], runs: initial[:0]}
	if s.steps > 0 && s.steps <= maxDepth {
		s.visit(s.target+1, maxLength+1, 1)
	}
	var buffer [outputSize]byte
	output := appendNumber(buffer[:0], len(s.runs))
	output = append(output, '\n')
	for _, run := range s.runs {
		output = appendNumber(output, run[0])
		output = append(output, ' ')
		output = appendNumber(output, run[1])
		output = append(output, '\n')
	}
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
func appendNumber(out []byte, n int) []byte {
	var digits [digitsInInt]byte
	i := len(digits)
	for {
		i--
		digits[i] = byte(n%decimal) + '0'
		n /= decimal
		if n == 0 {
			return append(out, digits[i:]...)
		}
	}
}
