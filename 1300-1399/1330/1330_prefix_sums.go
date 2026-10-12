package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		if !sc.Scan() {
			return 0
		}
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n := next()
	// before[i] is the sum of the first i readings
	before := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		before[i] = before[i-1] + int64(next())
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for q := next(); q > 0; q-- {
		i, j := next(), next()
		out.WriteString(strconv.FormatInt(before[j]-before[i-1], 10))
		out.WriteByte('\n')
	}
}
