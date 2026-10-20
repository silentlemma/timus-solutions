package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strings"
)

const (
	side       = 3 // seats on each side of the aisle
	masks      = 1 << side
	rightStart = 6 // the right seats in a row description
	letters    = "ABCDEF"
)

// bestSide returns the largest set of free, pairwise non-adjacent seats on one
// side, as a mask per row; seats in a row and in the next row may not share a
// column or stand next to each other.
func bestSide(rows []string, offset int) []int {
	n := len(rows)
	best := make([][masks]int, n+1)
	from := make([][masks]int, n+1)
	for r := range best {
		for m := range best[r] {
			best[r][m] = -1
		}
	}
	best[0][0] = 0
	for r, row := range rows {
		free := 0
		for s := 0; s < side; s++ {
			if row[offset+s] == '.' {
				free |= 1 << s
			}
		}
		for cur := 0; cur < masks; cur++ {
			if cur&^free != 0 || cur&(cur<<1) != 0 {
				continue
			}
			count := bits.OnesCount(uint(cur))
			for prev := 0; prev < masks; prev++ {
				if best[r][prev] < 0 || (prev|prev<<1|prev>>1)&cur != 0 {
					continue
				}
				if best[r][prev]+count > best[r+1][cur] {
					best[r+1][cur] = best[r][prev] + count
					from[r+1][cur] = prev
				}
			}
		}
	}
	mask := 0
	for m := 0; m < masks; m++ {
		if best[n][m] > best[n][mask] {
			mask = m
		}
	}
	chosen := make([]int, n)
	for r := n; r > 0; r-- {
		chosen[r-1] = mask
		mask = from[r][mask]
	}
	return chosen
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(reader, &n, &k)
	rows := make([]string, n)
	for i := range rows {
		fmt.Fscan(reader, &rows[i])
	}
	var seats []string
	for half := 0; half < 2; half++ {
		chosen := bestSide(rows, half*rightStart)
		for r := 0; r < n; r++ {
			for s := 0; s < side; s++ {
				if chosen[r]>>s&1 == 1 {
					seats = append(seats, fmt.Sprintf("%d%c", r+1, letters[half*side+s]))
				}
			}
		}
	}
	if len(seats) < k {
		fmt.Println("PORAZHENIE")
		return
	}
	fmt.Println("POBEDA\n" + strings.Join(seats[:k], "\n"))
}
