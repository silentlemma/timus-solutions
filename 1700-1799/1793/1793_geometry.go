package main

import "fmt"

func main() {
	var a, b, d, r1, top1, r2, top2, h int64
	if _, err := fmt.Scan(&a, &b, &d, &r1, &top1, &r2, &top2, &h); err != nil {
		return
	}
	// the widest part of a plate inside the borders, at height min(d, h),
	// scaled by h to stay in integers
	low := d
	if h < low {
		low = h
	}
	w1 := r1*h + (top1-r1)*low
	w2 := r2*h + (top2-r2)*low
	fits := 2*w1 <= a*h && 2*w1 <= b*h && 2*w2 <= a*h && 2*w2 <= b*h
	// the centres can be this far apart along each side, and the plates
	// must be at least top1 + top2 apart, where they are widest
	dx, dy, need := a*h-w1-w2, b*h-w1-w2, (top1+top2)*h
	apart := dx*dx+dy*dy >= need*need
	if fits && apart {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
