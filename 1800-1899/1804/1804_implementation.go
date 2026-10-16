package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const most = 30

// atLeast compares (total, away goals) pairs
func atLeast(a1, a2, b1, b2 int) bool {
	return a1 > b1 || a1 == b1 && a2 >= b2
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if !scanner.Scan() {
		return
	}
	t, _ := strconv.Atoi(strings.TrimSpace(scanner.Text()))
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for test := 0; test < t; test++ {
		scanner.Scan()
		line := scanner.Text()
		var numbers []int
		for _, word := range strings.Fields(line) {
			if v, err := strconv.Atoi(word); err == nil {
				numbers = append(numbers, v)
			}
		}
		firstHome := strings.Contains(line, " home ")
		x, y := numbers[0], numbers[1]
		lowest, highest := -1, -1
		for g := 0; g <= most; g++ {
			canPass, canFail := false, false
			for o := 0; o <= most; o++ {
				// totals first, then goals scored at the other team's stadium, and
				// when both are equal a coin decides, so both may happen
				oursAway, theirsAway := x, o
				if firstHome {
					oursAway, theirsAway = g, y
				}
				if atLeast(x+g, oursAway, y+o, theirsAway) {
					canPass = true
				}
				if atLeast(y+o, theirsAway, x+g, oursAway) {
					canFail = true
				}
			}
			if canPass && lowest == -1 {
				lowest = g
			}
			if canFail {
				highest = g
			}
		}
		fmt.Fprintln(writer, lowest, highest)
	}
}
