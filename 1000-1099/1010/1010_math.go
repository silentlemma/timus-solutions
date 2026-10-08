package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const bitSize = 64

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	next := func() int64 {
		sc.Scan()
		v, _ := strconv.ParseInt(sc.Text(), 10, bitSize)
		return v
	}
	n := int(next())
	prev := next()
	// the slope of a chord is the mean of the slopes of the steps under it, so
	// the steepest valid chord joins two neighbours; take the first steepest
	best, a := int64(-1), 1
	for x := 2; x <= n; x++ {
		cur := next()
		step := cur - prev
		if step < 0 {
			step = -step
		}
		if step > best {
			best, a = step, x-1
		}
		prev = cur
	}
	fmt.Println(a, a+1)
}
