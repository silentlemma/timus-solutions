package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	outputSize = 8
	cubeFaces  = 6
	ringSize   = 4
	byteValues = 256
)

const colours = 10
const rings = colours * colours * colours * colours

// One ring for each choice of opposite faces as the top and bottom.
var sides = [3][4]int{{0, 1, 3, 2}, {4, 1, 5, 2}, {0, 4, 3, 5}}

func key(cube [cubeFaces]int, faces [ringSize]int) int {
	start := 0
	for i := 1; i < len(faces); i++ {
		if cube[faces[i]] < cube[faces[start]] {
			start = i
		}
	}
	a, b := cube[faces[start]], cube[faces[(start+1)%len(faces)]]
	c, d := cube[faces[(start+2)%len(faces)]], cube[faces[(start+ringSize-1)%len(faces)]]
	// Rotate to the least colour, then take the smaller of the two directions.
	if b > d {
		b, d = d, b
	}
	return ((a*colours+b)*colours+c)*colours + d
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	in.Scan()
	n, _ := strconv.Atoi(in.Text())
	var ids [byteValues]int
	nextID := 1
	var counts [rings]uint16
	var best uint16
	for i := 0; i < n && in.Scan(); i++ {
		var cube [cubeFaces]int
		for face, colour := range in.Bytes() {
			if ids[colour] == 0 {
				ids[colour] = nextID
				nextID++
			}
			cube[face] = ids[colour] - 1
		}
		for _, faces := range sides {
			ring := key(cube, faces)
			counts[ring]++
			if counts[ring] > best {
				best = counts[ring]
			}
		}
	}
	var output [outputSize]byte
	os.Stdout.Write(append(strconv.AppendInt(output[:0], int64(best), 10), '\n'))
}
