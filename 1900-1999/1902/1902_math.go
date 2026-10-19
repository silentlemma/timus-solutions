package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var count, duration, start int
	fmt.Fscan(in, &count, &duration, &start)
	for i := 0; i < count; i++ {
		var other int
		fmt.Fscan(in, &other)
		doubledTime := start + duration + other
		fraction := "000000"
		if doubledTime%2 != 0 {
			fraction = "500000"
		}
		fmt.Fprintf(out, "%d.%s\n", doubledTime/2, fraction)
	}
}
