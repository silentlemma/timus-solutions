package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var s string
	fmt.Fscan(in, &n, &s)
	if n%2 == 0 && strings.Count(s, "0")%2 != 0 {
		fmt.Println("NO")
		return
	}

	balance := 0
	for i := 0; i < n/2; i++ {
		// A zero can move left, so the suffix must supply at least as many zeros.
		if s[n-1-i] == '0' {
			balance++
		}
		if s[i] == '0' {
			balance--
		}
		if balance < 0 {
			fmt.Println("NO")
			return
		}
	}
	fmt.Println("YES")
}
