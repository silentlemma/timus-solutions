package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Faces: 0 the base, 1..4 the sides clockwise from the one facing +y. On the
// base, side k rests on the edge (v[k - 1], v[k % 4]); on a side, v[0] and
// v[1] are its base corners and v[2] its apex.
const (
	sides    = 4
	faces    = 5
	maxRolls = 32
	eps      = 1e-12
	none     = -1e100
	beamSize = 4000 // states kept per depth by the first, greedy pass
	triangle = 3    // corners of a side: its centroid is a third of the way up
)

type pt struct{ x, y float64 }

type state struct {
	face, prev int
	v          [sides]pt
	c          pt // the centre of the face on the table
}

var (
	s, t, X, Y float64 // the base edge, the height of a side, the point
	N          int
	// the farthest the centre can go, ending on the base
	reach     [faces * faces][maxRolls + 1]float64
	best      float64
	bestRolls int
	bestSeq   [maxRolls + 1]int
	seq       [maxRolls + 1]int
)

func key(prev, face int) int {
	if prev < 0 {
		return 0
	}
	return prev*faces + face
}

func canRoll(face, next int) bool {
	if face == next {
		return false
	}
	return face == 0 || next == 0 || (face-next+sides)%2 == 1 // not the opposite side
}

func cross(a, b, p pt) float64 { return (b.x-a.x)*(p.y-a.y) - (b.y-a.y)*(p.x-a.x) }

func reflect(p, a, b pt) pt {
	dx, dy := b.x-a.x, b.y-a.y
	k := ((p.x-a.x)*dx + (p.y-a.y)*dy) / (dx*dx + dy*dy)
	return pt{2*(a.x+k*dx) - p.x, 2*(a.y+k*dy) - p.y}
}

// the unit normal of a -> b pointing away from q
func away(a, b, q pt) (float64, float64) {
	dx, dy := b.x-a.x, b.y-a.y
	length := math.Hypot(dx, dy)
	nx, ny := -dy/length, dx/length
	if cross(a, b, pt{a.x + nx, a.y + ny})*cross(a, b, q) > 0 {
		nx, ny = -nx, -ny
	}
	return nx, ny
}

func roll(st *state, next int) state {
	ns := state{face: next, prev: st.face}
	v := &st.v
	switch {
	case st.face == 0: // onto side next: its apex beyond the edge
		a, b := v[next-1], v[next%sides]
		nx, ny := away(a, b, st.c)
		ns.v[0], ns.v[1] = a, b
		ns.v[2] = pt{(a.x+b.x)/2 + nx*t, (a.y+b.y)/2 + ny*t}
	case next == 0: // onto the base: the square beyond the edge
		a, b := v[0], v[1]
		nx, ny := away(a, b, v[2])
		corner := [sides]pt{a, b, {b.x + nx*s, b.y + ny*s}, {a.x + nx*s, a.y + ny*s}}
		for i, p := range corner {
			ns.v[(st.face-1+i)%sides] = p
		}
	case next == st.face%sides+1: // clockwise over the edge (v[1], apex)
		ns.v[0], ns.v[1], ns.v[2] = v[1], reflect(v[0], v[1], v[2]), v[2]
	default: // counterclockwise over the edge (v[0], apex)
		ns.v[0], ns.v[1], ns.v[2] = reflect(v[1], v[0], v[2]), v[0], v[2]
	}
	n := sides - 1
	if next == 0 {
		n = sides
	}
	for _, p := range ns.v[:n] {
		ns.c.x += p.x / float64(n)
		ns.c.y += p.y / float64(n)
	}
	return ns
}

func distTo(st *state) float64 { return math.Hypot(st.c.x-X, st.c.y-Y) }

// can this state, with r rolls left, still beat the best?
func hopeful(st *state, r int) bool {
	u := reach[key(st.prev, st.face)][r]
	lim := best + u + eps
	dx, dy := st.c.x-X, st.c.y-Y
	return u > none && dx*dx+dy*dy <= lim*lim
}

