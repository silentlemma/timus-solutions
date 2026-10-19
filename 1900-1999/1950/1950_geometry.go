package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	decimalScale  int64   = 1000
	decimalPlaces         = 3
	side          int64   = 10 * decimalScale
	cuts                  = 30
	gridScale     int64   = 1 << cuts
	initialArea   float64 = 50.0
)

type point struct {
	x, y int64
}

func parseCoordinate(text string) int64 {
	if strings.HasPrefix(text, "+") {
		text = text[1:]
	}
	parts := strings.SplitN(text, ".", 2)
	whole := parts[0]
	if whole == "" {
		whole = "0"
	}
	fractional := ""
	if len(parts) > 1 {
		fractional = parts[1]
	}
	fractional += strings.Repeat("0", decimalPlaces)
	integer, _ := strconv.Atoi(whole)
	digits, _ := strconv.Atoi(fractional[:decimalPlaces])
	return int64(integer)*decimalScale + int64(digits)
}

func sign(value int64) int64 {
	if value < 0 {
		return -1
	}
	if value > 0 {
		return 1
	}
	return 0
}

func opposite(first, second int64) bool {
	return (first < 0 && second > 0) || (second < 0 && first > 0)
}

func areaForSale(x, y int64) float64 {
	target := point{x * gridScale, y * gridScale}
	right, first := point{side * gridScale, 0}, point{0, 0}
	second := point{side * gridScale, side * gridScale}
	area, answer := initialArea, 0.0
	for cut := 0; cut < cuts; cut++ {
		middle := point{(first.x + second.x) / 2, (first.y + second.y) / 2}
		normalX, normalY := sign(middle.y-right.y), -sign(middle.x-right.x)
		originSide := -normalX*right.x - normalY*right.y
		targetSide := normalX*(target.x-right.x) + normalY*(target.y-right.y)
		rayRight, rayMiddle := x*right.y-y*right.x, x*middle.y-y*middle.x
		half := area / 2
		if opposite(rayRight, rayMiddle) && (opposite(originSide, targetSide) || targetSide == 0) {
			answer += half
		}
		if targetSide == 0 {
			break
		}
		firstSide := normalX*(first.x-right.x) + normalY*(first.y-right.y)
		if (targetSide > 0) == (firstSide > 0) {
			second = right
		} else {
			first = right
		}
		right = middle
		area = half
	}
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var x, y string
	fmt.Fscan(in, &x, &y)
	fmt.Printf("%.10f\n", areaForSale(parseCoordinate(x), parseCoordinate(y)))
}
