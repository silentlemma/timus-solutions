package main

import (
	"io"
	"io/ioutil"
	"strconv"
)

import (
	"bufio"

	"os"
	"strings"
)

const buffer = 8192 // the text is up to 100 000 characters

func main() {
	in := bufio.NewReaderSize(os.Stdin, buffer)
	first, _ := in.ReadString('\n')
	var n, m int
	fastScan(strings.NewReader(first), &n, &m)
	// ReadString handles complete lines even when they exceed the refill buffer.
	text, _ := in.ReadString('\n') // read whole: the text may start with spaces
	text = strings.TrimRight(text, "\r\n")
	// run[i]: how many letters and spaces start at position i
	run := make([]uint32, len(text)+1)
	for i := len(text) - 1; i >= 0; i-- {
		c := text[i]
		if c == ' ' || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
			run[i] = run[i+1] + 1
		}
	}
	// the farthest reach never moves back, so the longest message each time is best
	pos, count := 0, 0
	for pos < len(text) {
		step := int(run[pos])
		if step > m {
			step = m
		}
		if step < n {
			step = n
		}
		pos += step
		count++
	}
	fastPrint(os.Stdout, true, true, count)
}

var fastInputData []byte
var fastInputPosition int
var fastInputLoaded bool

// Read the single input stream once and convert tokens without fmt reflection.
func fastScan(reader io.Reader, targets ...interface{}) (int, error) {
	if !fastInputLoaded {
		var err error
		fastInputData, err = ioutil.ReadAll(reader)
		if err != nil {
			return 0, err
		}
		fastInputLoaded = true
	}
	for index, target := range targets {
		for fastInputPosition < len(fastInputData) && fastInputData[fastInputPosition] <= ' ' {
			fastInputPosition++
		}
		start := fastInputPosition
		for fastInputPosition < len(fastInputData) && fastInputData[fastInputPosition] > ' ' {
			fastInputPosition++
		}
		if start == fastInputPosition {
			return index, io.EOF
		}
		word := fastInputData[start:fastInputPosition]
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

var fastOutputBuffer = make([]byte, 0, 64)

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func fastPrint(writer io.Writer, spaced, newline bool, values ...interface{}) (int, error) {
	buffer := fastOutputBuffer[:0]
	previousString := false
	for index, value := range values {
		_, isString := value.(string)
		if index > 0 && (spaced || (!previousString && !isString)) {
			buffer = append(buffer, ' ')
		}
		switch value := value.(type) {

		case int:
			buffer = strconv.AppendInt(buffer, int64(value), 10)

		default:
			panic("unsupported output type")
		}
		previousString = isString
	}
	if newline {
		buffer = append(buffer, '\n')
	}
	fastOutputBuffer = buffer
	return writer.Write(buffer)
}
