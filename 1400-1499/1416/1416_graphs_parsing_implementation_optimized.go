package main

import (
	"io"
	"strconv"
)

import (
	"bufio"

	"os"
)

const inf = 1 << 30

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fastScan(in, &n, &m)
	w := make([][]int, n)
	for i := range w {
		w[i] = make([]int, n)
		for j := range w[i] {
			w[i][j] = inf
		}
	}
	ea, eb, ec := make([]int, m), make([]int, m), make([]int, m)
	for i := 0; i < m; i++ {
		fastScan(in, &ea[i], &eb[i], &ec[i])
		ea[i]--
		eb[i]--
		w[ea[i]][eb[i]], w[eb[i]][ea[i]] = ec[i], ec[i]
	}
	// Prim on the matrix; heaviest[u][v] is the heaviest tree edge between u and v
	heaviest := make([][]int, n)
	inTree := make([][]bool, n)
	for i := range heaviest {
		heaviest[i] = make([]int, n)
		inTree[i] = make([]bool, n)
	}
	dist := append([]int(nil), w[0]...)
	parent := make([]int, n)
	done := make([]bool, n)
	done[0] = true
	order := []int{0}
	total := 0
	for step := 1; step < n; step++ {
		v := -1
		for u := 0; u < n; u++ {
			if !done[u] && (v < 0 || dist[u] < dist[v]) {
				v = u
			}
		}
		p, c := parent[v], dist[v]
		total += c
		inTree[p][v], inTree[v][p] = true, true
		for _, u := range order {
			h := heaviest[p][u]
			if c > h {
				h = c
			}
			heaviest[u][v], heaviest[v][u] = h, h
		}
		done[v] = true
		order = append(order, v)
		for u := 0; u < n; u++ {
			if !done[u] && w[v][u] < dist[u] {
				dist[u], parent[u] = w[v][u], v
			}
		}
	}
	// the next tree swaps one outside edge for the heaviest edge on its tree path
	swap := inf
	for i := 0; i < m; i++ {
		if d := ec[i] - heaviest[ea[i]][eb[i]]; !inTree[ea[i]][eb[i]] && d < swap {
			swap = d
		}
	}
	fastFormatted(os.Stdout, "Cost: %d\n", total)
	if swap == inf {
		fastPrint(os.Stdout, true, true, "Cost: -1")
	} else {
		fastFormatted(os.Stdout, "Cost: %d\n", total+swap)
	}
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