func consider(sequence []int, rolls int, d float64) {
	if d+eps < best || (math.Abs(d-best) <= eps && rolls < bestRolls) {
		best, bestRolls = d, rolls
		copy(bestSeq[:], sequence[:rolls+1])
	}
}

func search(st *state, depth int) {
	if st.face == 0 {
		consider(seq[:], depth, distTo(st))
	}
	if depth == N {
		return
	}
	var next [sides]state
	var d2 [sides]float64
	count := 0
	for f := 0; f < faces; f++ {
		if !canRoll(st.face, f) || f == st.prev {
			continue
		}
		ns := roll(st, f)
		if hopeful(&ns, N-depth-1) {
			dx, dy := ns.c.x-X, ns.c.y-Y
			next[count], d2[count] = ns, dx*dx+dy*dy
			count++
		}
	}
	for i := 1; i < count; i++ { // nearest first
		for j := i; j > 0 && d2[j] < d2[j-1]; j-- {
			next[j], next[j-1] = next[j-1], next[j]
			d2[j], d2[j-1] = d2[j-1], d2[j]
		}
	}
	for i := 0; i < count; i++ {
		seq[depth+1] = next[i].face
		search(&next[i], depth+1)
	}
}

type beamState struct {
	key float64
	st  state
	seq [maxRolls + 1]int
}

// a first answer: a beam search keeping the states that may get closest
func beam(start state) {
	states := []beamState{{st: start}}
	for depth := 0; depth < N; depth++ {
		var next []beamState
		for i := range states {
			b := &states[i]
			for f := 0; f < faces; f++ {
				if !canRoll(b.st.face, f) || f == b.st.prev {
					continue
				}
				ns := roll(&b.st, f)
				d, r := distTo(&ns), reach[key(ns.prev, ns.face)][N-depth-1]
				if r <= none {
					continue
				}
				nb := beamState{key: math.Max(0, d-r), st: ns, seq: b.seq}
				nb.seq[depth+1] = f
				if f == 0 {
					consider(nb.seq[:], depth+1, d)
				}
				next = append(next, nb)
			}
		}
		sort.Slice(next, func(i, j int) bool { return next[i].key < next[j].key })
		if len(next) > beamSize {
			next = next[:beamSize]
		}
		states = next
	}
}

func main() {
	var l float64
	fmt.Fscan(bufio.NewReader(os.Stdin), &s, &l, &X, &Y, &N)
	t = math.Sqrt(l*l - (s/2)*(s/2))
	// how far one roll moves the centre: base <-> side, and side <-> side
	baseStep, sideStep := s/2+t/triangle, 2*s*t/(triangle*l)
	for i := range reach {
		for r := range reach[i] {
			reach[i][r] = none
		}
	}
	for prev := -1; prev < faces; prev++ {
		if prev != 0 {
			reach[key(prev, 0)][0] = 0
		}
	}
	for r := 1; r <= N; r++ {
		for face := 0; face < faces; face++ {
			for prev := -1; prev < faces; prev++ {
				if (prev < 0 && face != 0) || (prev >= 0 && !canRoll(prev, face)) {
					continue
				}
				u := &reach[key(prev, face)][r]
				*u = reach[key(prev, face)][r-1]
				if face == 0 {
					*u = math.Max(*u, 0)
				}
				for f := 0; f < faces; f++ {
					if !canRoll(face, f) || f == prev || reach[key(face, f)][r-1] <= none {
						continue
					}
					step := sideStep
					if face == 0 || f == 0 {
						step = baseStep
					}
					*u = math.Max(*u, step+reach[key(face, f)][r-1])
				}
			}
		}
	}
	start := state{face: 0, prev: -1}
	start.v = [sides]pt{{-s / 2, s / 2}, {s / 2, s / 2}, {s / 2, -s / 2}, {-s / 2, -s / 2}}
	best, bestRolls = math.Hypot(X, Y), 0
	beam(start)
	search(&start, 0)
	faceList := make([]string, bestRolls+1)
	for i := range faceList {
		faceList[i] = strconv.Itoa(bestSeq[i])
	}
	fmt.Printf("%.3f\n%d\n%s\n", best+eps, bestRolls, strings.Join(faceList, " "))
}
