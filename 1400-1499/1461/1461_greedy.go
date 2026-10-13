package main

import (
	"bufio"
	"fmt"
	"os"
)

const book = "dhu" // letters in the order of the book

func step(c byte) int {
	switch c {
	case 'u':
		return 1
	case 'd':
		return -1
	}
	return 0
}

// can a garland at this height end at the ground in exactly `left` links?
// on the ground a link must go up, above it horizontal links can pad
func finishes(height, left int) bool {
	if height == 0 {
		return left == 0 || left >= 2
	}
	return left >= height
}

// never below the ground, and no horizontal link on it
func allowed(c byte, height int) bool {
	return height+step(c) >= 0 && !(c == 'h' && height == 0)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	var s string
	fmt.Fscan(reader, &n, &s)
	heights := make([]int, n+1)
	for i := 0; i < n; i++ {
		heights[i+1] = heights[i] + step(s[i])
	}
	// the last link that can take a larger letter and still be finished
	for i := n - 1; i >= 0; i-- {
		for k := 0; k < len(book); k++ {
			c := book[k]
			if c > s[i] && allowed(c, heights[i]) && finishes(heights[i]+step(c), n-i-1) {
				out := []byte(s[:i])
				out = append(out, c)
				height := heights[i] + step(c)
				// the rest is the smallest garland that still finishes
				for left := n - i - 1; left > 0; left-- {
					for j := 0; j < len(book); j++ {
						d := book[j]
						if allowed(d, height) && finishes(height+step(d), left-1) {
							out = append(out, d)
							height += step(d)
							break
						}
					}
				}
				fmt.Println(string(out))
				return
			}
		}
	}
	fmt.Println("No solution")
}
