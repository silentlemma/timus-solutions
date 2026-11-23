package main

import (
	"io"
	"io/ioutil"
	"strconv"
)

import (
	"bufio"

	"os"
	"strings"
)

// edges of the cube: A B C D around the bottom face, E F G H above them
var edges = []string{"AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH"}

const (
	// the cube is bipartite; every operation changes one chamber of each side
	evenSide = "ACFH"
	cells    = "ABCDEFGH"
)

func even(c byte) bool { return strings.IndexByte(evenSide, c) >= 0 }

func main() {
	count := map[byte]int{}
	balance := 0
	for i := range cells {
		var v int
		fastScan(os.Stdin, &v)
		count[cells[i]] = v
		if even(cells[i]) {
			balance += v
		} else {
			balance -= v
		}
	}
	if balance != 0 {
		fastPrint(os.Stdout, true, true, "IMPOSSIBLE")
		return
	}
	near := map[byte][]byte{}
	for _, e := range edges {
		near[e[0]] = append(near[e[0]], e[1])
		near[e[1]] = append(near[e[1]], e[0])
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	emit := func(a, b, sign byte) { out.Write([]byte{a, b, sign, '\n'}) }
	// annihilate along every edge as long as both ends hold duons; afterwards
	// every edge has an empty end
	for _, e := range edges {
		k := count[e[0]]
		if count[e[1]] < k {
			k = count[e[1]]
		}
		for j := 0; j < k; j++ {
			emit(e[0], e[1], '-')
		}
		count[e[0]] -= k
		count[e[1]] -= k
	}
	// what is left can only sit at two opposite corners u and w, in equal
	// numbers; a pair made on the middle edge of a path u x y w removes both
	for i := range evenSide {
		u := evenSide[i]
		if count[u] == 0 {
			continue
		}
		var w, y byte
		for j := range cells {
			if c := cells[j]; w == 0 && count[c] > 0 && !even(c) {
				w = c
			}
		}
		x := near[u][0]
		for _, c := range near[x] {
			for _, d := range near[w] {
				if y == 0 && c == d {
					y = c
				}
			}
		}
		for k := 0; k < count[u]; k++ {
			emit(x, y, '+')
			emit(u, x, '-')
			emit(y, w, '-')
		}
		count[w] -= count[u]
		count[u] = 0
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
