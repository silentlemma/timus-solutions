package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	alice = 1
	draw  = 0
	bob   = -1
	none  = 2 // the strip still shows both colours
)

func winner(top, bottom string) int {
	for _, colour := range []string{"A", "B"} {
		if strings.Count(top, colour) == len(top) && strings.Count(bottom, colour) == len(bottom) {
			if colour == "A" {
				return alice
			}
			return bob
		}
	}
	return none
}

func reversed(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}

// play is the result of optimal play from this strip with this player to move
func play(top, bottom string, aliceMoves bool) int {
	n := len(top)
	if n%2 == 1 {
		return draw
	}
	half := n / 2
	// folding brings the right half over or under the left one; the faces that
	// end up inside are hidden
	folds := [][2]string{{top[:half], reversed(top[half:])}, {reversed(bottom[half:]), bottom[:half]}}
	best := none
	goal := bob
	if aliceMoves {
		goal = alice
	}
	for _, f := range folds {
		result := winner(f[0], f[1])
		if result == none {
			result = play(f[0], f[1], !aliceMoves)
		}
		if best == none || (aliceMoves && result > best) || (!aliceMoves && result < best) {
			best = result
		}
		if best == goal {
			break
		}
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var top, bottom string
	fmt.Fscan(in, &n, &top, &bottom)
	switch play(top, bottom, true) {
	case alice:
		fmt.Println("Alice")
	case bob:
		fmt.Println("Bob")
	default:
		fmt.Println("Draw")
	}
}
