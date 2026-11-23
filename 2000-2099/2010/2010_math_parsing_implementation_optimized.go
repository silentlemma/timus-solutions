package main

import (
	"io"
	"strconv"
)

import (
	"bufio"

	"os"
)

const moveCount = 8
const pieceCount = 5

var moves = [moveCount][2]int64{
	{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
	{1, -2}, {1, 2}, {2, -1}, {2, 1},
}

func minimum(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func solve(n, x, y int64) [pieceCount]int64 {
	a, b := int64(1), int64(1)
	if x > 1 {
		a++
	}
	if x < n {
		a++
	}
	if y > 1 {
		b++
	}
	if y < n {
		b++
	}
	king := a*b - 1
	knight := int64(0)
	for _, move := range moves {
		nx, ny := x+move[0], y+move[1]
		if 1 <= nx && nx <= n && 1 <= ny && ny <= n {
			knight++
		}
	}
	bishop := minimum(x-1, y-1) + minimum(x-1, n-y) + minimum(n-x, y-1) + minimum(n-x, n-y)
	rook := 2 * (n - 1)
	return [pieceCount]int64{king, knight, bishop, rook, rook + bishop}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, x, y int64
	fastScan(in, &n, &x, &y)
	labels := [pieceCount]string{"King", "Knight", "Bishop", "Rook", "Queen"}
	for i, value := range solve(n, x, y) {
		fastFormatted(os.Stdout, "%s: %d\n", labels[i], value)
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
