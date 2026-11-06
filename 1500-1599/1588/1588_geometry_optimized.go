package main

import (
	"bufio"
	"math"
	"os"
	"sort"
	"strconv"
)

const (
	coordinateLimit = 10000
	directionWidth  = 2*coordinateLimit + 1
	outputSize      = 16
	decimal         = 10
)

type point struct{ x, y int }

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	cities := make([]point, nextInt(input))
	for i := range cities {
		cities[i] = point{nextInt(input), nextInt(input)}
	}
	sort.Slice(cities, func(i, j int) bool {
		return cities[i].x < cities[j].x ||
			cities[i].x == cities[j].x && cities[i].y < cities[j].y
	})
	directions := make(map[int]int, len(cities))
	total, correction := 0.0, 0.0
	for i, city := range cities {
		for j, other := range cities {
			if i == j {
				continue
			}
			dx, dy := other.x-city.x, other.y-city.y
			if j < i {
				dx, dy = -dx, -dy
			}
			step := gcd(dx, dy)
			key := dx/step*directionWidth + dy/step + coordinateLimit
			if j < i {
				// An earlier city counts this road instead.
				directions[key] = -1
			} else if distance := dx*dx + dy*dy; directions[key] >= 0 && distance > directions[key] {
				directions[key] = distance
			}
		}
		for key, distance := range directions {
			if distance > 0 {
				term := math.Sqrt(float64(distance)) - correction
				next := total + term
				correction = (next - total) - term
				total = next
			}
			delete(directions, key)
		}
	}
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], int64(math.Round(total)), decimal)
	os.Stdout.Write(append(line, '\n'))
}
