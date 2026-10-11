package main

import "fmt"

// The PIBAS program keeps the quote characters in C and B, so its printing
// statement needs no single quote and fits inside the single-quoted A; the
// statement prints the start of the program, then A in quotes, then A again.
const (
	head = `C="'";B='"';A='`
	tail = `;?"C="+B+C+B+";B="+C+B+C+";A="+C+A+C+A`
)

func main() {
	fmt.Println(head + tail + "'" + tail)
}
