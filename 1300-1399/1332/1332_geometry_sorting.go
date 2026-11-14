package main

import (
	"bufio"
	"math"
	"os"
	"sort"
	"strconv"
)

const (
	fullTurn = 2 * math.Pi
	eps      = 1e-12
	decimal  = 10
)

type point struct{ x, y int }

func next(input *bufio.Reader) int {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	negative := ch == '-'
	if negative {
		ch, err = input.ReadByte()
	}
	value := 0
	for err == nil && ch >= '0' && ch <= '9' {
		value = decimal*value + int(ch-'0')
		ch, err = input.ReadByte()
	}
	if negative {
		return -value
	}
	return value
}

func normalize(angle float64) float64 {
	if angle < 0 {
		return angle + fullTurn
	}
	return angle
}

func mostCities(cities []point, reach int) int {
	if reach < 0 || len(cities) == 0 {
		return 0
	}
	if reach == 0 {
		return 1
	}
	diameter := 2 * reach
	limit := diameter * diameter
	starts := make([]float64, 0, len(cities)-1)
	ends := make([]float64, 0, len(cities)-1)
	best := 1
	for _, anchor := range cities {
		starts, ends = starts[:0], ends[:0]
		active := 1
		for _, city := range cities {
			dx, dy := city.x-anchor.x, city.y-anchor.y
			squared := dx*dx + dy*dy
			if squared == 0 || squared > limit {
				continue
			}
			direction := math.Atan2(float64(dy), float64(dx))
			halfWidth := math.Acos(math.Sqrt(float64(squared)) / float64(diameter))
			start := normalize(direction - halfWidth - eps)
			end := normalize(direction + halfWidth + eps)
			if start > end {
				active++
			}
			starts = append(starts, start)
			ends = append(ends, end)
		}
		sort.Float64s(starts)
		sort.Float64s(ends)
		if active > best {
			best = active
		}
		end := 0
		for _, start := range starts {
			// Both endpoints count. Remove only intervals that ended earlier.
			for end < len(ends) && ends[end] < start {
				active--
				end++
			}
			active++
			if active > best {
				best = active
			}
		}
		if best == len(cities) {
			break
		}
	}
	return best
}

func main() {
	input := bufio.NewReader(os.Stdin)
	cities := make([]point, next(input))
	for i := range cities {
		cities[i] = point{next(input), next(input)}
	}
	reach := next(input) - next(input)
	os.Stdout.WriteString(strconv.Itoa(mostCities(cities, reach)) + "\n")
}
