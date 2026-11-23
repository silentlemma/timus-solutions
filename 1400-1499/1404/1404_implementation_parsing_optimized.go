package main

import (
	"io"
	"io/ioutil"
	"os"
	// added to the first letter
)

const shift = 5
const letters = 26

func main() {
	var word string
	fastScan(os.Stdin, &word)
	// each code is the previous code plus the letter, modulo 26: take differences
	prev, plain := shift, make([]byte, len(word))
	for i := 0; i < len(word); i++ {
		code := int(word[i] - 'a')
		plain[i] = byte('a' + ((code-prev)%letters+letters)%letters)
		prev = code
	}
	fastPrint(os.Stdout, true, true, string(plain))
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
		case *string:
			*value = string(word)
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
