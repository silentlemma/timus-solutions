package main

import (
	"io"
	"io/ioutil"
	"os"
)

import (
	"strconv"
	"strings"
)

const numericBitSize = 64
const initialOutputCapacity = 64

// power computes x^n mod m by repeated squaring
func power(x, n, m int) int {
	result := 1 % m
	for x %= m; n > 0; n >>= 1 {
		if n&1 == 1 {
			result = result * x % m
		}
		x = x * x % m
	}
	return result
}

func main() {
	var n, m, y int
	fastScan(os.Stdin, &n, &m, &y)
	// only M candidates; a Y of M or more is never a remainder
	var roots []string
	for x := 0; x < m; x++ {
		if power(x, n, m) == y {
			roots = append(roots, strconv.Itoa(x))
		}
	}
	if len(roots) == 0 {
		fastPrint(os.Stdout, true, true, -1)
	} else {
		fastPrint(os.Stdout, true, true, strings.Join(roots, " "))
	}
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
			*value, err = strconv.ParseInt(word, 10, numericBitSize)
		case *uint64:
			*value, err = strconv.ParseUint(word, 10, numericBitSize)
		case *float64:
			*value, err = strconv.ParseFloat(word, numericBitSize)
		default:
			panic("unsupported input type")
		}
		if err != nil {
			return index, err
		}
	}
	return len(targets), nil
}

var fastOutputBuffer = make([]byte, 0, initialOutputCapacity)

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
			buffer = strconv.AppendFloat(buffer, value, 'g', -1, numericBitSize)
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
