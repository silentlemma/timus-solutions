package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const lineCount = 3
const coordinatesPerLine = 4
const endYIndex = 3
const outputDigits = 15
const rotationCosine = 0.5

var rotationSine = math.Sqrt(3.0) / 2

type point struct{ x, y float64 }
type line [coordinatesPerLine]int64

func cross(first, second point) float64 {
	return first.x*second.y - first.y*second.x
}

func integerArea(source line, x, y int64) int64 {
	return (source[2]-source[0])*(y-source[1]) - (source[endYIndex]-source[1])*(x-source[0])
}

func absoluteInteger(value int64) int64 {
	if value < 0 {
		return -value
	}
	return value
}

func rotate(vector point, orientation float64) point {
	sine := orientation * rotationSine
	return point{rotationCosine*vector.x - sine*vector.y, sine*vector.x + rotationCosine*vector.y}
}

func equilateralPoints(lines [lineCount]line) [lineCount]point {
	first, second, third := lines[0], lines[1], lines[2]
	useBeginning := absoluteInteger(integerArea(second, first[0], first[1])) >=
		absoluteInteger(integerArea(second, first[2], first[endYIndex]))
	base := point{float64(first[2]), float64(first[endYIndex])}
	if useBeginning {
		base = point{float64(first[0]), float64(first[1])}
	}
	anchorSecond := point{float64(second[0]), float64(second[1])}
	anchorThird := point{float64(third[0]), float64(third[1])}
	directionSecond := point{float64(second[2] - second[0]), float64(second[endYIndex] - second[1])}
	directionThird := point{float64(third[2] - third[0]), float64(third[endYIndex] - third[1])}
	positive, negative := rotate(directionSecond, 1), rotate(directionSecond, -1)
	orientation, direction := 1.0, positive
	if math.Abs(cross(negative, directionThird)) > math.Abs(cross(positive, directionThird)) {
		orientation, direction = -1, negative
	}
	offset := rotate(point{anchorSecond.x - base.x, anchorSecond.y - base.y}, orientation)
	rotatedAnchor := point{base.x + offset.x, base.y + offset.y}
	delta := point{anchorThird.x - rotatedAnchor.x, anchorThird.y - rotatedAnchor.y}
	determinant := cross(direction, directionThird)
	secondParameter := cross(delta, directionThird) / determinant
	thirdParameter := cross(delta, direction) / determinant
	pointSecond := point{anchorSecond.x + secondParameter*directionSecond.x,
		anchorSecond.y + secondParameter*directionSecond.y}
	pointThird := point{anchorThird.x + thirdParameter*directionThird.x,
		anchorThird.y + thirdParameter*directionThird.y}
	return [lineCount]point{base, pointSecond, pointThird}
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var lines [lineCount]line
	for index := range lines {
		for coordinate := range lines[index] {
			fmt.Fscan(input, &lines[index][coordinate])
		}
	}
	output := bufio.NewWriter(os.Stdout)
	for _, position := range equilateralPoints(lines) {
		fmt.Fprintf(output, "%.*f %.*f\n", outputDigits, position.x, outputDigits, position.y)
	}
	output.Flush()
}
