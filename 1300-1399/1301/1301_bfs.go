package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	top = iota
	bottom
	north
	south
	east
	west
	sides
)

const (
	goEast = iota
	goWest
	goNorth
	goSouth
	moves
)

const size = 12

var dx = [moves]int{1, -1, 0, 0}
var dy = [moves]int{0, 0, 1, -1}

// a roll moves every face to a new side; only the side that holds the
// starting top face matters, so each roll (east, west, north, south)
// maps every side to the side it lands on
var roll = [moves][sides]int{
	{east, west, north, south, bottom, top},
	{west, east, north, south, top, bottom},
	{north, south, bottom, top, east, west},
	{south, north, top, bottom, east, west},
}

type state struct{ x, y, side int }

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() (string, bool) {
		if !in.Scan() {
			return "", false
		}
		return in.Text(), true
	}
	number := func() int {
		w, _ := next()
		v, _ := strconv.Atoi(w)
		return v
	}
	width, height := number(), number()
	a, b := number(), number()
	c, d := number(), number()
	var blocked [size][size][moves]bool
	kind := ""
	for word, ok := next(); ok; word, ok = next() {
		if word == "v" || word == "h" {
			kind = word
			continue
		}
		n, _ := strconv.Atoi(word)
		m := number()
		// a v wall stands between (n, m) and (n + 1, m), an h wall between
		// (n, m) and (n, m + 1), and each blocks the move both ways
		if kind == "v" {
			blocked[n][m][goEast], blocked[n+1][m][goWest] = true, true
		} else {
			blocked[n][m][goNorth], blocked[n][m+1][goSouth] = true, true
		}
	}
	dist := map[state]int{{a, b, top}: 0}
	queue := []state{{a, b, top}}
	for head := 0; head < len(queue); head++ {
		s := queue[head]
		if s == (state{c, d, top}) {
			fmt.Println(dist[s])
			return
		}
		for k := 0; k < moves; k++ {
			nx, ny := s.x+dx[k], s.y+dy[k]
			if nx < 1 || nx > width || ny < 1 || ny > height || blocked[s.x][s.y][k] {
				continue
			}
			next := state{nx, ny, roll[k][s.side]}
			if _, seen := dist[next]; !seen {
				dist[next] = dist[s] + 1
				queue = append(queue, next)
			}
		}
	}
	fmt.Println("No solution")
}
