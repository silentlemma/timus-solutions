package main

import (
	"io"
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
	total := int64(0)
	for i := 0; i < n; i++ {
		var d int64
		fastScan(in, &d)
		total += d
	}
	fastPrint( // a trip to a city with load L costs L d there and (L - d) d back; summed over
		// any order this is (sum of d)^2, so the order does not matter
		os.Stdout, true, true, total*total)
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
		case *int64:
			negative := word[0] == '-'
			first := 0
			if negative || word[0] == '+' {
				first = 1
			}
			if first == len(word) {
				return index, io.ErrUnexpectedEOF
			}
			number := int64(0)
			for _, digit := range word[first:] {
				if digit < '0' || digit > '9' {
					return index, io.ErrUnexpectedEOF
				}
				number = number*10 - int64(digit-'0')
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

		case int64:
			buffer = strconv.AppendInt(buffer, value, 10)

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
