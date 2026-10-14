package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	words := make([]string, n)
	for i := range words {
		fmt.Fscan(in, &words[i])
	}
	var letter string
	fmt.Fscan(in, &letter)
	// the dictionary order is kept, repeated entries are printed every time
	for _, w := range words {
		if w[0] == letter[0] {
			fmt.Fprintln(out, w)
		}
	}
}
