package main

import (
	"io"
	"io/ioutil"
	"strconv"
)

import (
	"bufio"

	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fastScan(in, &n)
	// every sum from 1 to reach is made of the notes taken so far; a note
	// no larger than reach + 1 extends that to reach + note
	reach := 0
	for i := 0; i < n; i++ {
		var d int
		fastScan(in, &d)
		if d > reach+1 {
			break
		}
		reach += d
	}
	fastPrint(os.Stdout, true, true, reach+1)
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
