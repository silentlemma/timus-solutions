package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var h, w, n int
	fmt.Fscan(reader, &h, &w, &n)
	lines, used := 1, -1
	for i := 0; i < n; i++ {
		var word string
		fmt.Fscan(reader, &word)
		// a word after another one on the line needs a space before it
		if used+1+len(word) > w {
			lines++
			used = -1
		}
		used += 1 + len(word)
	}
	fmt.Println((lines + h - 1) / h)
}
