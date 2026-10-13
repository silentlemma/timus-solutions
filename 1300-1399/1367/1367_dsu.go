package main

import (
	"bufio"
	"os"
	"sort"
	"strings"
)

var parent []int

func find(x int) int {
	for parent[x] != x {
		parent[x] = parent[parent[x]]
		x = parent[x]
	}
	return x
}

func union(a, b int) {
	a, b = find(a), find(b)
	if a != b {
		parent[a] = b
	}
}

type secret struct{ row, col, corner int }

const corners = 4

func main() {
	sc := bufio.NewScanner(os.Stdin)
	var pic []string
	for sc.Scan() {
		pic = append(pic, strings.TrimRight(sc.Text(), "\r"))
	}
	for len(pic) > 0 && pic[len(pic)-1] == "" {
		pic = pic[:len(pic)-1]
	}
	h, w := len(pic), 0
	for _, row := range pic {
		if len(row) > w {
			w = len(row)
		}
	}
	// walls run along the middle lines of the cells, so the four quarters
	// around a corner of the grid always meet: the corners are the places
	// an agent can be, and a cell joins some of its four corners
	side := w + 1
	parent = make([]int, (h+1)*side)
	for i := range parent {
		parent[i] = i
	}
	var secrets []secret
	for r, row := range pic {
		top, bottom := r*side, (r+1)*side
		for c := 0; c < len(row); c++ {
			switch row[c] {
			case '.':
				union(top+c, top+c+1)
				union(top+c, bottom+c)
				union(top+c, bottom+c+1)
			case '-': // keeps the upper and the lower pair apart
				union(top+c, top+c+1)
				union(bottom+c, bottom+c+1)
			case '|': // keeps the left and the right pair apart
				union(top+c, bottom+c)
				union(top+c+1, bottom+c+1)
			case '#':
				secrets = append(secrets, secret{r, c, top + c})
			}
		}
	}
	// numbered from the top, and from the right within a row
	sort.Slice(secrets, func(i, j int) bool {
		if secrets[i].row != secrets[j].row {
			return secrets[i].row < secrets[j].row
		}
		return secrets[i].col > secrets[j].col
	})
	// an agent may not pass through a secret, so two secrets are joined when
	// some corner of one shares a region with some corner of the other
	regions := make([][corners]int, len(secrets))
	for i, s := range secrets {
		v := s.corner
		regions[i] = [corners]int{find(v), find(v + 1), find(v + side), find(v + side + 1)}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, a := range regions {
		for _, b := range regions {
			shared := false
			for _, x := range a {
				for _, y := range b {
					shared = shared || x == y
				}
			}
			if shared {
				out.WriteByte('1')
			} else {
				out.WriteByte('0')
			}
		}
		out.WriteByte('\n')
	}
}
