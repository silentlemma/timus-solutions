package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')
	text := strings.TrimRight(line, "\r\n")
	n := len(text)
	out := make([]byte, n)
	// the encoded text lists the middle of a range, then its left part,
	// then its right part: replay that order and put each letter back
	stack := [][2]int{{0, n - 1}}
	at := 0
	for len(stack) > 0 {
		lo, hi := stack[len(stack)-1][0], stack[len(stack)-1][1]
		stack = stack[:len(stack)-1]
		if lo > hi {
			continue
		}
		mid := (lo + hi) / 2
		out[mid] = text[at]
		at++
		stack = append(stack, [2]int{mid + 1, hi}, [2]int{lo, mid - 1})
	}
	fmt.Println(string(out))
}
