package main

import (
	"bufio"
	"fmt"
	"os"
)

type customer struct {
	product string
	wanted  int
	seen    int // the amount told at the last visit, -1 before the first
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var m int
	if _, err := fmt.Fscan(reader, &m); err != nil {
		return
	}
	stock := map[string]int{}
	for i := 0; i < m; i++ {
		var amount int
		var of, name string
		fmt.Fscan(reader, &amount, &of, &name)
		stock[name] = amount
	}
	var n int
	fmt.Fscan(reader, &n)
	line := make([]customer, 0, n)
	for i := 0; i < n; i++ {
		var amount int
		var of, name string
		fmt.Fscan(reader, &amount, &of, &name)
		line = append(line, customer{name, amount, -1})
	}
	minutes := 0
	for len(line) > 0 {
		c := line[0]
		line = line[1:]
		minutes++
		left := stock[c.product]
		if left >= c.wanted {
			stock[c.product] = left - c.wanted
		} else if left == c.seen {
			// the same rest as before the call: take it all
			stock[c.product] = 0
		} else if left > 0 {
			// let the next one forward and call home; if the next one is
			// the last of the line, it is Mark's turn
			c.seen = left
			if len(line) == 0 {
				break
			}
			rest := append([]customer{line[0], c}, line[1:]...)
			line = rest
		}
	}
	fmt.Println(minutes)
}
