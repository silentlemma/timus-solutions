package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// brick holds a brick and everything it carries: its ends, the total
// weight (lengths) and twice its moment about 0, R^2 - L^2 per brick
type brick struct{ left, right, weight, moment int64 }

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int64 {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return int64(v)
	}
	layers := int(next())
	var above []brick
	for layer := 0; layer < layers; layer++ {
		k := int(next())
		bricks := make([]brick, k)
		for i := range bricks {
			l, r := next(), next()
			bricks[i] = brick{l, r, r - l, r*r - l*l}
		}
		// each brick above rests on the one brick below that it overlaps, and
		// the centre of all it carries must lie strictly inside the overlap, a test
		// that the doubled moment keeps in whole numbers
		j := 0
		for _, a := range above {
			for j < len(bricks) && bricks[j].right <= a.left {
				j++
			}
			if j == len(bricks) || bricks[j].left >= a.right {
				fmt.Println("No")
				return
			}
			lo, hi := a.left, a.right
			if bricks[j].left > lo {
				lo = bricks[j].left
			}
			if bricks[j].right < hi {
				hi = bricks[j].right
			}
			if !(2*lo*a.weight < a.moment && a.moment < 2*hi*a.weight) {
				fmt.Println("No")
				return
			}
			bricks[j].weight += a.weight
			bricks[j].moment += a.moment
		}
		above = bricks
	}
	fmt.Println("Yes")
}
