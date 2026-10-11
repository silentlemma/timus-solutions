package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	in.Scan()
	names := map[string]bool{in.Text(): true}
	for in.Scan() && in.Text() != "#" {
		for _, name := range strings.SplitN(in.Text(), "-", 2) {
			names[name] = true
		}
	}
	// every other compartment must be emptied through one opened partition,
	// and the partitions of a tree towards the airlock are enough
	fmt.Println(len(names) - 1)
}
