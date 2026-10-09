package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

var words = []string{"out", "output", "puton", "in", "input", "one"}

// dialogue cuts the line greedily from its end: read backwards the words
// never start one another, so at most one word ends at each position
func dialogue(s string) bool {
	end := len(s)
	for end > 0 {
		cut := -1
		for _, w := range words {
			if strings.HasSuffix(s[:end], w) {
				cut = end - len(w)
			}
		}
		if cut < 0 {
			return false
		}
		end = cut
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	first, _ := in.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(first))
	for i := 0; i < n; i++ {
		line, _ := in.ReadString('\n')
		if dialogue(strings.TrimSpace(line)) {
			w.WriteString("YES\n")
		} else {
			w.WriteString("NO\n")
		}
	}
}
