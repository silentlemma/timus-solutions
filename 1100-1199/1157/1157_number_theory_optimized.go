package main

import (
	"io"
	"os"
	"strconv"

	// limit: answers above it are reported as 0
	"io/ioutil"
)

const limit = 10000

func main() {
	var m, n, k int
	fastScan(os.Stdin, &m, &n, &k)
	// x tiles make one rectangle per divisor pair a * b = x with a <= b, that
	// is half the number of divisors, rounded up
	divisors := make([]int, limit+1)
	for d := 1; d <= limit; d++ {
		for x := d; x <= limit; x += d {
			divisors[x]++
		}
	}
	shapes := func(x int) int { return (divisors[x] + 1) / 2 }
	for t := k + 1; t <= limit; t++ {
		if shapes(t) == n && shapes(t-k) == m {
			fastPrint(os.Stdout, true, true, t)
			return
		}
	}
	fastPrint(os.Stdout, true, true, 0)
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
		word := string(fastInputData[start:fastInputPosition])
		var err error
		switch value := target.(type) {
		case *string:
			*value = word
		case *int:
			*value, err = strconv.Atoi(word)
		case *int64:
			*value, err = strconv.ParseInt(word, 10, 64)
		case *uint64:
			*value, err = strconv.ParseUint(word, 10, 64)
		case *float64:
			*value, err = strconv.ParseFloat(word, 64)
		default:
			panic("unsupported input type")
		}
		if err != nil {
			return index, err
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
		case string:
			buffer = append(buffer, value...)
		case int:
			buffer = strconv.AppendInt(buffer, int64(value), 10)
		case int64:
			buffer = strconv.AppendInt(buffer, value, 10)
		case uint64:
			buffer = strconv.AppendUint(buffer, value, 10)
		case float64:
			buffer = strconv.AppendFloat(buffer, value, 'g', -1, 64)
		case bool:
			buffer = strconv.AppendBool(buffer, value)
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
