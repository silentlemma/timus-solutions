package main

import "fmt"

const (
	side  = 3
	cubes = side * side * side
	ways  = 6
	names = "RLFBUD"
	right = 0 // the index of R
	up    = 4 // the index of U
)

// the six directions; cells are numbered x * 9 + y * 3 + z
var (
	dx   = [ways]int{1, -1, 0, 0, 0, 0}
	dy   = [ways]int{0, 0, 1, -1, 0, 0}
	dz   = [ways]int{0, 0, 0, 0, 1, -1}
	axis = [ways]int{0, 0, 1, 1, 2, 2}
)

var (
	snake  string
	answer []byte
	near   [cubes][ways]int
	used   [cubes]bool
)

func cellOf(x, y, z int) int {
	if x < 0 || x >= side || y < 0 || y >= side || z < 0 || z >= side {
		return -1
	}
	return (x*side+y)*side + z
}

// connected checks that the free cells stay one piece for the rest of the snake
func connected(left int) bool {
	start := 0
	for start < cubes && used[start] {
		start++
	}
	if start == cubes {
		return true
	}
	var seen [cubes]bool
	stack := []int{start}
	seen[start] = true
	count := 0
	for len(stack) > 0 {
		at := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		count++
		for _, next := range near[at] {
			if next >= 0 && !used[next] && !seen[next] {
				seen[next] = true
				stack = append(stack, next)
			}
		}
	}
	return count == left
}

// fold places cube k + 1 after cube k, which sits at cell at
func fold(k, at, way int) bool {
	if k == cubes-1 {
		return true
	}
	for d := 0; d < ways; d++ {
		// a straight cube keeps the direction, a turning one changes axis
		if snake[k] == 'F' && d != way || snake[k] == 'T' && axis[d] == axis[way] {
			continue
		}
		next := near[at][d]
		if next < 0 || used[next] {
			continue
		}
		used[next] = true
		answer = append(answer, names[d])
		if connected(cubes-2-k) && fold(k+1, next, d) {
			return true
		}
		answer = answer[:len(answer)-1]
		used[next] = false
	}
	return false
}

func main() {
	fmt.Scan(&snake)
	for x := 0; x < side; x++ {
		for y := 0; y < side; y++ {
			for z := 0; z < side; z++ {
				for d := 0; d < ways; d++ {
					near[cellOf(x, y, z)][d] = cellOf(x+dx[d], y+dy[d], z+dz[d])
				}
			}
		}
	}
	// the cube colours 14 cells one way and 13 the other, and the snake
	// alternates, so it starts on the larger colour: a corner or the centre
	// of a face; up to symmetry that leaves three first moves
	roots := [][2]int{{cellOf(0, 0, 0), right}, {cellOf(1, 1, 0), up}, {cellOf(1, 1, 0), right}}
	for _, root := range roots {
		start, d := root[0], root[1]
		next := near[start][d]
		used = [cubes]bool{}
		used[start], used[next] = true, true
		answer = []byte{names[d]}
		if connected(cubes-2) && fold(1, next, d) {
			fmt.Println(string(answer))
			return
		}
	}
	fmt.Println("IMPOSSIBLE")
}
