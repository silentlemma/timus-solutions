package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

var scanner = bufio.NewScanner(os.Stdin)

func description() (int, string) {
	scanner.Scan()
	words := strings.Fields(scanner.Text())
	amount, _ := strconv.Atoi(words[0])
	return amount, words[2]
}

type customer struct{ product, wanted, seen int }

func main() {
	scanner.Scan()
	m, _ := strconv.Atoi(scanner.Text())
	ids := make(map[string]int, m)
	stock := make([]int, m+1)
	for id := 1; id <= m; id++ {
		amount, name := description()
		ids[name] = id
		stock[id] = amount
	}
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	line := make([]customer, n)
	for i := range line {
		amount, name := description()
		line[i] = customer{ids[name], amount, -1}
	}
	front, minutes := 0, 0
	for front < n {
		c := line[front]
		left := stock[c.product]
		minutes++
		if left >= c.wanted {
			stock[c.product] = left - c.wanted
		} else if left == c.seen {
			stock[c.product] = 0
		} else if left > 0 {
			line[front].seen = left
			if front+1 == n {
				break
			}
			line[front], line[front+1] = line[front+1], line[front]
			continue
		}
		front++
	}
	os.Stdout.WriteString(strconv.Itoa(minutes) + "\n")
}
