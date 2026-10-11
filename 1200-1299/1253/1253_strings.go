package main

import (
	"bufio"
	"bytes"
	"io/ioutil"
	"os"
	"strconv"
)

const limit = 1000000

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	data = bytes.ReplaceAll(data, []byte("\r"), nil)
	line := bytes.IndexByte(data, '\n')
	n, _ := strconv.Atoi(string(bytes.TrimSpace(data[:line])))
	// a template runs from the start of a line to its '#'
	text := make([][]byte, n+1)
	rest := data[line+1:]
	for i := 1; i <= n; i++ {
		end := bytes.IndexByte(rest, '#')
		text[i] = rest[:end]
		rest = rest[end+1:]
		if len(rest) > 0 && rest[0] == '\n' {
			rest = rest[1:]
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// size[i]: the length of template i fully expanded, capped above the
	// limit; state 1 marks templates being expanded, so meeting one again
	// is a cycle and the expansion never ends
	size, state := make([]int, n+1), make([]int, n+1)
	var measure func(int) bool
	measure = func(i int) bool {
		state[i] = 1
		for k := 0; k < len(text[i]); k++ {
			if text[i][k] != '*' {
				size[i]++
				continue
			}
			k++
			j := int(text[i][k] - '0')
			if state[j] == 1 || state[j] == 0 && !measure(j) {
				return false
			}
			size[i] = min(size[i]+size[j], limit+1)
		}
		state[i] = 2
		return true
	}
	if !measure(1) || size[1] > limit {
		out.WriteString("#\n")
		return
	}
	var write func(int)
	write = func(i int) {
		for k := 0; k < len(text[i]); k++ {
			if text[i][k] == '*' {
				k++
				write(int(text[i][k] - '0'))
			} else {
				out.WriteByte(text[i][k])
			}
		}
	}
	write(1)
	out.WriteString("\n")
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
