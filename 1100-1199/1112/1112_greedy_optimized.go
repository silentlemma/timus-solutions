package main

import (
	"io"
	"io/ioutil"
	"strconv"
)

import (
	"bufio"

	"os"
	"sort"
)

const numericBitSize = 64
const initialOutputCapacity = 64

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fastScan(in, &n)
	segs := make([][2]int, n)
	for i := range segs {
		fastScan(in, &segs[i][0], &segs[i][1])
	}
	// the segment that ends first leaves the most room for the rest; touching
	// ends share no inner point
	sort.Slice(segs, func(i, j int) bool { return segs[i][1] < segs[j][1] })
	var chosen [][2]int
	for _, s := range segs {
		if len(chosen) == 0 || s[0] >= chosen[len(chosen)-1][1] {
			chosen = append(chosen, s)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fastPrint(out, true, true, len(chosen))
	for _, s := range chosen {
		fastPrint(out, true, true, s[0], s[1])
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
