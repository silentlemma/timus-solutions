package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func isLetter(c byte) bool { return c >= 'a' && c <= 'z' }

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	lines := strings.Split(strings.ReplaceAll(string(data), "\r", ""), "\n")
	known := map[string]bool{}
	stop := 0
	for stop < len(lines) && strings.TrimSpace(lines[stop]) != "#" {
		if w := strings.TrimSpace(lines[stop]); w != "" {
			known[w] = true
		}
		stop++
	}
	errors := 0
	fix := func(word string) string {
		if known[word] {
			return word
		}
		// only a single wrong letter is corrected, never a missing or extra one
		for d := range known {
			if len(d) != len(word) {
				continue
			}
			diff := 0
			for i := 0; i < len(d); i++ {
				if d[i] != word[i] {
					diff++
				}
			}
			if diff == 1 {
				errors++
				return d
			}
		}
		return word
	}
	text := strings.Join(lines[stop+1:], "\n")
	if !strings.HasSuffix(text, "\n") {
		text += "\n"
	}
	var out strings.Builder
	for i := 0; i < len(text); {
		if !isLetter(text[i]) {
			out.WriteByte(text[i])
			i++
			continue
		}
		j := i
		for j < len(text) && isLetter(text[j]) {
			j++
		}
		out.WriteString(fix(text[i:j]))
		i = j
	}
	fmt.Print(out.String())
	fmt.Println(errors)
}
