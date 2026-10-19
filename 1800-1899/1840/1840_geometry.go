package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	top = 10.0 // the speed limit; both accelerations are limited by 1
	eps = 1e-12
)

type piece struct{ length, cap float64 }

// fastest run over a piece entered at v0 and left at v1: speed up,
// perhaps cruise at the cap, slow down
func pieceTime(p piece, v0, v1 float64) float64 {
	if p.length <= eps {
		return 0
	}
	up, down := (p.cap*p.cap-v0*v0)/2, (p.cap*p.cap-v1*v1)/2
	if up+down <= p.length {
		return (p.cap - v0) + (p.cap - v1) + (p.length-up-down)/p.cap
	}
	peak := math.Sqrt(p.length + (v0*v0+v1*v1)/2)
	return (peak - v0) + (peak - v1)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	ax, ay, bx, by := make([]float64, n), make([]float64, n), make([]float64, n), make([]float64, n)
	ux, uy := make([]float64, n), make([]float64, n)
	length, extra := make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &ax[i], &ay[i], &bx[i], &by[i])
		length[i] = math.Hypot(bx[i]-ax[i], by[i]-ay[i])
		ux[i], uy[i] = (bx[i]-ax[i])/length[i], (by[i]-ay[i])/length[i]
	}
	var arcs []piece
	for i := 0; i+1 < n; i++ {
		dx, dy := ax[i+1]-bx[i], ay[i+1]-by[i]
		sin := ux[i]*uy[i+1] - uy[i]*ux[i+1]
		cos := ux[i]*ux[i+1] + uy[i]*uy[i+1]
		var radius, angle float64
		if math.Abs(sin) > eps {
			// the lines meet t past the end of this segment and back before
			// the start of the next one; the arc touches both lines at the
			// same distance from that point, as far as it can
			t := (dx*uy[i+1] - dy*ux[i+1]) / sin
			back := -(dx*uy[i] - dy*ux[i]) / sin
			nearest := math.Min(t, back)
			extra[i] += t - nearest
			extra[i+1] += back - nearest
			if math.Abs(nearest) <= eps {
				arcs = append(arcs, piece{0, 0})
				continue
			}
			radius = math.Abs(nearest) * (1 + cos) / math.Abs(sin)
			turn := math.Atan2(math.Abs(sin), cos)
			// a meeting point behind forces the long way around the circle
			angle = turn
			if nearest < 0 {
				angle = 2*math.Pi - turn
			}
		} else {
			// opposite directions: a half circle across the gap
			along, across := dx*ux[i]+dy*uy[i], -dx*uy[i]+dy*ux[i]
			if along > 0 {
				extra[i] += along
			} else {
				extra[i+1] -= along
			}
			radius, angle = math.Abs(across)/2, math.Pi
		}
		arcs = append(arcs, piece{radius * angle, math.Min(top, math.Sqrt(radius))})
	}
	var pieces []piece
	for i := 0; i < n; i++ {
		pieces = append(pieces, piece{length[i] + extra[i], top})
		if i+1 < n {
			pieces = append(pieces, arcs[i])
		}
	}
	// the speed where pieces meet: what acceleration from the start and
	// braking before the end allow, within the caps on both sides
	m := len(pieces)
	reach, stop := make([]float64, m+1), make([]float64, m+1)
	for i := 0; i < m; i++ {
		reach[i+1] = math.Min(pieces[i].cap, math.Sqrt(reach[i]*reach[i]+2*pieces[i].length))
	}
	for i := m - 1; i >= 0; i-- {
		stop[i] = math.Min(pieces[i].cap, math.Sqrt(stop[i+1]*stop[i+1]+2*pieces[i].length))
	}
	total := 0.0
	for i, p := range pieces {
		total += pieceTime(p, math.Min(reach[i], stop[i]), math.Min(reach[i+1], stop[i+1]))
	}
	fmt.Printf("%.10f\n", total)
}
