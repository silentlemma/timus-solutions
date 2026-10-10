package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// side: beacons and control points lie on the grid from 1 to side
const side = 200

type measure struct{ x, y, r int }

// numbers are the numbers in a line, whatever separates them
func numbers(line string) []int {
	var out []int
	for k := 0; k < len(line); {
		if line[k] < '0' || line[k] > '9' {
			k++
			continue
		}
		v := 0
		for ; k < len(line) && line[k] >= '0' && line[k] <= '9'; k++ {
			v = v*10 + int(line[k]-'0')
		}
		out = append(out, v)
	}
	return out
}

// ring lists the cells at distance exactly r from (x, y) in the max metric
func ring(x, y, r int) [][2]int {
	if r == 0 {
		return [][2]int{{x, y}}
	}
	var cells [][2]int
	for d := -r; d <= r; d++ {
		cells = append(cells, [2]int{x + d, y - r}, [2]int{x + d, y + r})
	}
	for d := -r + 1; d < r; d++ {
		cells = append(cells, [2]int{x - r, y + d}, [2]int{x + r, y + d})
	}
	return cells
}

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	var first []int
	for len(first) == 0 && in.Scan() {
		first = numbers(in.Text())
	}
	if len(first) == 0 {
		return
	}
	m := first[0]
	seen := map[int][]measure{}
	for i := 0; i < m && in.Scan(); {
		nums := numbers(in.Text())
		if len(nums) == 0 {
			continue
		}
		i++
		for k := 2; k+1 < len(nums); k += 2 {
			seen[nums[k]] = append(seen[nums[k]], measure{nums[0], nums[1], nums[k+1]})
		}
	}
	var ids []int
	for id := range seen {
		ids = append(ids, id)
	}
	sort.Ints(ids)
	for _, id := range ids {
		list := seen[id]
		var places [][2]int
		for _, c := range ring(list[0].x, list[0].y, list[0].r) {
			if c[0] < 1 || c[0] > side || c[1] < 1 || c[1] > side {
				continue
			}
			fits := true
			for _, q := range list {
				dx, dy := abs(c[0]-q.x), abs(c[1]-q.y)
				if dy > dx {
					dx = dy
				}
				fits = fits && dx == q.r
			}
			if fits {
				places = append(places, c)
			}
		}
		if len(places) == 1 {
			fmt.Printf("%d:%d,%d\n", id, places[0][0], places[0][1])
		} else {
			fmt.Printf("%d:UNKNOWN\n", id)
		}
	}
}
