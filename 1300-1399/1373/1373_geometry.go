package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const stroke = 4 // numbers per stroke

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	var nums []int64
	for sc.Scan() {
		v, _ := strconv.Atoi(sc.Text())
		nums = append(nums, int64(v))
	}
	var lowX, highX, lowY, highY int64
	for i := 0; i+stroke <= len(nums); i += stroke {
		ax, ay, bx, by := nums[i], nums[i+1], nums[i+2], nums[i+stroke-1]
		dx, dy := bx-ax, by-ay
		// go (p, q), then turn clockwise and go (q, -p): p + q = dx and
		// q - p = dy give the corner a + ((dx - dy) / 2, (dx + dy) / 2), and
		// doubled coordinates keep the halves whole
		xs := []int64{2 * ax, 2 * bx, 2*ax + dx - dy}
		ys := []int64{2 * ay, 2 * by, 2*ay + dx + dy}
		if i == 0 {
			lowX, highX, lowY, highY = xs[0], xs[0], ys[0], ys[0]
		}
		for _, x := range xs {
			if x < lowX {
				lowX = x
			}
			if x > highX {
				highX = x
			}
		}
		for _, y := range ys {
			if y < lowY {
				lowY = y
			}
			if y > highY {
				highY = y
			}
		}
	}
	fmt.Printf("%.4f %.4f\n", float64(highX-lowX)/2, float64(highY-lowY)/2)
}
