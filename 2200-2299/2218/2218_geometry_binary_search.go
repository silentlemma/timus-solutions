package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

type inputReader struct {
	data []byte
	pos  int
}

func (in *inputReader) nextInt() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	sign := int64(1)
	if in.data[in.pos] == '-' {
		sign = -1
		in.pos++
	}
	value := int64(0)
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int64(in.data[in.pos]-'0')
		in.pos++
	}
	return value * sign
}

type point struct {
	first  int64
	second int64
}

type pointList []point

func (points pointList) Len() int      { return len(points) }
func (points pointList) Swap(i, j int) { points[i], points[j] = points[j], points[i] }
func (points pointList) Less(i, j int) bool {
	return points[i].first < points[j].first ||
		(points[i].first == points[j].first && points[i].second < points[j].second)
}

func lowerBound(points pointList, fixed, value int64, inclusive bool) int {
	left, right := 0, len(points)
	for left < right {
		middle := left + (right-left)/2
		p := points[middle]
		before := p.first < fixed || (p.first == fixed && p.second < value)
		if inclusive && p.first == fixed && p.second == value {
			before = true
		}
		if before {
			left = middle + 1
		} else {
			right = middle
		}
	}
	return left
}

func countSegment(points pointList, fixed, low, high int64) int {
	return lowerBound(points, fixed, high, true) - lowerBound(points, fixed, low, false)
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := inputReader{data: data}
	count := int(in.nextInt())
	byU := make(pointList, count)
	byV := make(pointList, count)
	for i := range byU {
		x, y := in.nextInt(), in.nextInt()
		byU[i] = point{x + y, x - y}
		byV[i] = point{x - y, x + y}
	}
	sort.Sort(byU)
	sort.Sort(byV)

	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	queries := int(in.nextInt())
	for query := 0; query < queries; query++ {
		x, y, distance := in.nextInt(), in.nextInt(), in.nextInt()
		u, v := x+y, x-y
		if distance == 0 {
			fmt.Fprintln(out, countSegment(byU, u, v, v))
			continue
		}

		answer := countSegment(byU, u-distance, v-distance, v+distance)
		answer += countSegment(byU, u+distance, v-distance, v+distance)
		// The other two sides exclude corners already counted above.
		answer += countSegment(byV, v-distance, u-distance+1, u+distance-1)
		answer += countSegment(byV, v+distance, u-distance+1, u+distance-1)
		fmt.Fprintln(out, answer)
	}
}
