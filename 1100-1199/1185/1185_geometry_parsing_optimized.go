package main

import (
	"io"
	"io/ioutil"
	"strconv"
)

import (
	"bufio"

	"math"
	"os"
	"sort"
)

type pt struct{ x, y int64 }

func cross(o, a, b pt) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var gap float64
	fastScan(in, &n, &gap)
	pts := make([]pt, n)
	for i := range pts {
		fastScan(in, &pts[i].x, &pts[i].y)
	}
	sort.Slice(pts, func(i, j int) bool {
		if pts[i].x != pts[j].x {
			return pts[i].x < pts[j].x
		}
		return pts[i].y < pts[j].y
	})
	// the shortest wall is the convex hull pushed out by L: its straight
	// parts add up to the hull perimeter, and its arcs turn once around a
	// full circle of radius L in total
	var hull []pt
	for pass := 0; pass < 2; pass++ {
		var part []pt
		for _, p := range pts {
			for len(part) >= 2 && cross(part[len(part)-2], part[len(part)-1], p) <= 0 {
				part = part[:len(part)-1]
			}
			part = append(part, p)
		}
		hull = append(hull, part[:len(part)-1]...)
		for i, j := 0, len(pts)-1; i < j; i, j = i+1, j-1 {
			pts[i], pts[j] = pts[j], pts[i]
		}
	}
	length := 2 * math.Pi * gap
	for k := range hull {
		a, b := hull[k], hull[(k+1)%len(hull)]
		length += math.Hypot(float64(a.x-b.x), float64(a.y-b.y))
	}
	fastPrint(os.Stdout, true, true, int64(math.Round(length)))
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
		case *float64:
			parsed, err := strconv.ParseFloat(string(word), 64)
			if err != nil {
				return index, err
			}
			*value = parsed
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

		case int64:
			buffer = strconv.AppendInt(buffer, value, 10)

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
