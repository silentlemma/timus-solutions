package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const wall = '0'

type seed struct{ level, cell int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, sr, sc, tr, tc int
	fmt.Fscan(in, &n, &m, &sr, &sc, &tr, &tc)
	width := m + 2
	// the plan with a frame of walls, as one flat array
	var b strings.Builder
	frame := strings.Repeat(string(wall), width)
	b.WriteString(frame)
	for r := 0; r < n; r++ {
		var row string
		fmt.Fscan(in, &row)
		for len(row) < m {
			row += string(wall)
		}
		b.WriteByte(wall)
		b.WriteString(row[:m])
		b.WriteByte(wall)
	}
	b.WriteString(frame)
	grid := b.String()
	steps := make([]int, len(grid))
	seeded := make([]int, len(grid)) // the layer that last took the cell as a seed
	for i := range steps {
		steps[i], seeded[i] = -1, -1
	}
	var moves []int
	for dr := -1; dr <= 1; dr++ {
		for dc := -1; dc <= 1; dc++ {
			if dr != 0 || dc != 0 {
				moves = append(moves, dr*width+dc)
			}
		}
	}
	start, target := sr*width+sc, tr*width+tc
	// layer c holds the cells first reached after c changes of shoes, all of
	// the same kind; seeds come in sorted by the number of steps
	kind, changes := grid[start], 0
	seeds := []seed{{0, start}}
	for len(seeds) > 0 && steps[target] < 0 {
		var later []seed
		var current []int
		i, level := 0, seeds[0].level
		for (i < len(seeds) || len(current) > 0) && steps[target] < 0 {
			if len(current) == 0 && seeds[i].level > level {
				level = seeds[i].level
			}
			for ; i < len(seeds) && seeds[i].level == level; i++ {
				if cell := seeds[i].cell; steps[cell] < 0 {
					steps[cell] = level
					current = append(current, cell)
				}
			}
			var following []int
			for _, cell := range current {
				for _, move := range moves {
					near := cell + move
					if steps[near] >= 0 || grid[near] == wall {
						continue
					}
					if grid[near] == kind {
						steps[near] = level + 1
						following = append(following, near)
					} else if seeded[near] != changes {
						seeded[near] = changes
						later = append(later, seed{level + 1, near})
					}
				}
			}
			current = following
			level++
		}
		if steps[target] < 0 {
			if len(later) > 0 {
				kind = grid[later[0].cell]
			}
			changes++
			seeds = later
		}
	}
	if steps[target] < 0 {
		fmt.Println(0, 0)
	} else {
		fmt.Println(steps[target]+1, changes)
	}
}
