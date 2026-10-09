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
	// Josephus: with m characters left, the one that stays last sits at
	// (survivor of m - 1) + step, counted from where the first deletion was
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
