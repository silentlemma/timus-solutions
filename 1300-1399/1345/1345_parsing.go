package main

import (
	"bufio"
	"bytes"
	"io/ioutil"
	"os"
	"strings"
)

var keywords = map[string]bool{}

func init() {
	for _, w := range strings.Fields("and array begin case class const div do else end for" +
		" function if implementation interface mod not of or procedure program record repeat" +
		" shl shr string then to type unit until uses var with while") {
		keywords[w] = true
	}
}

func isDigit(c byte) bool { return c >= '0' && c <= '9' }
func isWord(c byte) bool  { return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c == '_' }

func main() {
	raw, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	text := bytes.ReplaceAll(raw, []byte("\r\n"), []byte("\n"))
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	wrap := func(kind string, part []byte) {
		out.WriteString("<span class=" + kind + ">")
		out.Write(part)
		out.WriteString("</span>")
	}
	n := len(text)
	for i := 0; i < n; {
		c, j := text[i], i+1
		switch {
		case c == '{':
			j = n
			if k := bytes.IndexByte(text[i:], '}'); k >= 0 {
				j = i + k + 1
			}
			wrap("comment", text[i:j])
		case c == '/' && i+1 < n && text[i+1] == '/':
			j = n // the line break is not part of it
			if k := bytes.IndexByte(text[i:], '\n'); k >= 0 {
				j = i + k
			}
			wrap("comment", text[i:j])
		case c == '\'':
			j = n
			if k := bytes.IndexByte(text[i+1:], '\''); k >= 0 {
				j = i + 1 + k + 1
			}
			wrap("string", text[i:j])
		case c == '#' && i+1 < n && isDigit(text[i+1]):
			for j = i + 1; j < n && isDigit(text[j]); j++ {
			}
			wrap("string", text[i:j])
		case isDigit(c):
			for j = i; j < n && isDigit(text[j]); j++ {
			}
			// one point is allowed, but only with digits after it
			if j+1 < n && text[j] == '.' && isDigit(text[j+1]) {
				for j++; j < n && isDigit(text[j]); j++ {
				}
			}
			wrap("number", text[i:j])
		case isWord(c):
			for j = i; j < n && (isWord(text[j]) || isDigit(text[j])); j++ {
			}
			if keywords[strings.ToLower(string(text[i:j]))] {
				wrap("keyword", text[i:j])
			} else {
				out.Write(text[i:j])
			}
		default:
			out.WriteByte(c)
		}
		i = j
	}
}
