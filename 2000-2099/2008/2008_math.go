package main

import (
	"bufio"
	"fmt"
	"os"
)

const gravityNumerator int64 = 49
const gravityDenominator int64 = 5
const pointCount = 3

type point struct{ x, y int64 }

func canReach(speed, dx, dy int64) bool {
	threshold := gravityDenominator*speed*speed - gravityNumerator*dy
	return threshold >= 0 && threshold*threshold >= gravityNumerator*gravityNumerator*(dx*dx+dy*dy)
}

func solve(speed int64, head, left, right point) bool {
	jump := func(start, target point) bool {
		return canReach(speed, target.x-start.x, target.y-start.y)
	}
	return jump(left, right) && jump(right, left) && (jump(left, head) || jump(right, head))
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var speed int64
	var points [pointCount]point
	fmt.Fscan(in, &speed)
	for i := range points {
		fmt.Fscan(in, &points[i].x, &points[i].y)
	}
	if solve(speed, points[0], points[1], points[2]) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
