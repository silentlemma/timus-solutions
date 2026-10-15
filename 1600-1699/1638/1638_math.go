package main

import "fmt"

func main() {
	var pages, cover, start, stop int
	if _, err := fmt.Scan(&pages, &cover, &start, &stop); err != nil {
		return
	}
	// on a shelf a volume's first page faces its right neighbour and its
	// last page faces the left one
	whole := pages + 2*cover
	var length int
	switch {
	case start == stop:
		length = pages
	case start < stop:
		length = 2*cover + (stop-start-1)*whole
	default:
		length = 2*pages + 2*cover + (start-stop-1)*whole
	}
	fmt.Println(length)
}
