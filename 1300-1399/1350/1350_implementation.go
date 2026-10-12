package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	word := func() string {
		sc.Scan()
		return sc.Text()
	}
	number := func() int {
		v, _ := strconv.Atoi(word())
		return v
	}
	readSet := func() map[string]bool {
		items := map[string]bool{}
		for c := number(); c > 0; c-- {
			items[word()] = true
		}
		return items
	}
	menu := readSet()
	k := number()
	blocks := make([]map[string]bool, k+1)
	for i := range blocks {
		blocks[i] = readSet()
	}
	m := number()
	// the first student was fine, so the meal is m products of the rest
	var safe []string
	for p := range menu {
		if !blocks[0][p] {
			safe = append(safe, p)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, danger := range blocks[1:] {
		risky := 0
		for _, p := range safe {
			if danger[p] {
				risky++
			}
		}
		switch {
		case m == 0 || risky == 0:
			fmt.Fprintln(out, "YES")
		case len(safe)-risky < m:
			fmt.Fprintln(out, "NO") // every possible meal holds a dangerous product
		default:
			fmt.Fprintln(out, "MAYBE")
		}
	}
}
