package main

import (
	"bufio"
	"fmt"
	"os"
)

const four = 4

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for {
		var m int64
		if _, err := fmt.Fscan(reader, &m); err != nil {
			break
		}
		// by the Hull-Dobell theorem the full cycles come from a - 1
		// divisible by every prime of m, and by 4 when 4 divides m, with
		// any b coprime to m; so a runs over 1, 1 + c, ..., below m
		c, rest := int64(1), m
		for p := int64(2); p*p <= rest; p++ {
			if rest%p == 0 {
				c *= p
				for rest%p == 0 {
					rest /= p
				}
			}
		}
		if rest > 1 {
			c *= rest
		}
		if m%four == 0 {
			c *= 2
		}
		fmt.Fprintln(writer, (m-c+2)/2)
	}
}
