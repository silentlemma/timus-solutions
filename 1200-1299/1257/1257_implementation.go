package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

const width = 40

type rule struct {
	pattern string // s1s2 in lower case
	carry   int    // length of s2
}

func isLetter(c byte) bool {
	return 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z'
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	lines := strings.Split(strings.Replace(string(data), "\r", "", -1), "\n")
	n, _ := strconv.Atoi(strings.TrimSpace(lines[0]))
	// a rule s1-s2 matches words ending in s1s2 and carries s2 over
	rules := make([]rule, n)
	for i := range rules {
		line := strings.TrimSpace(lines[1+i])
		dash := strings.IndexByte(line, '-')
		rules[i] = rule{strings.ToLower(line[:dash] + line[dash+1:]), len(line) - dash - 1}
	}
	text := strings.Join(lines[n+1:], "\n")
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	col := 0
	for i := 0; i < len(text); {
		c := text[i]
		if c == '\n' {
			out.WriteByte(c)
			col = 0
			i++
			continue
		}
		if !isLetter(c) {
			// a full line moves a separator to the next one
			if col == width {
				out.WriteByte('\n')
				col = 0
			}
			out.WriteByte(c)
			col++
			i++
			continue
		}
		start := i
		for i < len(text) && isLetter(text[i]) {
			i++
		}
		word := text[start:i]
		if col+len(word) <= width {
			out.WriteString(word)
			col += len(word)
			continue
		}
		// the shortest carried part whose head and '-' still fit
		lower := strings.ToLower(word)
		carry := 0
		for _, r := range rules {
			fits := col+len(word)-r.carry+1 <= width
			if strings.HasSuffix(lower, r.pattern) && fits && (carry == 0 || r.carry < carry) {
				carry = r.carry
			}
		}
		if carry > 0 {
			out.WriteString(word[:len(word)-carry] + "-\n" + word[len(word)-carry:])
		} else {
			out.WriteString("\n" + word)
			carry = len(word)
		}
		col = carry
	}
}
