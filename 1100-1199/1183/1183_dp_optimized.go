package main

import (
	"io"
	"strconv"
)

import (
	"bufio"

	"os"
	"strings"
)

var (
	s string
	// add[i][j]: fewest brackets to add so that s[i:j] becomes regular; how
	// it is best done: 0 pads a lone bracket, -1 wraps a pair, k splits at k
	add, how [][]int
)

func pair(a, b byte) bool {
	return (a == '(' && b == ')') || (a == '[' && b == ']')
}

func build(i, j int, out *strings.Builder) {
	if i == j {
		return
	}
	switch way := how[i][j]; {
	case way == 0:
		if s[i] == '(' || s[i] == ')' {
			out.WriteString("()")
		} else {
			out.WriteString("[]")
		}
	case way < 0:
		out.WriteByte(s[i])
		build(i+1, j-1, out)
		out.WriteByte(s[j-1])
	default:
		build(i, way, out)
		build(way, j, out)
	}
}

func main() {
	line, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	s = strings.TrimSpace(line)
	n := len(s)
	add, how = make([][]int, n+1), make([][]int, n+1)
	for i := range add {
		add[i], how[i] = make([]int, n+1), make([]int, n+1)
	}
	for length := 1; length <= n; length++ {
		for i := 0; i+length <= n; i++ {
			j := i + length
			if length == 1 {
				add[i][j] = 1
				continue
			}
			best, way := add[i][i+1]+add[i+1][j], i+1
			if pair(s[i], s[j-1]) && add[i+1][j-1] < best {
				best, way = add[i+1][j-1], -1
			}
			for k := i + 2; k < j; k++ {
				if add[i][k]+add[k][j] < best {
					best, way = add[i][k]+add[k][j], k
				}
			}
			add[i][j], how[i][j] = best, way
		}
	}
	var out strings.Builder
	build(0, n, &out)
	fastPrint(os.Stdout, true, true, out.String())
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
