package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

const pieceSide = 4
const gridSide = 3
const pieceCount = gridSide * gridSide
const turnCount = 4
const stateCount = pieceCount * turnCount
const pixelCount = pieceSide * pieceSide
const stride = pieceSide - 1
const boardSide = gridSide*stride + 1

type piece [pixelCount]int
type neighbor struct{ direction, slot int }
type solver struct {
	states     [stateCount]piece
	masks      [pieceCount]uint64
	compatible [turnCount][stateCount]uint64
	neighbors  [pieceCount][]neighbor
	placement  [pieceCount]int
}

func (s *solver) search(domains [pieceCount]uint64, remaining int) bool {
	if remaining == 0 {
		return true
	}
	slot, best := -1, stateCount+1
	for i := 0; i < pieceCount; i++ {
		if s.placement[i] >= 0 {
			continue
		}
		count := bits.OnesCount64(domains[i])
		if count < best || count == best && len(s.neighbors[i]) > len(s.neighbors[slot]) {
			slot, best = i, count
		}
	}
	for choices := domains[slot]; choices != 0; choices &= choices - 1 {
		state := bits.TrailingZeros64(choices)
		s.placement[slot] = state
		unused := ^s.masks[state/turnCount]
		following := domains
		for i := range following {
			following[i] &= unused
		}
		for _, adjacent := range s.neighbors[slot] {
			if s.placement[adjacent.slot] < 0 {
				following[adjacent.slot] &= s.compatible[adjacent.direction][state]
			}
		}
		possible := true
		for i := 0; i < pieceCount; i++ {
			if s.placement[i] < 0 && following[i] == 0 {
				possible = false
			}
		}
		if possible && s.search(following, remaining-1) {
			return true
		}
		s.placement[slot] = -1
	}
	return false
}

func assemble(pieces [pieceCount]piece) [boardSide][boardSide]int {
	s := solver{}
	var initial uint64
	for index, original := range pieces {
		current := original
		for turn := 0; turn < turnCount; turn++ {
			state := index*turnCount + turn
			s.states[state] = current
			s.masks[index] |= uint64(1) << uint(state)
			duplicate := false
			for previous := index * turnCount; previous < state; previous++ {
				duplicate = duplicate || s.states[previous] == current
			}
			if !duplicate && (index != 0 || turn == 0) {
				initial |= uint64(1) << uint(state)
			}
			var rotated piece
			for r := 0; r < pieceSide; r++ {
				for c := 0; c < pieceSide; c++ {
					rotated[r*pieceSide+c] = current[(pieceSide-1-c)*pieceSide+r]
				}
			}
			current = rotated
		}
	}
	var edges [stateCount][turnCount][pieceSide]int
	for state, pixels := range s.states {
		for i := 0; i < pieceSide; i++ {
			edges[state][0][i] = pixels[i]
			edges[state][1][i] = pixels[i*pieceSide+pieceSide-1]
			edges[state][2][i] = pixels[(pieceSide-1)*pieceSide+i]
			edges[state][turnCount-1][i] = pixels[i*pieceSide]
		}
	}
	for direction := 0; direction < turnCount; direction++ {
		for first := 0; first < stateCount; first++ {
			for second := 0; second < stateCount; second++ {
				opposite := (direction + 2) % turnCount
				if first/turnCount != second/turnCount &&
					edges[first][direction] == edges[second][opposite] {
					s.compatible[direction][first] |= uint64(1) << uint(second)
				}
			}
		}
	}
	dr, dc := [turnCount]int{-1, 0, 1, 0}, [turnCount]int{0, 1, 0, -1}
	var domains [pieceCount]uint64
	for slot := 0; slot < pieceCount; slot++ {
		s.placement[slot], domains[slot] = -1, initial
		for direction := 0; direction < turnCount; direction++ {
			r, c := slot/gridSide+dr[direction], slot%gridSide+dc[direction]
			if 0 <= r && r < gridSide && 0 <= c && c < gridSide {
				s.neighbors[slot] = append(s.neighbors[slot], neighbor{direction, r*gridSide + c})
			}
		}
	}
	if !s.search(domains, pieceCount) {
		panic("The guaranteed arrangement was not found")
	}
	var board [boardSide][boardSide]int
	for slot, state := range s.placement {
		for r := 0; r < pieceSide; r++ {
			for c := 0; c < pieceSide; c++ {
				board[slot/gridSide*stride+r][slot%gridSide*stride+c] = s.states[state][r*pieceSide+c]
			}
		}
	}
	return board
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var pieces [pieceCount]piece
	for i := range pieces {
		for j := range pieces[i] {
			fmt.Fscan(in, &pieces[i][j])
		}
	}
	for _, row := range assemble(pieces) {
		for c, value := range row {
			if c != 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, value)
		}
		fmt.Fprintln(out)
	}
}
