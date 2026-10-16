package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	var touches []string
	if n == 2 {
		touches = []string{"1", "1"}
	} else {
		// sweep 2..n-1 and back: the first pass catches one parity of the
		// start, the second pass the other
		for p := 2; p <= n-1; p++ {
			touches = append(touches, strconv.Itoa(p))
		}
		for p := n - 1; p >= 2; p-- {
			touches = append(touches, strconv.Itoa(p))
		}
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, len(touches))
	fmt.Fprintln(writer, strings.Join(touches, " "))
}
