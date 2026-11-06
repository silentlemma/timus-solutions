package main

import (
	"bufio"
	"bytes"
	"io"
	"os"
)

const (
	alice = 1
	draw  = 0
	bob   = -1
	base  = 10
)

type face struct {
	cells    []byte
	reversed bool
}

func (f face) halves() (face, face) {
	half := len(f.cells) / 2
	if f.reversed {
		return face{f.cells[half:], true}, face{f.cells[:half], false}
	}
	return face{f.cells[:half], false}, face{f.cells[half:], true}
}

func fold(f face, top, nextAlice bool) int {
	if f.cells[0] == 'A' {
		if bytes.IndexByte(f.cells, 'B') < 0 {
			return alice
		}
	} else if bytes.IndexByte(f.cells, 'A') < 0 {
		return bob
	}
	left, right := f.halves()
	if top {
		return play(left, right, nextAlice)
	}
	return play(right, left, nextAlice)
}

func play(top, bottom face, turnAlice bool) int {
	if len(top.cells)%2 != 0 {
		return draw
	}
	first := fold(top, true, !turnAlice)
	if turnAlice && first == alice || !turnAlice && first == bob {
		return first
	}
	second := fold(bottom, false, !turnAlice)
	if turnAlice && second > first || !turnAlice && second < first {
		return second
	}
	return first
}

func nextNonSpace(input *bufio.Reader) byte {
	for {
		ch, err := input.ReadByte()
		if err != nil {
			return 0
		}
		if ch > ' ' {
			return ch
		}
	}
}

func main() {
	input := bufio.NewReader(os.Stdin)
	size := 0
	ch := nextNonSpace(input)
	for ch >= '0' && ch <= '9' {
		size = size*base + int(ch-'0')
		ch, _ = input.ReadByte()
	}
	if size == 0 {
		return
	}
	cells := make([]byte, 2*size)
	for _, row := range [][]byte{cells[:size], cells[size:]} {
		row[0] = nextNonSpace(input)
		if _, err := io.ReadFull(input, row[1:]); err != nil {
			return
		}
	}
	switch play(face{cells[:size], false}, face{cells[size:], false}, true) {
	case alice:
		os.Stdout.WriteString("Alice\n")
	case bob:
		os.Stdout.WriteString("Bob\n")
	default:
		os.Stdout.WriteString("Draw\n")
	}
}
