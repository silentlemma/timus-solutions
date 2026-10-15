package main

import (
	"fmt"
	"math"
)

const dim = 3

func cross(u, v [dim]float64) [dim]float64 {
	return [dim]float64{u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]}
}

func main() {
	var a, b int64
	var p, q, d [dim]int64
	fmt.Scan(&a, &b)
	for i := range p {
		fmt.Scan(&p[i])
	}
	for i := range q {
		fmt.Scan(&q[i])
	}
	for i := range d {
		d[i] = q[i] - p[i]
	}
	// the elbow's axis is parallel to the rail and across both segments, so the
	// shoulder, the elbow and the claw lie in the plane through the shoulder
	// across the rail, and the claw sits at the rail's point h nearest to it
	c := [dim]int64{p[1]*d[2] - p[2]*d[1], p[2]*d[0] - p[0]*d[2], p[0]*d[1] - p[1]*d[0]}
	dd := d[0]*d[0] + d[1]*d[1] + d[2]*d[2]
	num := c[0]*c[0] + c[1]*c[1] + c[2]*c[2] // |h|^2 = num / dd, exactly
	// the bend (the angle opposite h) is not acute and the triangle closes:
	// a^2 + b^2 <= |h|^2 <= (a + b)^2
	if (a*a+b*b)*dd > num || num > (a+b)*(a+b)*dd {
		fmt.Println("No solution.")
		return
	}
	t := -float64(p[0]*d[0]+p[1]*d[1]+p[2]*d[2]) / float64(dd)
	r := math.Sqrt(float64(num) / float64(dd))
	var e1, unit [dim]float64
	for i := range e1 {
		e1[i] = (float64(p[i]) + t*float64(d[i])) / r
		unit[i] = float64(d[i]) / math.Sqrt(float64(dd))
	}
	e2 := cross(unit, e1)
	// the elbow is at distance a from the shoulder and b from h
	fa, fb := float64(a), float64(b)
	along := (fa*fa - fb*fb + r*r) / (2 * r)
	side := math.Sqrt(math.Max(0, fa*fa-along*along))
	bend := math.Acos(math.Max(-1, math.Min(1, (fa*fa+fb*fb-r*r)/(2*fa*fb))))
	for i := 0; i < dim; i++ {
		fmt.Printf("%.15f ", along*e1[i]+side*e2[i])
	}
	fmt.Printf("%.15f\n", bend)
}
