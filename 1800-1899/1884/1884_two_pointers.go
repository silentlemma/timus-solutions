package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	maxCars        = 300
	perMetre       = 9
	laneTime       = 72
	carLength      = 5
	unitsPerSecond = 50
	intervalWidth  = laneTime + perMetre*carLength
)

func earliestStart(near, far []int) int {
	wait, i, j := 0, 0, 0
	for i < len(near) || j < len(far) {
		var start int
		if j == len(far) || i < len(near) && near[i] <= far[j] {
			start = near[i]
			i++
		} else {
			start = far[j]
			j++
		}
		if start >= wait {
			return wait
		}
		if end := start + intervalWidth; end > wait {
			wait = end
		}
	}
	return wait
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var starts [2][maxCars]int
	var counts [2]int
	for lane := range starts {
		if _, err := fmt.Fscan(input, &counts[lane]); err != nil {
			return
		}
		for i := 0; i < counts[lane]; i++ {
			var distance int
			if _, err := fmt.Fscan(input, &distance); err != nil {
				return
			}
			starts[lane][i] = perMetre*distance - (lane+1)*laneTime
		}
	}
	wait := earliestStart(starts[0][:counts[0]], starts[1][:counts[1]])
	fmt.Printf("%.6f\n", float64(wait)/unitsPerSecond)
}
