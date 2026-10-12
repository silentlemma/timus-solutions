package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int64 {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return int64(v)
	}
	reach, rx, ry, lx, ly := next(), next(), next(), next(), next()
	n := next()
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := int64(0); i < n; i++ {
		x, y := next(), next()
		// inside the sector means left of the right border and right of the
		// left one, borders included; the sector is narrower than a half turn
		right, left := rx*y-ry*x, x*ly-y*lx
		inside := right >= 0 && left >= 0
		// a border's extension behind the gun is out; for a sector of zero
		// width, both borders along one ray, no other test rejects it
		behind := (right == 0 && rx*x+ry*y < 0) || (left == 0 && lx*x+ly*y < 0)
		if inside && !behind && x*x+y*y <= reach*reach {
			out.WriteString("YES\n")
		} else {
			out.WriteString("NO\n")
		}
	}
}
