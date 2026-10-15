package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

const (
	scale    = 1000
	halfTurn = 180 * scale
	fullTurn = 2 * halfTurn
	digits   = 3
)

// the angle in thousandths of a degree, read exactly from the text
func thousandths(text string) int64 {
	whole, part := text, ""
	if dot := strings.IndexByte(text, '.'); dot >= 0 {
		whole, part = text[:dot], text[dot+1:]
	}
	part = (part + "000")[:digits]
	w, _ := strconv.Atoi(whole)
	p, _ := strconv.Atoi(part)
	return int64(w)*scale + int64(p)
}

func main() {
	var r float64
	var angle string
	fmt.Scan(&r, &angle)
	a := thousandths(angle)
	// each shore point shows an arc of 2a, so the walk along the shore
	// covers 360 - 2a degrees; chords grow slower than their angles, so
	// it is shortest as full 2a chords and one short chord for the rest
	steps := halfTurn / a
	rest := fullTurn - steps*2*a
	chord := func(t int64) float64 {
		return 2 * r * math.Sin(float64(t)*math.Pi/fullTurn)
	}
	fmt.Printf("%.7f\n", r+float64(steps-1)*chord(2*a)+chord(rest))
}
