package main

import (
	"bufio"
	"fmt"
	"os"
)

const window = 10 // digits seen in the window

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	digits := make([]string, n)
	for i := range digits {
		fmt.Fscan(in, &digits[i])
	}
	// each click moves the window one digit on, around the wheel
	out := ""
	for i := 0; i < window; i++ {
		out += digits[(m+i)%n]
	}
	fmt.Println(out)
}
