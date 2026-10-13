package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math"
	"os"
)

const keys = 10
const half = 1 / math.Sqrt2 // each axis of a diagonal jump

// the numeric keypad: the jump of each key in steps east and north
var dxs = [keys]int64{0, -1, 0, 1, -1, 0, 1, -1, 0, 1}
var dys = [keys]int64{0, -1, -1, -1, 0, 0, 0, 1, 1, 1}

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	var times [keys]int64
	for _, c := range data {
		if c == '0' {
			break
		}
		if c > '0' && c <= '9' {
			times[c-'0']++
		}
	}
	// straight jumps add whole metres, diagonal ones 1/sqrt(2) on each axis
	var sx, sy, dx, dy int64
	for k := 0; k < keys; k++ {
		if dxs[k] != 0 && dys[k] != 0 {
			dx += dxs[k] * times[k]
			dy += dys[k] * times[k]
		} else {
			sx += dxs[k] * times[k]
			sy += dys[k] * times[k]
		}
	}
	x := float64(sx) + float64(dx)*half
	y := float64(sy) + float64(dy)*half
	fmt.Printf("%.10f %.10f\n", x, y)
}
