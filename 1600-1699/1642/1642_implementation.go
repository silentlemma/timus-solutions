package main

import "fmt"

const far = 2000 // beyond every coordinate

func main() {
	var n, x int
	if _, err := fmt.Scan(&n, &x); err != nil {
		return
	}
	// the nearest obstacles on both sides; walking away from the exit is
	// promised to meet one, so the one needed below always exists
	left, right := -far, far
	for i := 0; i < n; i++ {
		var w int
		fmt.Scan(&w)
		if w < 0 && w > left {
			left = w
		}
		if w > 0 && w < right {
			right = w
		}
	}
	switch {
	case x < left || x > right:
		fmt.Println("Impossible") // an obstacle stands between the start and the exit
	case x > 0:
		fmt.Println(x, -2*left+x)
	default:
		fmt.Println(2*right-x, -x)
	}
}
