package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// results of a position for the first player
const (
	unknown uint8 = iota
	win
	lose
	draw
)

const (
	inf     = 65535
	sides   = 4
	cellW   = 3
	moves   = 10
	pass    = 4
	suicide = 9
	none    = -1
	// a rocket state: 0 still loaded, 1 fired out of the maze, w + 2 destroyed wall w
	loaded   = 0
	fired    = 1
	wallBase = 2
)

const direction = "8624" // north, east, south, west as on a keypad
const wallChar = "-|-|"

var dr = [sides]int{-1, 0, 1, 0}
var dc = [sides]int{0, 1, 0, -1}

var (
	n, cells, walls, states, places int
	side, step                      [][sides]int
	start1, start2, chest           int
	// a place: both cells, who holds the chest (0 nobody, 1 or 2) and whose turn
	cell1, cell2, holder, turnOf []int
	valid                        []int
	resultAll                    []uint8 // by rocket states and place
	distAll                      []uint16
)

func placeID(c1, c2, h, turn int) int { return ((c1*cells+c2)*cellW+h)*2 + turn }
func slot(s1, s2, place int) int      { return (s1*states+s2)*places + place }

func wallStands(w, s1, s2 int) bool {
	return w != none && s1 != w+wallBase && s2 != w+wallBase
}

func canPass(from, d, s1, s2 int) bool {
	to := step[from][d]
	return to != none && !wallStands(side[from][d], s1, s2) &&
		!wallStands(side[to][(d+2)%sides], s1, s2)
}

type move struct {
	inside bool // to a place of the same rocket states
	to     int
	result uint8
	dist   uint16
}

// fly follows a rocket: whether it hits the other player, else the new rocket state
func fly(from, d, other, s1, s2 int) (bool, int) {
	pos := from
	for {
		if wallStands(side[pos][d], s1, s2) {
			return false, side[pos][d] + wallBase
		}
		next := step[pos][d]
		if next == none {
			return false, fired
		}
		if back := side[next][(d+2)%sides]; wallStands(back, s1, s2) {
			return false, back + wallBase
		}
		pos = next
		if pos == other {
			return true, 0
		}
	}
}

func winFor(turn int) uint8 {
	if turn == 0 {
		return win
	}
	return lose
}

func loseFor(turn int) uint8 { return win + lose - winFor(turn) }

// moveFrom gives the move with a code (M8 M6 M2 M4 M5 S8 S6 S2 S4 S5) from a
// place under the rocket states; a missing move is not inside and unknown
func moveFrom(s1, s2, place, code int) move {
	turn, h := turnOf[place], holder[place]
	cur, other := cell1[place], cell2[place]
	if turn == 1 {
		cur, other = other, cur
	}
	if code < pass {
		d, next := code, step[cur][code]
		if next == none { // out of the maze, only with the chest
			if h == turn+1 && !wallStands(side[cur][d], s1, s2) {
				return move{result: winFor(turn)}
			}
			return move{}
		}
		if next == other || !canPass(cur, d, s1, s2) {
			return move{}
		}
		nh := h
		if h == 0 && next == chest {
			nh = turn + 1
		}
		if turn == 0 {
			return move{inside: true, to: placeID(next, cell2[place], nh, 1)}
		}
		return move{inside: true, to: placeID(cell1[place], next, nh, 0)}
	}
	if code == pass {
		return move{inside: true, to: place ^ 1}
	}
	if (turn == 0 && s1 != loaded) || (turn == 1 && s2 != loaded) {
		return move{}
	}
	if code == suicide {
		return move{result: loseFor(turn)}
	}
	hit, state := fly(cur, code-pass-1, other, s1, s2)
	if hit {
		return move{result: winFor(turn)}
	}
	if turn == 0 {
		s1 = state
	} else {
		s2 = state
	}
	at := slot(s1, s2, place^1)
	return move{to: place ^ 1, result: resultAll[at], dist: distAll[at]}
}

type event struct{ d, place int }
type events []event

func (h events) Len() int            { return len(h) }
func (h events) Less(i, j int) bool  { return h[i].d < h[j].d }
func (h events) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *events) Push(x interface{}) { *h = append(*h, x.(event)) }
func (h *events) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

const sawWin, sawLose, sawDraw = 1, 2, 4

