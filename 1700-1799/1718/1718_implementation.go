package main

import (
	"bufio"
	"fmt"
	"os"
)

// test 6 was removed and new tests were added after test 7, which became
// test 6: a failure on old test 7 must now read 6, while an accepted run or
// a failure on old test 6 may change or stay as it was
const (
	removed    = 6
	renumbered = 7
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	must, any := map[string]bool{}, map[string]bool{}
	for i := 0; i < n; i++ {
		var name, verdict string
		fmt.Fscan(reader, &name, &verdict)
		switch verdict {
		case "ML", "TL", "WA":
			var test int
			fmt.Fscan(reader, &test)
			if test == renumbered {
				must[name], any[name] = true, true
			} else if test == removed {
				any[name] = true
			}
		case "AC":
			any[name] = true
		}
	}
	fmt.Println(len(must), len(any))
}
