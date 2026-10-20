package main

import "fmt"

const (
	digits = 4
	base   = 256
)

func main() {
	var kind string
	var v uint64
	fmt.Scan(&kind, &v)
	// Both directions reverse the four base-256 digits, so the type does not matter.
	var sent uint64
	for i := 0; i < digits; i++ {
		sent = sent*base + v%base
		v /= base
	}
	fmt.Println(sent)
}