func saw(r uint8) uint8 {
	switch r {
	case win:
		return sawWin
	case lose:
		return sawLose
	case draw:
		return sawDraw
	}
	return 0
}

// buffers of one rocket state, reused: every place has at most moves moves,
// and at most maxPreds places move into it: a step from each side, with or
// without the chest picked up on the way, and a pass
const maxPreds = 2*sides + 1

var (
	moveTo                  []int32
	moveInside              []bool
	moveResult              []uint8
	moveDist                []uint16
	moveCount               []uint8
	predList                []int32
	predCount               []uint8
	res, seen               []uint8
	rest, needed, got, most []int32
	dist                    []int32
	order                   []int32
	queue                   events
)

func allocate() {
	moveTo = make([]int32, places*moves)
	moveInside = make([]bool, places*moves)
	moveResult = make([]uint8, places*moves)
	moveDist = make([]uint16, places*moves)
	moveCount = make([]uint8, places)
	predList = make([]int32, places*maxPreds)
	predCount = make([]uint8, places)
	res = make([]uint8, places)
	seen = make([]uint8, places)
	rest = make([]int32, places)
	needed = make([]int32, places)
	got = make([]int32, places)
	most = make([]int32, places)
	dist = make([]int32, places)
	order = make([]int32, 0, places)
}

func settle(place int) {
	if res[place] != unknown {
		return
	}
	good, bad, mine := lose, win, uint8(sawLose)
	if turnOf[place] == 0 {
		good, bad, mine = win, lose, sawWin
	}
	switch {
	case seen[place]&mine != 0:
		res[place] = good
	case rest[place] == 0 && seen[place]&sawDraw != 0:
		res[place] = draw
	case rest[place] == 0:
		res[place] = bad
	default:
		return
	}
	order = append(order, int32(place))
}

func solve(s1, s2 int) {
	for _, place := range valid {
		moveCount[place], predCount[place] = 0, 0
		res[place], seen[place], rest[place] = unknown, 0, 0
	}
	for _, place := range valid {
		for code := 0; code < moves; code++ {
			m := moveFrom(s1, s2, place, code)
			if !m.inside && m.result == unknown {
				continue
			}
			k := place*moves + int(moveCount[place])
			moveCount[place]++
			moveTo[k], moveInside[k], moveResult[k], moveDist[k] = int32(m.to), m.inside, m.result, m.dist
			if m.inside {
				predList[m.to*maxPreds+int(predCount[m.to])] = int32(place)
				predCount[m.to]++
				rest[place]++
			} else {
				seen[place] |= saw(m.result)
			}
		}
	}
	// the result by backward induction: a player wins as soon as one move
	// wins for her, loses when every move loses, and a cycle is a draw
	order = order[:0]
	for _, place := range valid {
		settle(place)
	}
	for head := 0; head < len(order); head++ {
		u := int(order[head])
		for k := u * maxPreds; k < u*maxPreds+int(predCount[u]); k++ {
			if p := int(predList[k]); res[p] == unknown {
				rest[p]--
				seen[p] |= saw(res[u])
				settle(p)
			}
		}
	}
	for _, place := range valid {
		if res[place] == unknown {
			res[place] = draw
		}
		dist[place] = inf
	}
	// the number of turns: the first player takes the fewest, the second the
	// most, among the moves that keep the result
	for _, kind := range []uint8{win, lose} {
		queue = queue[:0]
		for _, place := range valid {
			needed[place], got[place], most[place] = 0, 0, 0
			if res[place] != kind {
				continue
			}
			for k := place * moves; k < place*moves+int(moveCount[place]); k++ {
				inside := moveInside[k]
				if (inside && res[moveTo[k]] == kind) || (!inside && moveResult[k] == kind) {
					needed[place]++
					if !inside && moveDist[k] < inf {
						heap.Push(&queue, event{int(moveDist[k]) + 1, place})
					}
				}
			}
		}
		for queue.Len() > 0 {
			e := heap.Pop(&queue).(event)
			d, place := int32(e.d), e.place
			done := false
			if turnOf[place] == 0 {
				done = d < dist[place] && dist[place] == inf
				if d < dist[place] {
					dist[place] = d
				}
			} else {
				got[place]++
				if d > most[place] {
					most[place] = d
				}
				if got[place] == needed[place] && most[place] < dist[place] {
					dist[place] = most[place]
					done = true
				}
			}
			if done {
				for k := place * maxPreds; k < place*maxPreds+int(predCount[place]); k++ {
					if p := int(predList[k]); res[p] == kind {
						heap.Push(&queue, event{int(dist[place]) + 1, p})
					}
				}
			}
		}
	}
	for _, place := range valid {
		at := slot(s1, s2, place)
		resultAll[at] = res[place]
		distAll[at] = inf
		if res[place] != draw {
			distAll[at] = uint16(dist[place])
		}
	}
}

