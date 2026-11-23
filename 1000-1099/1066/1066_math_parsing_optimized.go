package main

import (
	"io"
	"io/ioutil"
	"os"
	"strconv"
)

import (
	"math"
)

func main() {
	var n int
	var a float64
	fastScan(os.Stdin, &n, &a)
	// with the second height x, lamp i hangs at a + (i-1)(x - a) + (i-1)(i-2)
	// and the last height grows with x, so x is the smallest value keeping every
	// lamp at height 0 or above
	x := 0.0
	for k := 1; k < n; k++ {
		x = math.Max(x, a-a/float64(k)-float64(k-1))
	}
	m := float64(n - 1)
	fastFormatted(os.Stdout, "%.2f\n", a+m*(x-a)+m*(m-1))
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

var fastFormatBuffer = make([]byte, 0, 64)

// Only the fixed integer, character, string and decimal formats used here are needed.
func fastFormatted(writer io.Writer, format string, values ...interface{}) (int, error) {
	buffer := fastFormatBuffer[:0]
	argument := 0
	for index := 0; index < len(format); index++ {
		if format[index] != '%' {
			buffer = append(buffer, format[index])
			continue
		}
		index++
		zero := false
		if format[index] == '0' {
			zero = true
			index++
		}
		width := 0
		for format[index] >= '0' && format[index] <= '9' {
			width = width*10 + int(format[index]-'0')
			index++
		}
		precision := 6
		if format[index] == '.' {
			index++
			precision = 0
			for format[index] >= '0' && format[index] <= '9' {
				precision = precision*10 + int(format[index]-'0')
				index++
			}
		}
		value := values[argument]
		argument++
		word := ""
		switch format[index] {
		case 's':
			word = value.(string)
		case 'd':
			switch v := value.(type) {
			case int:
				word = strconv.FormatInt(int64(v), 10)
			case int64:
				word = strconv.FormatInt(v, 10)
			default:
				panic("unsupported integer format")
			}
		case 'c':
			switch v := value.(type) {
			case int:
				word = string(rune(v))
			case int32:
				word = string(v)
			case uint8:
				word = string(rune(v))
			default:
				panic("unsupported character format")
			}
		case 'f':
			word = strconv.FormatFloat(value.(float64), 'f', precision, 64)
		default:
			panic("unsupported fixed format")
		}
		padding := byte(' ')
		if zero {
			padding = '0'
		}
		if zero && len(word) > 0 && word[0] == '-' {
			buffer = append(buffer, '-')
			word = word[1:]
			width--
		}
		for left := width - len(word); left > 0; left-- {
			buffer = append(buffer, padding)
		}
		buffer = append(buffer, word...)
	}
	fastFormatBuffer = buffer
	return writer.Write(buffer)
}
