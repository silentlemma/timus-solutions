package main

import "fmt"

func floorDiv(a, b int64) int64 {
	q := a / b
	if q*b > a {
		q--
	}
	return q
}

func main() {
	var ar, ai, br, bi int64
	fmt.Scan(&ar, &ai, &br, &bi)
	norm := br*br + bi*bi
	if norm == 0 {
		fmt.Println(0) // no remainder is shorter than zero
		return
	}
	// a / b = (x + y i) / norm; every quotient q lies within 1 of it
	x, y := ar*br+ai*bi, ai*br-ar*bi
	fx, fy := floorDiv(x, norm), floorDiv(y, norm)
	count := 0
	for qr := fx - 1; qr <= fx+1; qr++ {
		for qi := fy - 1; qi <= fy+1; qi++ {
			rr, ri := ar-(br*qr-bi*qi), ai-(br*qi+bi*qr)
			if rr*rr+ri*ri < norm {
				count++
			}
		}
	}
	fmt.Println(count)
}
