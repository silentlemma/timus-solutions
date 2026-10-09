package main

import (
	"fmt"
	"math"
)

type vec struct{ x, y, z float64 }

func (a vec) sub(b vec) vec     { return vec{a.x - b.x, a.y - b.y, a.z - b.z} }
func (a vec) dot(b vec) float64 { return a.x*b.x + a.y*b.y + a.z*b.z }
func (a vec) norm() float64     { return math.Sqrt(a.dot(a)) }
func (a vec) cross(b vec) vec {
	return vec{a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x}
}

func read() (v vec) {
	fmt.Scan(&v.x, &v.y, &v.z)
	return
}

func main() {
	a, b, c := read(), read(), read()
	var r float64
	fmt.Scan(&r)
	u, v := a.sub(c), b.sub(c)
	angle := math.Atan2(u.cross(v).norm(), u.dot(v))
	da, db := u.norm(), v.norm()
	// seen from C, the tangents from A and B cover these angles; when the angle
	// ACB fits in them, the segment AB misses the ball
	reach := math.Acos(r/da) + math.Acos(r/db)
	length := a.sub(b).norm()
	if angle > reach {
		length = math.Sqrt(da*da-r*r) + math.Sqrt(db*db-r*r) + r*(angle-reach)
	}
	fmt.Printf("%.2f\n", length)
}
