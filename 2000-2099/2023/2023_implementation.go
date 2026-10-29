package main

import (
	"bufio"
	"fmt"
	"os"
)

// the three cabinets from left to right, with the names from the statement
var cabinets = [3][9]string{
	{"Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"},
	{"Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"},
	{"Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"},
}

func main() {
	cabinet := map[string]int{}
	for i, names := range cabinets {
		for _, name := range names {
			cabinet[name] = i
		}
	}
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	position, steps := 0, 0
	for k := 0; k < n; k++ {
		var name string
		fmt.Fscan(in, &name)
		target := cabinet[name]
		if target > position {
			steps += target - position
		} else {
			steps += position - target
		}
		position = target
	}
	fmt.Println(steps)
}
