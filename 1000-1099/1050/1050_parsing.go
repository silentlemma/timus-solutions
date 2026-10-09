package main

import (
	"bufio"
	"io/ioutil"
	"os"
)

// what happens to a double quote
const (
	kept = iota
	opening
	closing
	dropped
)

func blank(c byte) bool { return c == ' ' || c == '\t' || c == '\r' || c == '\v' || c == '\f' }

func letter(c byte) bool { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') }

func main() {
	// the text is handled as bytes: letters above 127 are copied as they are
	s, _ := ioutil.ReadAll(os.Stdin)
	n := len(s)
	mark := make([]byte, n)
	var quotes []int
	// finish pairs the quotes of the paragraph; an unpaired last one goes away
	finish := func() {
		if len(quotes)%2 == 1 {
			mark[quotes[len(quotes)-1]] = dropped
			quotes = quotes[:len(quotes)-1]
		}
		for k, q := range quotes {
			if k%2 == 0 {
				mark[q] = opening
			} else {
				mark[q] = closing
			}
		}
		quotes = quotes[:0]
	}
	for i := 0; i < n; {
		switch {
		case s[i] == '\\':
			// \" is an umlaut; otherwise the command name is the letters after \.
			if i+1 < n && s[i+1] == '"' {
				i += 2
				continue
			}
			j := i + 1
			for j < n && letter(s[j]) {
				j++
			}
			if string(s[i+1:j]) == "par" {
				finish()
			}
			i = j
		case s[i] == '"':
			quotes = append(quotes, i)
			i++
		default:
			// a line of only whitespace that ends with a line break ends a paragraph
			if s[i] == '\n' {
				j := i + 1
				for j < n && blank(s[j]) {
					j++
				}
				if j < n && s[j] == '\n' {
					finish()
				}
			}
			i++
		}
	}
	finish()
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for i := 0; i < n; i++ {
		switch mark[i] {
		case kept:
			w.WriteByte(s[i])
		case opening:
			w.WriteString("``")
		case closing:
			w.WriteString("''")
		}
	}
}
