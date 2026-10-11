package main

import (
	"fmt"
	"strconv"
)

const (
	none = iota
	pawn
	queen
	rook
	bishop
	knight
)

// the double steps start from these rows, counted from 0
const (
	whiteStart   = 1
	enPassantRow = 3
	// a square is packed into 5 bits per coordinate in the memo keys
	shift = 5
	// the king steps list the four straight directions before the diagonal ones
	firstDiagonal = 4
)

var (
	promotions = []int{queen, rook, bishop, knight}
	kingSteps  = [8][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
	jumps      = [8][2]int{{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}}
	n          int
	memo       = map[int64]bool{}
)

type move struct{ kind, bx, by, kx, ky int }

// option is a white move: where the pawn lands and what is left of Black's
// pawn or piece.
type option struct{ wx, wy, kind, bx, by int }

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}

func inside(x, y int) bool { return x >= 0 && x < n && y >= 0 && y < n }

// pieceMoves lists the squares the black piece can reach, ignoring the
// white pawn.
func pieceMoves(kind, bx, by, kx, ky int) [][2]int {
	var out [][2]int
	if kind == knight {
		for _, d := range jumps {
			x, y := bx+d[0], by+d[1]
			if inside(x, y) && !(x == kx && y == ky) {
				out = append(out, [2]int{x, y})
			}
		}
		return out
	}
	// the queen uses all eight rays, the rook the first four, the bishop the last four
	from, to := 0, len(kingSteps)
	if kind == bishop {
		from = firstDiagonal
	}
	if kind == rook {
		to = firstDiagonal
	}
	for _, d := range kingSteps[from:to] {
		x, y := bx+d[0], by+d[1]
		for inside(x, y) && !(x == kx && y == ky) {
			out = append(out, [2]int{x, y})
			x, y = x+d[0], y+d[1]
		}
	}
	return out
}

// blackFails tells whether White wins against every reply, Black to move.
func blackFails(wx, wy, kind, bx, by, kx, ky int) bool {
	dx, dy := abs(kx-wx), abs(ky-wy)
	if dx <= 1 && dy <= 1 {
		return false // the king takes the pawn
	}
	if kind == pawn && by-1 == wy && abs(bx-wx) == 1 {
		return false
	}
	var squares [][2]int
	if kind != none && kind != pawn {
		squares = pieceMoves(kind, bx, by, kx, ky)
		for _, s := range squares {
			if s[0] == wx && s[1] == wy {
				return false
			}
		}
	}
	var moves []move
	for _, d := range kingSteps {
		x, y := kx+d[0], ky+d[1]
		// the pawn attacks the two squares diagonally in front of it
		attacked := y == wy+1 && abs(x-wx) == 1
		if inside(x, y) && !attacked && (kind == none || !(x == bx && y == by)) {
			moves = append(moves, move{kind, bx, by, x, y})
		}
	}
	if kind == pawn {
		free := func(y int) bool { return !(bx == wx && y == wy) && !(bx == kx && y == ky) }
		if ahead := by - 1; ahead >= 0 && free(ahead) {
			if ahead == 0 {
				for _, p := range promotions {
					moves = append(moves, move{p, bx, ahead, kx, ky})
				}
			} else {
				moves = append(moves, move{pawn, bx, ahead, kx, ky})
				if by == n-2 && free(by-2) {
					moves = append(moves, move{pawn, bx, by - 2, kx, ky})
				}
			}
		}
	} else if kind != none {
		for _, s := range squares {
			moves = append(moves, move{kind, s[0], s[1], kx, ky})
		}
	}
	if len(moves) == 0 {
		return false // nothing to move: the pawn has not promoted
	}
	for _, m := range moves {
		if !whiteWins(wx, wy, m.kind, m.bx, m.by, m.kx, m.ky) {
			return false
		}
	}
	return true
}

func whiteWins(wx, wy, kind, bx, by, kx, ky int) bool {
	key := int64(kind)
	for _, v := range []int{wx, wy, bx + 1, by + 1, kx, ky} {
		key = key<<shift | int64(v)
	}
	if r, ok := memo[key]; ok {
		return r
	}
	memo[key] = false
	free := func(x, y int) bool {
		return !(x == kx && y == ky) && !(kind != none && x == bx && y == by)
	}
	var options []option
	if free(wx, wy+1) {
		options = append(options, option{wx, wy + 1, kind, bx, by})
		if wy == whiteStart && free(wx, wy+2) {
			// a black pawn beside the landing square takes it en passant
			beside := kind == pawn && by == enPassantRow && abs(bx-wx) == 1
			if !beside {
				options = append(options, option{wx, wy + 2, kind, bx, by})
			}
		}
	}
	for _, dx := range []int{-1, 1} {
		if kind != none && bx == wx+dx && by == wy+1 {
			options = append(options, option{wx + dx, wy + 1, none, -1, -1})
		}
	}
	result := false
	for _, o := range options {
		if o.wy == n-1 || blackFails(o.wx, o.wy, o.kind, o.bx, o.by, kx, ky) {
			result = true
			break
		}
	}
	memo[key] = result
	return result
}

func main() {
	var w, b, k string
	fmt.Scan(&n, &w, &b, &k)
	col := func(s string) int { return int(s[0] - 'a') }
	row := func(s string) int {
		v, _ := strconv.Atoi(s[1:])
		return v - 1
	}
	if whiteWins(col(w), row(w), pawn, col(b), row(b), col(k), row(k)) {
		fmt.Println("WHITE WINS")
	} else {
		fmt.Println("BLACK WINS")
	}
}
