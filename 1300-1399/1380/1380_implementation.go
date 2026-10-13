package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	size   = 8
	pawn   = 1
	knight = 2
	bishop = 3
	rook   = 4
	queen  = 5
	king   = 6
	toFile = 3 // a move reads like e2-e4
	toRank = 4
)

// board[r][f]: row r is rank r + 1, column f is file a + f
var board [size][size]int

func inside(f, r int) bool { return 0 <= f && f < size && 0 <= r && r < size }

func sign(x int) int {
	switch {
	case x > 0:
		return 1
	case x < 0:
		return -1
	}
	return 0
}

func abs(x int) int { return x * sign(x) }

// reaches: can the piece on (f, r) move to (tf, tr), ignoring checks?
func reaches(f, r, tf, tr int) bool {
	piece, target := board[r][f], board[tr][tf]
	side, kind := sign(piece), abs(piece)
	df, dr := tf-f, tr-r
	if (df == 0 && dr == 0) || target*side > 0 {
		return false
	}
	switch kind {
	case pawn:
		home := 1 // a pawn may step two squares from here
		if side < 0 {
			home = size - 2
		}
		if df == 0 && target == 0 {
			return dr == side || (dr == 2*side && r == home && board[r+side][f] == 0)
		}
		return abs(df) == 1 && dr == side && target*side < 0
	case knight:
		return abs(df*dr) == 2
	case king:
		return abs(df) <= 1 && abs(dr) <= 1
	}
	straight, diagonal := df == 0 || dr == 0, abs(df) == abs(dr)
	if !((kind == bishop && diagonal) || (kind == rook && straight) ||
		(kind == queen && (straight || diagonal))) {
		return false
	}
	sf, sr := sign(df), sign(dr)
	for f, r = f+sf, r+sr; f != tf || r != tr; f, r = f+sf, r+sr {
		if board[r][f] != 0 {
			return false
		}
	}
	return true
}

// inCheck: is any king of this side attacked?
func inCheck(side int) bool {
	for kr := 0; kr < size; kr++ {
		for kf := 0; kf < size; kf++ {
			if board[kr][kf] != king*side {
				continue
			}
			for r := 0; r < size; r++ {
				for f := 0; f < size; f++ {
					if board[r][f]*side < 0 && reaches(f, r, kf, kr) {
						return true
					}
				}
			}
		}
	}
	return false
}

// legal makes the move if it is legal and returns the piece it took.
func legal(side, f, r, tf, tr int) (int, bool) {
	if !inside(f, r) || !inside(tf, tr) || board[r][f]*side <= 0 || !reaches(f, r, tf, tr) {
		return 0, false
	}
	taken := board[tr][tf]
	board[tr][tf], board[r][f] = board[r][f], 0
	if inCheck(side) {
		board[r][f], board[tr][tf] = board[tr][tf], taken
		return 0, false
	}
	return taken, true
}

func hasMove(side int) bool {
	for r := 0; r < size; r++ {
		for f := 0; f < size; f++ {
			if board[r][f]*side <= 0 {
				continue
			}
			for tr := 0; tr < size; tr++ {
				for tf := 0; tf < size; tf++ {
					if taken, ok := legal(side, f, r, tf, tr); ok {
						board[r][f], board[tr][tf] = board[tr][tf], taken
						return true
					}
				}
			}
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	for r := size - 1; r >= 0; r-- {
		for f := 0; f < size; f++ {
			fmt.Fscan(in, &board[r][f])
		}
	}
	var count int
	var who string
	fmt.Fscan(in, &count, &who)
	side := 1
	if who != "White" {
		side = -1
	}
	var out []string
	for i := 0; i < count; i++ {
		var move string
		fmt.Fscan(in, &move)
		f, r := int(move[0]-'a'), int(move[1]-'1')
		tf, tr := int(move[toFile]-'a'), int(move[toRank]-'1')
		if _, ok := legal(side, f, r, tf, tr); !ok {
			out = append(out, "Incorrect")
			break
		}
		side = -side
		check, free := inCheck(side), hasMove(side)
		switch {
		case !free && check:
			out = append(out, "Mate")
		case !free:
			out = append(out, "Draw")
		case check:
			out = append(out, "Check")
		default:
			out = append(out, "Correct")
		}
		if !free {
			break
		}
	}
	out = append(out, "")
	for r := size - 1; r >= 0; r-- {
		cells := make([]string, size)
		for f := range cells {
			cells[f] = strconv.Itoa(board[r][f])
		}
		out = append(out, strings.Join(cells, " "))
	}
	fmt.Println(strings.Join(out, "\n"))
}
