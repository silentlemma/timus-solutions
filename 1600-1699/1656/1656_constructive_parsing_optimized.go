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

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fastScan(in, &n); err != nil {
		return
	}
	heights := make([]int, n*n)
	for i := range heights {
		fastScan(in, &heights[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(heights)))
	mid := n / 2
	// cells by (nearer, farther) distance from the centre row and column:
	// along any row or column this grows outwards on each side
	type cell struct{ near, far, r, c int }
	var cells []cell
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			a, b := abs(r-mid), abs(c-mid)
			if a > b {
				a, b = b, a
			}
			cells = append(cells, cell{a, b, r, c})
		}
	}
	sort.SliceStable(cells, func(x, y int) bool {
		if cells[x].near != cells[y].near {
			return cells[x].near < cells[y].near
		}
		return cells[x].far < cells[y].far
	})
	grid := make([][]int, n)
	for r := range grid {
		grid[r] = make([]int, n)
	}
	for k, p := range cells {
		grid[p.r][p.c] = heights[k]
	}
	for _, row := range grid {
		for c, h := range row {
			if c > 0 {
				fastPrint(out, false, false, " ")
			}
			fastPrint(out, false, false, h)
		}
		fastPrint(out, true, true)
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
		case string:
			buffer = append(buffer, value...)
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
