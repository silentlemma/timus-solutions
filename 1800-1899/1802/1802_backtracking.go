package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	faces = 6
	turns = 4
	axes  = 3
	word  = 64
)

type mask []uint64

var (
	n       int
	parts   [faces][][]int
	options [faces][faces][]mask // [part][face], all different
	faceOf  [faces]int           // -1 while a part is unused
	chosen  [faces]mask
)

// cellIndex is the cell at depth k under row r, column c of a face; every
// face is the bottom one turned by a rotation of the cube, so no part is
// mirrored
func cellIndex(face, r, c, k int) int {
	last := n - 1
	cells := [faces][axes]int{{k, r, c}, {last - k, last - r, c}, {r, last - k, c},
		{r, k, last - c}, {r, c, k}, {r, last - c, last - k}}
	at := cells[face]
	return (at[0]*n+at[1])*n + at[2]
}

func placement(p, face, t int) mask {
	m := make(mask, (n*n*n+word-1)/word)
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			rr, cc := r, c
			for i := 0; i < t; i++ {
				rr, cc = cc, n-1-rr
			}
			for k := 0; k < parts[p][r][c]; k++ {
				id := cellIndex(face, rr, cc, k)
				m[id/word] |= 1 << uint(id%word)
			}
		}
	}
	return m
}

func disjoint(a, b mask) bool {
	for i := range a {
		if a[i]&b[i] != 0 {
			return false
		}
	}
	return true
}

func equal(a, b mask) bool {
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func union(a, b mask) mask {
	m := make(mask, len(a))
	for i := range a {
		m[i] = a[i] | b[i]
	}
	return m
}

func solve(used mask, freeFaces int) bool {
	if freeFaces == 0 {
		return true
	}
	// fill next the face with the fewest ways left
	bestFace := -1
	var best [][2]int
	for f := 0; f < faces; f++ {
		if freeFaces>>uint(f)&1 == 0 {
			continue
		}
		var ways [][2]int
		for p := 0; p < faces; p++ {
			if faceOf[p] != -1 {
				continue
			}
			for i, m := range options[p][f] {
				if disjoint(m, used) {
					ways = append(ways, [2]int{p, i})
				}
			}
		}
		if len(ways) == 0 {
			return false
		}
		if bestFace == -1 || len(ways) < len(best) {
			bestFace, best = f, ways
		}
	}
	for _, way := range best {
		p := way[0]
		faceOf[p] = bestFace
		chosen[p] = options[p][bestFace][way[1]]
		if solve(union(used, chosen[p]), freeFaces&^(1<<uint(bestFace))) {
			return true
		}
		faceOf[p] = -1
	}
	return false
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	if _, err := fmt.Fscan(reader, &n); err != nil {
		return
	}
	var volume [faces]int
	for p := 0; p < faces; p++ {
		parts[p] = make([][]int, n)
		for r := range parts[p] {
			parts[p][r] = make([]int, n)
			for c := range parts[p][r] {
				fmt.Fscan(reader, &parts[p][r][c])
				volume[p] += parts[p][r][c]
			}
		}
	}
	for p := 0; p < faces; p++ {
		for f := 0; f < faces; f++ {
			for t := 0; t < turns; t++ {
				m := placement(p, f, t)
				seen := false
				for _, o := range options[p][f] {
					seen = seen || equal(o, m)
				}
				if !seen {
					options[p][f] = append(options[p][f], m)
				}
			}
		}
	}
	// a turn of the whole cube brings the largest part onto face 0 unturned
	anchor := 0
	for p := 1; p < faces; p++ {
		if volume[p] > volume[anchor] {
			anchor = p
		}
	}
	for p := range faceOf {
		faceOf[p] = -1
	}
	faceOf[anchor] = 0
	chosen[anchor] = placement(anchor, 0, 0)
	if !solve(chosen[anchor], (1<<faces-1)&^1) {
		fmt.Println("No")
		return
	}
	label := make([]int, n*n*n)
	for p := 0; p < faces; p++ {
		for i := range label {
			if chosen[p][i/word]>>uint(i%word)&1 == 1 {
				label[i] = p + 1
			}
		}
	}
	var out strings.Builder
	out.WriteString("Yes\n")
	for row := 0; row < n*n; row++ {
		for x := 0; x < n; x++ {
			if x > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(label[row*n+x]))
		}
		out.WriteByte('\n')
	}
	fmt.Print(out.String())
}
