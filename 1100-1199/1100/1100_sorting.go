package main

import (
	"bufio"
	"os"
	"strconv"
)

const most = 100

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n := next()
	// bubble sort never swaps equal scores, so teams with the same score keep
	// their input order: a counting sort by score does the same
	buckets := make([][]int32, most+1)
	for i := 0; i < n; i++ {
		team := int32(next())
		solved := next()
		buckets[solved] = append(buckets[solved], team)
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for solved := most; solved >= 0; solved-- {
		tail := " " + strconv.Itoa(solved) + "\n"
		for _, team := range buckets[solved] {
			w.WriteString(strconv.Itoa(int(team)))
			w.WriteString(tail)
		}
	}
}
