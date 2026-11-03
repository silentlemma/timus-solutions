package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// every sum from 1 to reach is made of the notes taken so far; a note
	// no larger than reach + 1 extends that to reach + note
	reach := 0
	for i := 0; i < n; i++ {
		var d int
		fmt.Fscan(in, &d)
		if d > reach+1 {
			break
		}
		reach += d
	}
	fmt.Println(reach + 1)
}
