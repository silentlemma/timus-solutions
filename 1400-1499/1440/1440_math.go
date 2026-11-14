package main

import "syscall"

const (
	decimal        = 10
	outputCapacity = 80
	inputCapacity  = 128
)

var weekdays = [...]string{
	"Monday", "Tuesday", "Wednesday", "Thursday",
	"Friday", "Saturday", "Sunday",
}
var months = [...]string{"September", "October", "November", "December"}
var monthOffsets = [...]int{0, 30, 61, 91}

var input [inputCapacity]byte
var start, end int

const byteBits = 8

func nameKey(first, second byte) uint16 {
	return uint16(first)<<byteBits | uint16(second)
}

func readName() uint16 {
	first := nextByte()
	for first != 0 && first <= ' ' {
		first = nextByte()
	}
	key := nameKey(first, nextByte())
	for c := nextByte(); c > ' '; c = nextByte() {
	}
	return key
}
func nextByte() byte {
	if start == end {
		for {
			n, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if n <= 0 {
				return 0
			}
			start, end = 0, n
			break
		}
	}
	value := input[start]
	start++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*decimal + int(c-'0')
		c = nextByte()
	}
	return value
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
	weekday := readName()
	month := readName()
	date, minimum, maximum := number(), number(), number()
	first, monthIndex := 0, 0
	for nameKey(weekdays[first][0], weekdays[first][1]) != weekday {
		first++
	}
	for nameKey(months[monthIndex][0], months[monthIndex][1]) != month {
		monthIndex++
	}
	week := len(weekdays)
	trainingDays := monthOffsets[monthIndex] + date - 2
	fullWeeks, extra := trainingDays/week, trainingDays%week
	for count := 1; count <= week; count++ {
		// Pick the lowest number of frequent days allowed by both bounds.
		frequent := max(0, max(count-(week-extra), minimum-count*fullWeeks))
		if frequent > count || frequent > extra || count*fullWeeks+frequent > maximum {
			continue
		}
		ordinary := count - frequent
		var buffer [outputCapacity]byte
		output := append(buffer[:0], byte('0'+count), '\n')
		for i := 0; i < week; i++ {
			if i < frequent || extra <= i && i < extra+ordinary {
				output = append(output, weekdays[(first+1+i)%week]...)
				output = append(output, '\n')
			}
		}
		write(output)
		return
	}
	write([]byte("Impossible\n"))
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
