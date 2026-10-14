package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	side    = 7
	arm     = 2 // the corners cut from the 7 x 7 square are 2 x 2
	letters = "ABCDEFG"
	classes = 3 // the residues behind the invariant
)

var (
	dr = [...]int{0, 1, 0, -1}
	dc = [...]int{1, 0, -1, 0}
)

type move struct {
	from, over, to uint64
	i, j           int
}

var (
	moves []move
	dead  = map[uint64]bool{}
	path  [][2]int
	goal  uint64
)

func onBoard(r, c int) bool {
	return r >= 0 && r < side && c >= 0 && c < side &&
		((r >= arm && r < side-arm) || (c >= arm && c < side-arm))
}

func solve(board uint64) bool {
	if board == goal {
		return true
	}
	if dead[board] {
		return false
	}
	for _, m := range moves {
		if board&m.from != 0 && board&m.over != 0 && board&m.to == 0 {
			path = append(path, [2]int{m.i, m.j})
			if solve(board ^ m.from ^ m.over ^ m.to) {
				return true
			}
			path = path[:len(path)-1]
		}
	}
	dead[board] = true
	return false
}

func main() {
	var target string
	if _, err := fmt.Scan(&target); err != nil {
		return
	}
	tc, tr := strings.IndexByte(letters, target[0]), int(target[1]-'1')
	centre := side / 2
	// A jump changes the parity of the peg count in each class of r + c
	// (mod 3), and of r - c: so the last peg sits where r and c are both
	// congruent to the centre modulo 3.
	if (tr-centre)%classes != 0 || (tc-centre)%classes != 0 || !onBoard(tr, tc) {
		fmt.Println("Impossible")
		return
	}
	// The start is symmetric, so an edge target is a quarter turn of the top
	// one: search for the top cell, which the search finds fast, then turn.
	turns := 0
	for !(tr == centre && tc == centre) && !(tr == side-1 && tc == centre) {
		tr, tc = side-1-tc, tr // a quarter turn back
		turns++
	}
	var cells [][2]int
	var index [side][side]int
	for r := 0; r < side; r++ {
		for c := 0; c < side; c++ {
			if onBoard(r, c) {
				index[r][c] = len(cells)
				cells = append(cells, [2]int{r, c})
			}
		}
	}
	// every move as (from, over, to) bits
	for _, cell := range cells {
		r, c := cell[0], cell[1]
		for d := range dr {
			r1, c1, r2, c2 := r+dr[d], c+dc[d], r+2*dr[d], c+2*dc[d]
			if onBoard(r1, c1) && onBoard(r2, c2) {
				moves = append(moves, move{1 << uint(index[r][c]), 1 << uint(index[r1][c1]),
					1 << uint(index[r2][c2]), index[r][c], index[r2][c2]})
			}
		}
	}
	full := uint64(1)<<uint(len(cells)) - 1
	start := full &^ (1 << uint(index[centre][centre]))
	goal = 1 << uint(index[tr][tc])
	solve(start)
	name := func(i int) string {
		r, c := cells[i][0], cells[i][1]
		for t := 0; t < turns; t++ {
			r, c = c, side-1-r // a quarter turn forward
		}
		return string([]byte{letters[c], byte('1' + r)})
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, p := range path {
		fmt.Fprintf(out, "%s-%s\n", name(p[0]), name(p[1]))
	}
}
