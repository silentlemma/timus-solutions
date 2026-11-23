package main

import (
	"io"
	"io/ioutil"
	"os"
	"strconv"
)

type branch struct{ to, apples int }

var (
	adj [][]branch
	q   int
)

// solve: best[k] is the most apples on k branches kept in the subtree of v,
// all of them connected to v; the slice is only as long as k can go.
func solve(v, parent int) []int {
	best := []int{0}
	for _, e := range adj[v] {
		if e.to == parent {
			continue
		}
		sub := solve(e.to, v)
		size := len(best) + len(sub)
		if size > q+1 {
			size = q + 1
		}
		merged := make([]int, size)
		for i := range merged {
			merged[i] = -1
		}
		for i, a := range best {
			// taking j >= 1 branches on the child's side: its edge and j - 1 below
			for j := 0; j <= len(sub) && i+j < size; j++ {
				gain := 0
				if j > 0 {
					gain = e.apples + sub[j-1]
				}
				if a+gain > merged[i+j] {
					merged[i+j] = a + gain
				}
			}
		}
		best = merged
	}
	return best
}

func main() {
	var n int
	fastScan(os.Stdin, &n, &q)
	adj = make([][]branch, n+1)
	for i := 1; i < n; i++ {
		var a, b, apples int
		fastScan(os.Stdin, &a, &b, &apples)
		adj[a] = append(adj[a], branch{b, apples})
		adj[b] = append(adj[b], branch{a, apples})
	}
	fastPrint(os.Stdout, true, true, solve(1, 0)[q])
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
