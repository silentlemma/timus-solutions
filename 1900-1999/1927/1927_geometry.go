package main

import (
	"bufio"
	"fmt"
	"os"
)

const segmentCoordinates = 4

type segment [segmentCoordinates]int64

func ordered(a, b int64) (int64, int64) {
	if a > b {
		return b, a
	}
	return a, b
}

func intersectionArea(first, second segment) float64 {
	vx, vy := first[2]-first[0], first[segmentCoordinates-1]-first[1]
	wx, wy := second[2]-second[0], second[segmentCoordinates-1]-second[1]
	determinant := vx*wy - vy*wx
	if determinant != 0 {
		if determinant < 0 {
			determinant = -determinant
		}
		return float64((vx*vx+vy*vy)*(wx*wx+wy*wy)) / float64(determinant)
	}
	low, high := ordered(vx*first[0]+vy*first[1], vx*first[2]+vy*first[segmentCoordinates-1])
	otherLow, otherHigh := ordered(
		vx*second[0]+vy*second[1], vx*second[2]+vy*second[segmentCoordinates-1],
	)
	if otherLow > low {
		low = otherLow
	}
	if otherHigh < high {
		high = otherHigh
	}
	if low < high {
		return -1
	}
	return 0
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var first, second segment
	for i := range first {
		fmt.Fscan(input, &first[i])
	}
	for i := range second {
		fmt.Fscan(input, &second[i])
	}
	fmt.Printf("%.10f\n", intersectionArea(first, second))
}
