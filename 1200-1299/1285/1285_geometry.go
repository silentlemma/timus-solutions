package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const dim = 8

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b, c [dim]int64
	var r int64
	for _, v := range []*[dim]int64{&a, &b, &c} {
		for i := range v {
			fmt.Fscan(in, &v[i])
		}
	}
	fmt.Fscan(in, &r)
	var length2, ca2, cb2, dot int64
	for i := 0; i < dim; i++ {
		ab, ac, bc := b[i]-a[i], c[i]-a[i], c[i]-b[i]
		length2 += ab * ab
		ca2 += ac * ac
		cb2 += bc * bc
		dot += ab * ac
	}
	// the segment enters the ball when the closest point of it to C lies
	// strictly inside; outside 0 <= t <= 1 the closest point is an end, and
	// both ends are outside: |AC|^2 |AB|^2 - (AB . AC)^2 < R^2 |AB|^2
	if length2 == 0 || dot <= 0 || dot >= length2 || ca2*length2-dot*dot >= r*r*length2 {
		fmt.Printf("%.2f\n", math.Sqrt(float64(length2)))
		return
	}
	// otherwise, in the plane of A, B and C: a tangent from A, an arc of the
	// great circle and a tangent to B
	da, db := math.Sqrt(float64(ca2)), math.Sqrt(float64(cb2))
	cos := float64(ca2+cb2-length2) / (2 * da * db)
	angle := math.Acos(math.Max(-1, math.Min(1, cos)))
	rf := float64(r)
	arc := angle - math.Acos(rf/da) - math.Acos(rf/db)
	fmt.Printf("%.2f\n", math.Sqrt(float64(ca2-r*r))+math.Sqrt(float64(cb2-r*r))+rf*arc)
}
