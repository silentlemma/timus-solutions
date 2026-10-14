package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	free   = 6 // calls of up to six seconds cost nothing
	minute = 60
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n1, c1, n2, t, c2, n3, k int
	fmt.Fscan(in, &n1, &c1, &n2, &t, &c2, &n3, &k)
	minutes := 0
	for i := 0; i < k; i++ {
		var call string
		fmt.Fscan(in, &call)
		parts := strings.SplitN(call, ":", 2)
		mm, _ := strconv.Atoi(parts[0])
		ss, _ := strconv.Atoi(parts[1])
		if seconds := mm*minute + ss; seconds > free {
			minutes += (seconds + minute - 1) / minute // a started minute counts in full
		}
	}
	extra := minutes - t
	if extra < 0 {
		extra = 0
	}
	fmt.Printf("Basic:     %d\n", n1+c1*minutes)
	fmt.Printf("Combined:  %d\n", n2+c2*extra)
	fmt.Printf("Unlimited: %d\n", n3)
}
