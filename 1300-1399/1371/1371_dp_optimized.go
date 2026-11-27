package main

import (
	"io"
	"io/ioutil"
	"strconv"
)

import (
	"bufio"

	"os"
)

type edge struct{ to, cost int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fastScan(in, &n)
	adj := make([][]edge, n+1)
	for i := 0; i < n-1; i++ {
		var a, b, c int
		fastScan(in, &a, &b, &c)
		adj[a] = append(adj[a], edge{b, c})
		adj[b] = append(adj[b], edge{a, c})
	}
	// an edge with s branches on one side carries the s (n - s) pairs that
	// it separates; sizes come from a parents-first order read backwards
	parent, cost := make([]int, n+1), make([]int64, n+1)
	parent[1] = -1
	order := []int{1}
	for i := 0; i < len(order); i++ {
		v := order[i]
		for _, e := range adj[v] {
			if e.to != parent[v] {
				parent[e.to], cost[e.to] = v, int64(e.cost)
				order = append(order, e.to)
			}
		}
	}
	size := make([]int64, n+1)
	for i := range size {
		size[i] = 1
	}
	total := int64(0)
	for i := len(order) - 1; i > 0; i-- {
		v := order[i]
		size[parent[v]] += size[v]
		total += cost[v] * size[v] * (int64(n) - size[v])
	}
	fastFormatted( // every pair is counted in both directions
		os.Stdout, "%.4f\n", 2*float64(total)/(float64(n)*float64(n-1)))
}

const integerBitSize = 64
const floatBitSize = 64
const defaultFloatPrecision = 6

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
			*value, err = strconv.ParseInt(word, 10, integerBitSize)
		case *uint64:
			*value, err = strconv.ParseUint(word, 10, integerBitSize)
		case *float64:
			*value, err = strconv.ParseFloat(word, floatBitSize)
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
		precision := defaultFloatPrecision
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
			word = strconv.FormatFloat(value.(float64), 'f', precision, floatBitSize)
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
