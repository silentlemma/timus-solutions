package main

import "fmt"

// results, better for white upwards
const (
	black = iota
	draw
	white
)

const size = 8
const second = 6 // the black pawn may move two squares from rank 7

var diagonals = [][2]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}

// memo[turn][bf][br][pf][pr]: the result plus one, 0 when unknown
var memo [2][size][size][size][size]int

func inside(f, r int) bool { return f >= 0 && f < size && r >= 0 && r < size }

// sees: can the bishop reach square (qf, qr) on an otherwise empty board?
func sees(bf, br, qf, qr int) bool {
	for _, d := range diagonals {
		for f, r := bf+d[0], br+d[1]; inside(f, r); f, r = f+d[0], r+d[1] {
			if f == qf && r == qr {
				return true
			}
		}
	}
	return false
}

func whiteMove(bf, br, pf, pr int) int {
	if m := memo[0][bf][br][pf][pr]; m > 0 {
		return m - 1
	}
	best := black
	for _, d := range diagonals {
		for f, r := bf+d[0], br+d[1]; inside(f, r); f, r = f+d[0], r+d[1] {
			if f == pf && r == pr {
				best = white // the bishop takes the pawn
				break
			}
			if v := blackMove(f, r, pf, pr); v > best {
				best = v
			}
		}
	}
	memo[0][bf][br][pf][pr] = best + 1
	return best
}

func blackMove(bf, br, pf, pr int) int {
	if m := memo[1][bf][br][pf][pr]; m > 0 {
		return m - 1
	}
	best := white + 1 // no move yet
	if br == pr-1 && (bf == pf-1 || bf == pf+1) {
		best = black // the pawn takes the bishop and cannot be stopped
	}
	consider := func(v int) {
		if v < best {
			best = v
		}
	}
	if !(bf == pf && br == pr-1) {
		if pr-1 == 0 {
			// a queen: white wins only by taking it at once
			if sees(bf, br, pf, 0) {
				consider(white)
			} else {
				consider(black)
			}
		} else {
			consider(whiteMove(bf, br, pf, pr-1))
			if pr == second && !(bf == pf && br == pr-2) {
				consider(whiteMove(bf, br, pf, pr-2))
			}
		}
	}
	if best > white {
		best = draw // a blocked pawn is a draw
	}
	memo[1][bf][br][pf][pr] = best + 1
	return best
}

func main() {
	var bishop, pawn string
	fmt.Scan(&bishop, &pawn)
	result := whiteMove(int(bishop[0]-'a'), int(bishop[1]-'1'), int(pawn[0]-'a'), int(pawn[1]-'1'))
	fmt.Println([]string{"BLACK", "DRAW", "WHITE"}[result])
}