func strength(r uint8) int {
	switch r {
	case win:
		return 2
	case draw:
		return 1
	}
	return 0
}

func main() {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')
	n, _ = strconv.Atoi(strings.TrimSpace(line))
	cells = n * n
	board := make([][]byte, cellW*n)
	for i := range board {
		row, _ := in.ReadString('\n')
		row = strings.TrimRight(row, "\r\n")
		board[i] = []byte(row + strings.Repeat(" ", cellW*n))
	}
	side = make([][sides]int, cells)
	step = make([][sides]int, cells)
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			cell := r*n + c
			switch board[cellW*r+1][cellW*c+1] {
			case '1':
				start1 = cell
			case '2':
				start2 = cell
			case '*':
				chest = cell
			}
			// the side characters of a cell: north, east, south, west
			at := [sides]byte{board[cellW*r][cellW*c+1], board[cellW*r+1][cellW*c+2],
				board[cellW*r+2][cellW*c+1], board[cellW*r+1][cellW*c]}
			for d := 0; d < sides; d++ {
				side[cell][d] = none
				if at[d] == wallChar[d] {
					side[cell][d] = walls
					walls++
				}
				step[cell][d] = none
				if nr, nc := r+dr[d], c+dc[d]; 0 <= nr && nr < n && 0 <= nc && nc < n {
					step[cell][d] = nr*n + nc
				}
			}
		}
	}
	states = walls + wallBase
	places = cells * cells * cellW * 2
	cell1 = make([]int, places)
	cell2 = make([]int, places)
	holder = make([]int, places)
	turnOf = make([]int, places)
	for a := 0; a < cells; a++ {
		for b := 0; b < cells; b++ {
			for h := 0; h < cellW; h++ {
				for turn := 0; turn < 2; turn++ {
					place := placeID(a, b, h, turn)
					cell1[place], cell2[place], holder[place], turnOf[place] = a, b, h, turn
					if a != b {
						valid = append(valid, place)
					}
				}
			}
		}
	}
	allocate()
	resultAll = make([]uint8, states*states*places)
	distAll = make([]uint16, states*states*places)
	// a shot only uses a rocket up, so states with fewer rockets come first
	for left := 0; left <= 2; left++ {
		for s1 := 0; s1 < states; s1++ {
			for s2 := 0; s2 < states; s2++ {
				count := 0
				if s1 == loaded {
					count++
				}
				if s2 == loaded {
					count++
				}
				if count == left && !(s1 >= wallBase && s1 == s2) {
					solve(s1, s2)
				}
			}
		}
	}
	place := placeID(start1, start2, 0, 0)
	result := resultAll[slot(loaded, loaded, place)]
	if result == draw {
		fmt.Println("Draw")
		return
	}
	// the first move: the best result, then the fewest turns, then the order of codes
	best, bestResult, bestDist := none, unknown, inf
	for code := 0; code < moves; code++ {
		m := moveFrom(loaded, loaded, place, code)
		if !m.inside && m.result == unknown {
			continue
		}
		// a move leads to a table entry or ends the game at once (distance 0)
		r, later := m.result, int(m.dist)
		if m.inside {
			at := slot(loaded, loaded, m.to)
			r, later = resultAll[at], int(distAll[at])
		}
		d := later + 1
		if r == draw {
			d = 0
		} else if later == inf {
			d = inf
		}
		if best == none || strength(r) > strength(bestResult) ||
			(strength(r) == strength(bestResult) && r != draw && d < bestDist) {
			best, bestResult, bestDist = code, r, d
		}
	}
	word := "Lose"
	if result == win {
		word = "Win"
	}
	fmt.Println(word, distAll[slot(loaded, loaded, place)])
	kind, dir := byte('M'), byte('5')
	if best > pass {
		kind = 'S'
	}
	if best != pass && best != suicide {
		dir = direction[best%(pass+1)]
	}
	fmt.Printf("%c%c\n", kind, dir)
}
