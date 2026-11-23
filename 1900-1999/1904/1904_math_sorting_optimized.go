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

type interval struct {
	left, right int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count int
	fastScan(in, &count)
	constants := make([]int, count)
	for i := range constants {
		fastScan(in, &constants[i])
	}
	intervals := []interval{{0, 1}}
	for i := count - 1; i >= 0; i-- {
		candidates := make([]interval, 0, 2*len(intervals))
		for _, item := range intervals {
			if item.right < 0 {
				continue
			}
			left := item.left
			if left < 0 {
				left = 0
			}
			candidates = append(candidates, interval{constants[i] - item.right, constants[i] - left})
			candidates = append(candidates, interval{constants[i] + left, constants[i] + item.right})
		}
		sort.Slice(candidates, func(a, b int) bool {
			if candidates[a].left != candidates[b].left {
				return candidates[a].left < candidates[b].left
			}
			return candidates[a].right < candidates[b].right
		})
		merged := make([]interval, 0, len(candidates))
		for _, item := range candidates {
			last := len(merged) - 1
			if last >= 0 && item.left <= merged[last].right {
				if item.right > merged[last].right {
					merged[last].right = item.right
				}
			} else {
				merged = append(merged, item)
			}
		}
		intervals = merged
	}
	out := bufio.NewWriter(os.Stdout)
	fastPrint(out, true, true, len(intervals))
	for _, item := range intervals {
		fastPrint(out, true, true, item.left, item.right)
	}
	out.Flush()
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
