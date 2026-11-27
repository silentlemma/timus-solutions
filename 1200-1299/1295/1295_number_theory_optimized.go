package main

import (
	"io"
	"io/ioutil"
	"os"
	"strconv"
)

const mod = 100
const bases = 4
const numericBits = 64

func power(base, n int) int {
	r := 1
	for ; n > 0; n >>= 1 {
		if n&1 == 1 {
			r = r * base % mod
		}
		base = base * base % mod
	}
	return r
}

func main() {
	var n int
	fastScan(os.Stdin, &n)
	// from the second power on the sum is even but never divisible by 8,
	// so it ends in at most two zeros and its remainder mod 100 decides
	s := 0
	for b := 1; b <= bases; b++ {
		s = (s + power(b, n)) % mod
	}
	switch {
	case s == 0:
		fastPrint(os.Stdout, true, true, 2)
	case s%10 == 0:
		fastPrint(os.Stdout, true, true, 1)
	default:
		fastPrint(os.Stdout, true, true, 0)
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
			*value, err = strconv.ParseInt(word, 10, numericBits)
		case *uint64:
			*value, err = strconv.ParseUint(word, 10, numericBits)
		case *float64:
			*value, err = strconv.ParseFloat(word, numericBits)
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
			buffer = strconv.AppendFloat(buffer, value, 'g', -1, numericBits)
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
