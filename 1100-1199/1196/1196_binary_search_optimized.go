package main

import (
	"bufio"
	"os"
	"strconv"
)

// bufferSize is the reader's buffer size in bytes
const bufferSize = 4096

// the dates are parsed by hand from a 4 KB buffered reader instead of a
// 1 MB word scanner, and kept as int32
var input = bufio.NewReaderSize(os.Stdin, bufferSize)

func nextInt() int {
	value := 0
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	for err == nil && ch >= '0' && ch <= '9' {
		value = value*10 + int(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

// a plain binary search over the int32 dates instead of sort.SearchInts
func contains(known []int32, year int32) bool {
	left, right := 0, len(known)
	for left < right {
		middle := left + (right-left)/2
		if known[middle] == year {
			return true
		}
		if known[middle] < year {
			left = middle + 1
		} else {
			right = middle
		}
	}
	return false
}

func main() {
	// the teacher's dates come sorted, so each of the student's dates is
	// looked up by binary search, counting repeats every time
	known := make([]int32, nextInt())
	for i := range known {
		known[i] = int32(nextInt())
	}
	queries, count := nextInt(), 0
	for i := 0; i < queries; i++ {
		if contains(known, int32(nextInt())) {
			count++
		}
	}
	os.Stdout.WriteString(strconv.Itoa(count) + "\n")
}
