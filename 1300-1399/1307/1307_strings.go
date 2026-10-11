package main

import (
	"bufio"
	"bytes"
	"io/ioutil"
	"os"
	"strconv"
)

// pieces are common bits of English, tried in this order; each one that
// pays off gets a printable character the text never uses
var pieces = []string{
	"\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in",
	"er", "an", "re", "on", "at", "en", "nd", "es", "or", "ou", "ha",
	"is", "it", "te", "st", "ar", "al", "le", "se", "ve", "me", "ne",
	"hi", "as", "ng", "e ", "s ", "d ", "t ", ", ", ". ", "y ", "o ",
}

const (
	entry = 24   // the size of one table line, so a piece must save more than this
	chunk = 1000 // characters of the coded text per string literal

	first   = 33      // the first printable character that may become a code
	last    = 126     // and the last one
	special = "\"\\?" // need a backslash inside a C string
)

// writeLiteral writes the text as it looks inside a C string literal
func writeLiteral(w *bufio.Writer, text []byte) {
	for _, ch := range text {
		if ch == '\n' {
			w.WriteString("\\n")
			continue
		}
		if bytes.IndexByte([]byte(special), ch) >= 0 {
			w.WriteByte('\\')
		}
		w.WriteByte(ch)
	}
}

func writtenLength(piece string) int {
	n := 0
	for i := 0; i < len(piece); i++ {
		n++
		if piece[i] == '\n' || bytes.IndexByte([]byte(special), piece[i]) >= 0 {
			n++
		}
	}
	return n
}

func main() {
	raw, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	text := bytes.ReplaceAll(raw, []byte("\r"), nil)
	var free []byte
	for c := first; c <= last; c++ {
		if bytes.IndexByte(text, byte(c)) < 0 && bytes.IndexByte([]byte(special), byte(c)) < 0 {
			free = append(free, byte(c))
		}
	}
	type code struct {
		ch    byte
		piece string
	}
	var table []code
	for _, piece := range pieces {
		if len(free) == 0 {
			break
		}
		p := []byte(piece)
		// every use saves the written length of the piece less one character
		if bytes.Count(text, p)*(writtenLength(piece)-1) <= entry {
			continue
		}
		// replace in place, left to right: the text only gets shorter
		write := 0
		for read := 0; read < len(text); {
			if bytes.HasPrefix(text[read:], p) {
				text[write] = free[0]
				read += len(p)
			} else {
				text[write] = text[read]
				read++
			}
			write++
		}
		text = text[:write]
		table = append(table, code{free[0], piece})
		free = free[1:]
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.WriteString("//CPP\n#include <cstdio>\nconst char *d[] = {\n")
	for i := 0; i < len(text); i += chunk {
		end := i + chunk
		if end > len(text) {
			end = len(text)
		}
		w.WriteByte('"')
		writeLiteral(w, text[i:end])
		w.WriteString("\",\n")
	}
	w.WriteString("0};\nint main() {\n    const char *t[256] = {0};\n")
	for _, e := range table {
		w.WriteString("    t[" + strconv.Itoa(int(e.ch)) + "] = \"")
		writeLiteral(w, []byte(e.piece))
		w.WriteString("\";\n")
	}
	w.WriteString("    for (int k = 0; d[k]; k++)\n")
	w.WriteString("        for (const char *p = d[k]; *p; p++)\n")
	w.WriteString("            if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);\n")
	w.WriteString("            else putchar(*p);\n")
	w.WriteString("    return 0;\n}\n")
}
