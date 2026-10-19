package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const orientations = 4
const initialQueueCapacity = 1024

type point struct{ row, column int }
type transition struct {
	player, change, offset int
	mask                   byte
}
type intDeque struct {
	values     []int
	head, size int
}

func (q *intDeque) ensureSpace() {
	if q.size < len(q.values) {
		return
	}
	next := make([]int, len(q.values)*2)
	for index := 0; index < q.size; index++ {
		next[index] = q.values[(q.head+index)&(len(q.values)-1)]
	}
	q.values, q.head = next, 0
}
func (q *intDeque) addFirst(value int) {
	q.ensureSpace()
	q.head = (q.head - 1) & (len(q.values) - 1)
	q.values[q.head] = value
	q.size++
}
func (q *intDeque) addLast(value int) {
	q.ensureSpace()
	q.values[(q.head+q.size)&(len(q.values)-1)] = value
	q.size++
}
func (q *intDeque) removeFirst() int {
	value := q.values[q.head]
	q.head = (q.head + 1) & (len(q.values) - 1)
	q.size--
	return value
}

func minimumPassages(rows, columns int, scheme []string) int {
	height, width := rows+2, columns+2
	size := height * width
	outside := make([]bool, size)
	masks := make([]byte, size)
	moves := []point{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
	offsets := []int{-width, 1, width, -1}
	for position := 0; position < size; position++ {
		r, c := position/width, position%width
		outside[position] = r == 0 || r == height-1 || c == 0 || c == width-1
	}
	var starts []int
	for row := 1; row <= rows; row++ {
		for column := 1; column <= columns; column++ {
			position, r, c := row*width+column, 2*row-1, 2*column-1
			if scheme[r][c] == '1' || scheme[r][c] == '2' {
				starts = append(starts, position)
			}
			walls := []byte{scheme[r-1][c], scheme[r][c+1], scheme[r+1][c], scheme[r][c-1]}
			for direction, wall := range walls {
				if wall == '.' {
					masks[position] |= byte(1 << direction)
				}
			}
		}
	}
	for position := 0; position < size; position++ {
		if !outside[position] {
			continue
		}
		row, column := position/width, position%width
		for direction, move := range moves {
			nr, nc := row+move.row, column+move.column
			if nr < 0 || nr >= height || nc < 0 || nc >= width {
				continue
			}
			neighbor, opposite := nr*width+nc, (direction+2)%len(moves)
			if outside[neighbor] || masks[neighbor]&byte(1<<opposite) != 0 {
				masks[position] |= byte(1 << direction)
			}
		}
	}
	relative := []point{{0, 1}, {1, -1}, {1, 0}, {1, 1}}
	deltas := make([]int, orientations)
	transitions := make([][]transition, orientations)
	for orientation, delta := range relative {
		deltas[orientation] = delta.row*width + delta.column
		for player := 0; player < 2; player++ {
			for direction, move := range moves {
				positions := [2]point{{0, 0}, delta}
				positions[player].row += move.row
				positions[player].column += move.column
				if positions[1].row < positions[0].row || positions[1].row == positions[0].row &&
					positions[1].column < positions[0].column {
					positions[0], positions[1] = positions[1], positions[0]
				}
				difference := point{positions[1].row - positions[0].row,
					positions[1].column - positions[0].column}
				next := -1
				for index, candidate := range relative {
					if candidate == difference {
						next = index
						break
					}
				}
				if next < 0 {
					continue
				}
				shift := positions[0].row*width + positions[0].column
				transitions[orientation] = append(transitions[orientation], transition{
					player: player, mask: byte(1 << direction), offset: offsets[direction],
					change: shift*orientations + next - orientation,
				})
			}
		}
	}
	if starts[0] > starts[1] {
		starts[0], starts[1] = starts[1], starts[0]
	}
	orientation := 0
	for index, delta := range deltas {
		if delta == starts[1]-starts[0] {
			orientation = index
		}
	}
	initial := starts[0]*orientations + orientation
	distance := make([]int32, size*orientations)
	finished := make([]bool, len(distance))
	for index := range distance {
		distance[index] = -1
	}
	distance[initial] = 0
	pending := intDeque{values: make([]int, initialQueueCapacity)}
	pending.addLast(initial)
	for pending.size > 0 {
		state := pending.removeFirst()
		if finished[state] {
			continue
		}
		finished[state] = true
		current, first, dir := distance[state], state/orientations, state%orientations
		second := first + deltas[dir]
		if outside[first] && outside[second] {
			return int(current)
		}
		for _, action := range transitions[dir] {
			position := first
			if action.player != 0 {
				position = second
			}
			if masks[position]&action.mask == 0 {
				continue
			}
			neighbor, cost := position+action.offset, int32(1)
			if outside[position] && outside[neighbor] {
				cost = 0
			}
			following, candidate := state+action.change, current+cost
			if distance[following] == -1 || candidate < distance[following] {
				distance[following] = candidate
				if cost == 0 {
					pending.addFirst(following)
				} else {
					pending.addLast(following)
				}
			}
		}
	}
	return -1
}

func main() {
	in := bufio.NewReader(os.Stdin)
	header, _ := in.ReadString('\n')
	var rows, columns int
	fmt.Sscan(header, &rows, &columns)
	scheme := make([]string, 2*rows+1)
	for index := range scheme {
		line, _ := in.ReadString('\n')
		scheme[index] = strings.TrimRight(line, "\r\n")
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	answer := minimumPassages(rows, columns, scheme)
	if answer < 0 {
		fmt.Fprintln(out, "Death")
	} else {
		fmt.Fprintln(out, answer)
	}
}
