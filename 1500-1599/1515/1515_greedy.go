package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	notes := make([]int, n)
	for i := range notes {
		fmt.Fscan(in, &notes[i])
	}
	sort.Ints(notes)
	// every sum from 1 to reach is made of the notes taken so far; a note
	// no larger than reach + 1 extends that to reach + note
	reach := 0
	for _, d := range notes {
		if d > reach+1 {
			break
		}
		reach += d
	}
	fmt.Println(reach + 1)
}
