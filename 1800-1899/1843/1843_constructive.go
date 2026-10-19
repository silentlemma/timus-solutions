package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// front, back, down, up, left, right: face 2a + side lies on axis a
const faces = "FBDULR"
const sides = len(faces)
const axes = sides / 2

// axisSum - a - b is the axis other than a and b
const axisSum = axes * (axes - 1) / 2
const inside = '.'

// quarter turns about the vertical and the front-back axis: the face at
// each letter's place comes from the place of the next letter, cyclically
var quarterTurns = []string{"FLBR", "DLUR"}

type turn [sides]int

type piece struct {
	dims   [axes]int
	colors string
}

// rotations returns every turn: p puts the old face p[k] at place k, and
// the two quarter turns generate all 24
func rotations() []turn {
	var start turn
	for k := range start {
		start[k] = k
	}
	var turns []turn
	for _, cycle := range quarterTurns {
		p := start
		for i := range cycle {
			p[strings.IndexByte(faces, cycle[i])] = strings.IndexByte(faces, cycle[(i+1)%len(cycle)])
		}
		turns = append(turns, p)
	}
	seen := map[turn]bool{start: true}
	all := []turn{start}
	for todo := []turn{start}; len(todo) > 0; {
		p := todo[len(todo)-1]
		todo = todo[:len(todo)-1]
		for _, q := range turns {
			var r turn
			for k := range r {
				r[k] = p[q[k]]
			}
			if !seen[r] {
				seen[r] = true
				all = append(all, r)
				todo = append(todo, r)
			}
		}
	}
	return all
}

// turned writes the extents and colours of a turned piece as one string
func turned(p turn, x piece) string {
	var b strings.Builder
	for a := 0; a < axes; a++ {
		b.WriteString(strconv.Itoa(x.dims[p[2*a]/2]))
		b.WriteByte(',')
	}
	for k := 0; k < sides; k++ {
		b.WriteByte(x.colors[p[k]])
	}
	return b.String()
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var size [axes]int
	var box string
	var n int
	for a := range size {
		fmt.Fscan(in, &size[a])
	}
	fmt.Fscan(in, &box, &n)
	pieces := make([]piece, n)
	for i := range pieces {
		x := &pieces[i]
		for a := range x.dims {
			fmt.Fscan(in, &x.dims[a])
		}
		fmt.Fscan(in, &x.colors)
	}
	turns := rotations()
	canonical := func(x piece) string {
		best := turned(turns[0], x)
		for _, p := range turns {
			if s := turned(p, x); s < best {
				best = s
			}
		}
		return best
	}
	// the pieces on the edge along an axis carry the two box colours of the
	// faces before it on the other axes; their remaining extents are the
	// sections, the first one also coloured like the start face
	var cuts [axes][]int
	for axis := 0; axis < axes; axis++ {
		a := 0
		if axis == 0 {
			a = 1
		}
		b := axisSum - axis - a
		var first, middle, last []int
		for _, x := range pieces {
			fa, fb := strings.IndexByte(x.colors, box[2*a]), strings.IndexByte(x.colors, box[2*b])
			if fa < 0 || fb < 0 {
				continue
			}
			extent := x.dims[axisSum-fa/2-fb/2]
			if strings.IndexByte(x.colors, box[2*axis]) >= 0 {
				first = append(first, extent)
			} else if strings.IndexByte(x.colors, box[2*axis+1]) >= 0 {
				last = append(last, extent)
			} else {
				middle = append(middle, extent)
			}
		}
		cuts[axis] = append(append(first, middle...), last...)
	}
	// middle sections may come in any order: the pieces are the same
	groups := map[string][]int{}
	for i, x := range pieces {
		key := canonical(x)
		groups[key] = append(groups[key], i)
	}
	answer := make([]string, n)
	var place, corner [axes]int
	for place[0] = 0; place[0] < len(cuts[0]); place[0]++ {
		corner[1] = 0
		for place[1] = 0; place[1] < len(cuts[1]); place[1]++ {
			corner[2] = 0
			for place[2] = 0; place[2] < len(cuts[2]); place[2]++ {
				var want piece
				colors := make([]byte, 0, sides)
				for axis := 0; axis < axes; axis++ {
					want.dims[axis] = cuts[axis][place[axis]]
					c, d := byte(inside), byte(inside)
					if place[axis] == 0 {
						c = box[2*axis]
					}
					if place[axis] == len(cuts[axis])-1 {
						d = box[2*axis+1]
					}
					colors = append(colors, c, d)
				}
				want.colors = string(colors)
				key := canonical(want)
				group := groups[key]
				k := group[len(group)-1]
				groups[key] = group[:len(group)-1]
				target := turned(turns[0], want)
				for _, p := range turns {
					if turned(p, pieces[k]) == target {
						answer[k] = fmt.Sprintf("%c %c %d %d %d",
							faces[p[0]], faces[p[2]], corner[0], corner[1], corner[2])
						break
					}
				}
				corner[2] += want.dims[2]
			}
			corner[1] += cuts[1][place[1]]
		}
		corner[0] += cuts[0][place[0]]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, strings.Join(answer, "\n"))
}
