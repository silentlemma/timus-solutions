package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type point struct{ x, y int }

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n := next()
	var minX, maxX, minY, maxY, minS, maxS, minD, maxD int
	for i := 0; i < n; i++ {
		x, y := next(), next()
		if i == 0 {
			minX, maxX, minY, maxY = x, x, y, y
			minS, maxS, minD, maxD = x+y, x+y, x-y, x-y
			continue
		}
		minX, maxX = min(minX, x), max(maxX, x)
		minY, maxY = min(minY, y), max(maxY, y)
		minS, maxS = min(minS, x+y), max(maxS, x+y)
		minD, maxD = min(minD, x-y), max(maxD, x-y)
	}
	// the hull is cut out by eight lines, x, y, x + y and x - y each at
	// their extremes; going counterclockwise from the bottom edge, every
	// corner joins an axis line to a diagonal one
	corners := []point{
		{minS - minY, minY}, {maxD + minY, minY}, {maxX, maxX - maxD}, {maxX, maxS - maxX},
		{maxS - maxY, maxY}, {minD + maxY, maxY}, {minX, minX - minD}, {minX, minS - minX},
	}
	var hull []point
	for _, p := range corners {
		if len(hull) == 0 || hull[len(hull)-1] != p {
			hull = append(hull, p)
		}
	}
	for len(hull) > 1 && hull[0] == hull[len(hull)-1] {
		hull = hull[:len(hull)-1]
	}
	// the sides left all point in different directions, so no corner is in
	// the middle of a straight side
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, p := range hull {
		fmt.Fprintln(out, p.x, p.y)
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
