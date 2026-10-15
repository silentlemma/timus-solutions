package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	classes            = 4 // houses by the parities of x and y
	candidatesPerPlace = 5 // 5n names for n places
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	var groups [classes][]string
	for i := 1; i <= candidatesPerPlace*n; i++ {
		var x, y int
		fmt.Fscan(in, &x, &y)
		c := 2*(x&1) + y&1
		groups[c] = append(groups[c], strconv.Itoa(i))
	}
	// two houses with the same parities differ by even dx and dy, so the
	// middle of their segment is a lattice point; 5n houses in 4 classes
	// leave one class with at least n of them, so the army always exists
	best := groups[0]
	for _, g := range groups {
		if len(g) > len(best) {
			best = g
		}
	}
	fmt.Println("OK")
	fmt.Println(strings.Join(best[:n], " "))
}
