package main

import "syscall"

const (
	week      = 7
	year      = 365
	leap      = 4
	century   = 100
	era       = 400
	maxWeeks  = 6
	cell      = 5
	dayName   = 3
	inputSize = 64
)

var names = [week]string{"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
var monthLengths = [...]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

var input [inputSize]byte
var inputPosition, inputLength int

// Use standard handles directly; retry interrupts and finish short writes.
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

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength = readInput(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func nextInt() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return value
}

func main() {
	day, month, currentYear := nextInt(), nextInt(), nextInt()
	lengths := monthLengths
	if currentYear%leap == 0 && (currentYear%century != 0 || currentYear%era == 0) {
		lengths[1]++
	}
	past := currentYear - 1
	before := year*past + past/leap - past/century + past/era
	for _, length := range lengths[:month-1] {
		before += length
	}
	first, days := before%week, lengths[month-1]
	columns := (first + days + week - 1) / week
	var output [week * (dayName + maxWeeks*cell + 1)]byte
	line := output[:0]
	for row, name := range names {
		line = append(line, name...)
		for col := 0; col < columns; col++ {
			current := col*week + row - first + 1
			last := col+1 == columns
			if current < 1 || current > days {
				line = append(line, "    "...)
				if !last {
					line = append(line, ' ')
				}
				continue
			}
			left, right := byte(' '), byte(' ')
			if current == day {
				left, right = '[', ']'
			}
			tens := byte(' ')
			if current >= 10 {
				tens = '0' + byte(current/10)
			}
			line = append(line, ' ', left, tens, '0'+byte(current%10))
			if !last || current == day {
				line = append(line, right)
			}
		}
		line = append(line, '\n')
	}
	writeAll(line)
}
