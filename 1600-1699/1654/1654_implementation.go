package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var text string
	fmt.Fscan(in, &text)
	// a letter equal to the one before it cancels that one: removing the
	// inserted pairs in any order leaves the same text
	stack := make([]byte, 0, len(text))
	for i := 0; i < len(text); i++ {
		if n := len(stack); n > 0 && stack[n-1] == text[i] {
			stack = stack[:n-1]
		} else {
			stack = append(stack, text[i])
		}
	}
	fmt.Println(string(stack))
}
