package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
)

// bytesCount is the number of different byte values
const bytesCount = 256

// quoted returns the text between quotes starting at p, with doubled quotes
// undone, and the index just past the closing quote
func quoted(line []byte, p int) ([]byte, int) {
	var out []byte
	for p++; p < len(line); p++ {
		if line[p] == '\'' {
			if p+1 < len(line) && line[p+1] == '\'' {
				out = append(out, '\'')
				p++
				continue
			}
			return out, p + 1
		}
		out = append(out, line[p])
	}
	return out, p
}

func like(text, pattern []byte) bool {
	n, m := len(text), len(pattern)
	// reach[i]: the pattern so far can match exactly the first i bytes
	reach := make([]bool, n+1)
	reach[0] = true
	for j := 0; j < m; {
		c := pattern[j]
		next := make([]bool, n+1)
		switch c {
		case '%':
			seen := false
			for i := 0; i <= n; i++ {
				seen = seen || reach[i]
				next[i] = seen
			}
			j++
		case '[':
			// a set of bytes, negated after ^, with ranges a-b unless b is ]
			k := j + 1
			negated := k < m && pattern[k] == '^'
			if negated {
				k++
			}
			var accepted [bytesCount]bool
			for k < m && pattern[k] != ']' {
				lo, hi := pattern[k], pattern[k]
				if k+2 < m && pattern[k+1] == '-' && pattern[k+2] != ']' {
					hi = pattern[k+2]
					k += 2
				}
				for x := int(lo); x <= int(hi); x++ {
					accepted[x] = true
				}
				k++
			}
			if k == m {
				return false // a [ with no closing ] never matches
			}
			for i := 0; i < n; i++ {
				next[i+1] = reach[i] && accepted[text[i]] != negated
			}
			j = k + 1
		default:
			for i := 0; i < n; i++ {
				next[i+1] = reach[i] && (c == '_' || text[i] == c)
			}
			j++
		}
		reach = next
	}
	return reach[n]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	first, _ := in.ReadBytes('\n')
	n, _ := strconv.Atoi(string(bytes.TrimSpace(first)))
	for q := 0; q < n; q++ {
		line, _ := in.ReadBytes('\n')
		line = bytes.TrimRight(line, "\r\n")
		text, p := quoted(line, bytes.IndexByte(line, '\''))
		pattern, _ := quoted(line, p+bytes.IndexByte(line[p:], '\''))
		if like(text, pattern) {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
}
