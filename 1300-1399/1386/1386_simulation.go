package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const commands = 4

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n, m := next(), next()
	cells := n * m
	// goTo[k][c]: the cell reached from cell c by command k, cells numbered by rows
	goTo := make([][]int, commands)
	for k := range goTo {
		goTo[k] = make([]int, cells)
		for c := range goTo[k] {
			row := next()
			col := next()
			goTo[k][c] = (row-1)*m + (col - 1)
		}
	}
	s := next()
	// the distinct cells the player may stand on, and when each was last added
	cur := make([]int, cells)
	nxt := make([]int, 0, cells)
	mark := make([]int, cells)
	for c := range cur {
		cur[c] = c
		mark[c] = -1
	}
	for step := 0; step < s; step++ {
		to := goTo[next()-1]
		nxt = nxt[:0]
		for _, c := range cur {
			if mark[to[c]] != step {
				mark[to[c]] = step
				nxt = append(nxt, to[c])
			}
		}
		cur, nxt = nxt, cur
	}
	sort.Ints(cur)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.Itoa(len(cur)) + "\n")
	for _, c := range cur {
		out.WriteString(strconv.Itoa(c/m+1) + " " + strconv.Itoa(c%m+1) + "\n")
	}
}
