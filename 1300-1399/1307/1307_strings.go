package main

import (
	"bufio"
	"bytes"
	"io/ioutil"
	"os"
	"runtime/debug"
	"sort"
	"strconv"
)

// pieces are common bits of English, tried along with the frequent words
// of the text
var pieces = []string{
	"\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in",
	"er", "an", "re", "on", "at", "en", "nd", "es", "or", "ou", "ha",
	"is", "it", "te", "st", "ar", "al", "le", "se", "ve", "me", "ne",
	"hi", "as", "ng", "e ", "s ", "d ", "t ", ", ", ". ", "y ", "o ",
}

const (
	line  = 17   // a table line without its piece: '    t[NNN] = "";' and a line end
	chunk = 1000 // characters of the coded text per string literal
	words = 300  // the most promising words of the text that are tried

	gcPercent = 20 // the heap may grow 20 % past the live data before a collection

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

func isLetter(ch byte) bool { return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') }

type candidate struct {
	piece    string
	estimate int
}

// better orders candidates by their estimated saving, then by the piece
func better(a, b candidate) bool {
	if a.estimate != b.estimate {
		return a.estimate > b.estimate
	}
	return a.piece < b.piece
}

func main() {
	// the memory limit is 4 MB: collect garbage early and keep one copy of the text
	debug.SetGCPercent(gcPercent)
	text, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	kept := 0
	for _, ch := range text {
		if ch != '\r' {
			text[kept] = ch
			kept++
		}
	}
	text = text[:kept]
	var used [256]bool
	for _, ch := range text {
		used[ch] = true
	}
	var free []byte
	for c := first; c <= last; c++ {
		if !used[c] && bytes.IndexByte([]byte(special), byte(c)) < 0 {
			free = append(free, byte(c))
		}
	}
	// the words of the text, with the space before them and without, kept
	// as their start alone: a word runs to the end of its letters, after
	// the space if it starts with one; sorting them groups equal ones
	word := func(at uint32) []byte {
		end := int(at)
		if text[end] == ' ' {
			end++
		}
		for end < len(text) && isLetter(text[end]) {
			end++
		}
		return text[at:end]
	}
	// scan calls visit with the start of every word of two letters or more,
	// first with the space before it if there is one
	scan := func(visit func(at int)) {
		for i := 0; i < len(text); {
			if !isLetter(text[i]) {
				i++
				continue
			}
			j := i
			for j < len(text) && isLetter(text[j]) {
				j++
			}
			if j-i >= 2 {
				if i > 0 && text[i-1] == ' ' {
					visit(i - 1)
				}
				visit(i)
			}
			i = j
		}
	}
	count := 0
	scan(func(int) { count++ })
	starts := make([]uint32, 0, count)
	scan(func(at int) { starts = append(starts, uint32(at)) })
	sort.Slice(starts, func(a, b int) bool {
		return bytes.Compare(word(starts[a]), word(starts[b])) < 0
	})
	// one group per distinct word: where it is and its estimated saving
	type group struct{ at, estimate int }
	var groups []group
	for i := 0; i < len(starts); {
		j := i
		for j < len(starts) && bytes.Equal(word(starts[i]), word(starts[j])) {
			j++
		}
		groups = append(groups, group{int(starts[i]), (j - i) * (len(word(starts[i])) - 1)})
		i = j
	}
	starts = nil
	sort.Slice(groups, func(a, b int) bool {
		if groups[a].estimate != groups[b].estimate {
			return groups[a].estimate > groups[b].estimate
		}
		return bytes.Compare(word(uint32(groups[a].at)), word(uint32(groups[b].at))) < 0
	})
	if len(groups) > words {
		groups = groups[:words]
	}
	var found []candidate
	for _, g := range groups {
		found = append(found, candidate{string(word(uint32(g.at))), g.estimate})
	}
	// a piece made only of characters of the text can never match a code
	var order []candidate
	for _, piece := range pieces {
		fits := true
		for i := 0; i < len(piece); i++ {
			fits = fits && used[piece[i]]
		}
		if fits {
			estimate := bytes.Count(text, []byte(piece)) * (writtenLength(piece) - 1)
			order = append(order, candidate{piece, estimate})
		}
	}
	for _, w := range found {
		known := false
		for k := range order {
			if order[k].piece == w.piece {
				if w.estimate > order[k].estimate {
					order[k].estimate = w.estimate
				}
				known = true
			}
		}
		if !known {
			order = append(order, w)
		}
	}
	sort.Slice(order, func(a, b int) bool { return better(order[a], order[b]) })
	type code struct {
		ch    byte
		piece string
	}
	var table []code
	for _, c := range order {
		if len(free) == 0 {
			break
		}
		p := []byte(c.piece)
		cost := writtenLength(c.piece)
		// every use saves the written length of the piece less one character
		if bytes.Count(text, p)*(cost-1) <= line+cost {
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
		table = append(table, code{free[0], c.piece})
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
