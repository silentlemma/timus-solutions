package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const step = 1999

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	var text []byte
	for _, c := range data {
		if c != '\r' && c != '\n' {
			text = append(text, c)
		}
	}
	// Josephus: J(m) is zero-based from the original counting start.
	// After the first deletion, counting restarts step positions from that start.
	// Thus J(m) = (J(m - 1) + step) % m, with J(1) = 0.
	survivor := 0
	for m := 2; m <= len(text); m++ {
		survivor = (survivor + step) % m
	}
	switch text[survivor] {
	case '?':
		fmt.Println("Yes")
	case ' ':
		fmt.Println("No")
	default:
		fmt.Println("No comments")
	}
}
