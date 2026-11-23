package main

import (
	"io"
	"os"
	"strconv"
)

import (
	"math"
)

const km = 1000                // input distances are in thousands of kilometres
const roundingScaleSquared = 4 // square of the half-unit comparison scale

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	// a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
	// inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
	var a, b, c, d int64
	fastScan(os.Stdin, &a, &b, &c, &d)
	den := a*b - c*d
	diff := a*a + b*b - c*c - d*d
	if den == 0 || abs(diff) >= 2*abs(den) || b*c <= a*d {
		fastPrint(os.Stdout, true, true, "Impossible.")
		return
	}
	num := a*b*(c*c+d*d) - c*d*(a*a+b*b)
	if den < 0 {
		num = -num
		den = -den
	}
	distance := int64(km * math.Sqrt(float64(num)/float64(den)))
	// Compare the half-kilometre boundary exactly, dividing before scaling.
	scale := int64(roundingScaleSquared * km * km)
	bound := scale*(num/den) + scale*(num%den)/den
	if (2*distance+1)*(2*distance+1) <= bound {
		distance++
	}
	fastFormatted(os.Stdout, "Distance is %d km.\n", distance)
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
		case string:
			buffer = append(buffer, value...)

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
		if format[index] == '.' {
			index++
			for format[index] >= '0' && format[index] <= '9' {
				index++
			}
		}
		value := values[argument]
		argument++
		word := ""
		switch format[index] {

		case 'd':
			switch v := value.(type) {
			case int:
				word = strconv.FormatInt(int64(v), 10)
			case int64:
				word = strconv.FormatInt(v, 10)
			default:
				panic("unsupported integer format")
			}

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
