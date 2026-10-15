package main

import (
	"bufio"
	"fmt"
	"os"
)

// sameSide tells whether one side of some inscribed square passes through
// both points: a side lies on a line at distance R / sqrt(2) from the
// centre, and the disc cuts exactly the side out of that line.
func sameSide(r, x1, y1, x2, y2 int64) bool {
	if x1 == x2 && y1 == y2 {
		return 2*(x1*x1+y1*y1) >= r*r
	}
	cross := x1*y2 - y1*x2
	dx, dy := x1-x2, y1-y2
	return 2*cross*cross == r*r*(dx*dx+dy*dy)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var r, x1, y1, x2, y2 int64
		fmt.Fscan(in, &r, &x1, &y1, &x2, &y2)
		// the second point on the same, the opposite or an adjacent side:
		// turning it by 0, 180, 90 or -90 degrees brings it onto the first one's side
		ok := sameSide(r, x1, y1, x2, y2) || sameSide(r, x1, y1, -x2, -y2) ||
			sameSide(r, x1, y1, -y2, x2) || sameSide(r, x1, y1, y2, -x2)
		if ok {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
}
