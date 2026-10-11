package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int64 {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return int64(v)
	}
	n := int(next())
	// twice the signed area by the shoelace formula: positive when the
	// runner goes counterclockwise, and the rope winds the same way
	x0, y0 := next(), next()
	px, py := x0, y0
	var twice int64
	for i := 1; i < n; i++ {
		x, y := next(), next()
		twice += px*y - x*py
		px, py = x, y
	}
	twice += px*y0 - x0*py
	if twice > 0 {
		fmt.Println("ccw")
	} else {
		fmt.Println("cw")
	}
}
