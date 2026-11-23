package main

import (
	"io"
)

import (
	"bufio"

	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var m int
	fastScan(in, &m)
	var values []int
	for {
		var v int
		if _, err := fastScan(in, &v); err != nil || v < 0 {
			break
		}
		values = append(values, v)
	}
	// indices of the window whose values decrease from front to back: the
	// front is the maximum, and a value never matters once a later one is larger
	window := make([]int, 0, len(values))
	head := 0
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i, v := range values {
		for len(window) > head && values[window[len(window)-1]] <= v {
			window = window[:len(window)-1]
		}
		window = append(window, i)
		if window[head] <= i-m {
			head++
		}
		if i >= m-1 {
			out.WriteString(strconv.Itoa(values[window[head]]) + "\n")
		}
	}
}

const inputBufferBytes = 8192

var fastInputReader io.Reader
var fastInputBuffer [inputBufferBytes]byte
var fastInputPosition, fastInputLength int
var fastInputLoaded bool

// Read the single input stream once and convert tokens without fmt reflection.
func fastScan(reader io.Reader, targets ...interface{}) (int, error) {
	if !fastInputLoaded {
		fastInputReader = reader
		fastInputLoaded = true
	}
	for index, target := range targets {
		ch, err := scanByte()
		for err == nil && ch <= ' ' {
			ch, err = scanByte()
		}
		if err != nil {
			return index, err
		}
		var inline [128]byte
		word := inline[:0]
		for {
			word = append(word, ch)
			ch, err = scanByte()
			if err != nil || ch <= ' ' {
				break
			}
		}
		if err != nil && err != io.EOF {
			return index, err
		}
		switch value := target.(type) {
		case *int:
			negative := word[0] == '-'
			first := 0
			if negative || word[0] == '+' {
				first = 1
			}
			if first == len(word) {
				return index, io.ErrUnexpectedEOF
			}
			number := int(0)
			for _, digit := range word[first:] {
				if digit < '0' || digit > '9' {
					return index, io.ErrUnexpectedEOF
				}
				number = number*10 - int(digit-'0')
			}
			if !negative {
				number = -number
			}
			*value = number
		default:
			panic("unsupported input type")
		}
	}
	return len(targets), nil
}

// Keep only a bounded refill buffer and the current token; Read may return partial data.
func scanByte() (byte, error) {
	for fastInputPosition == fastInputLength {
		var err error
		fastInputLength, err = fastInputReader.Read(fastInputBuffer[:])
		fastInputPosition = 0
		if fastInputLength > 0 {
			break
		}
		if err != nil {
			return 0, err
		}
	}
	value := fastInputBuffer[fastInputPosition]
	fastInputPosition++
	return value, nil
}
