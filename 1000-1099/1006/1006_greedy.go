package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const (
	width      = 50
	height     = 20
	minSide    = 2
	empty      = byte('.')
	upperLeft  = byte(218)
	upperRight = byte(191)
	lowerLeft  = byte(192)
	lowerRight = byte(217)
	vertical   = byte(179)
	horizontal = byte(196)
)

type frame struct{ x, y, side int }

var (
	screen [height][width]byte
	peeled [height][width]bool
)

// fits: a peeled cell is covered by a frame drawn later, so it may hold anything.
func fits(x, y int, c byte, fresh *int) bool {
	if peeled[y][x] {
		return true
	}
	if screen[y][x] != c {
		return false
	}
	*fresh++
	return true
}

// frameFits: the frame matches the picture where it is visible and shows something new.
func frameFits(x, y, side int) bool {
	last, fresh := side-1, 0
	if !fits(x, y, upperLeft, &fresh) || !fits(x+last, y, upperRight, &fresh) ||
		!fits(x, y+last, lowerLeft, &fresh) || !fits(x+last, y+last, lowerRight, &fresh) {
		return false
	}
	for i := 1; i < last; i++ {
		if !fits(x+i, y, horizontal, &fresh) || !fits(x+i, y+last, horizontal, &fresh) ||
			!fits(x, y+i, vertical, &fresh) || !fits(x+last, y+i, vertical, &fresh) {
			return false
		}
	}
	return fresh > 0
}

func peelCell(x, y int, left *int) {
	if !peeled[y][x] {
		peeled[y][x] = true
		*left--
	}
}

func peel(x, y, side int, left *int) {
	last := side - 1
	for i := 0; i <= last; i++ {
		peelCell(x+i, y, left)
		peelCell(x+i, y+last, left)
		peelCell(x, y+i, left)
		peelCell(x+last, y+i, left)
	}
}

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	left, pos := 0, 0
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			c := empty
			if pos < len(data) && data[pos] != '\n' && data[pos] != '\r' {
				c = data[pos]
				pos++
			}
			screen[y][x] = c
			if c != empty {
				left++
			}
		}
		for pos < len(data) && data[pos] != '\n' {
			pos++
		}
		pos++
	}

	// Undo the drawing: a frame that fits can be the last one drawn among the
	// remaining ones; its cells then may hold anything.
	var frames []frame
	for left > 0 {
		before := left
		for y := 0; y < height; y++ {
			for x := 0; x < width; x++ {
				for side := minSide; x+side <= width && y+side <= height; side++ {
					if frameFits(x, y, side) {
						frames = append(frames, frame{x, y, side})
						peel(x, y, side, &left)
					}
				}
			}
		}
		if left == before {
			break
		}
	}

	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(frames))
	for i := len(frames) - 1; i >= 0; i-- {
		fmt.Fprintln(out, frames[i].x, frames[i].y, frames[i].side)
	}
}
