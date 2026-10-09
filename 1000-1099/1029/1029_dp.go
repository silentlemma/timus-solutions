package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const bitSize = 64

// where the cheapest way to an office comes from
const (
	start = iota
	below
	left
	right
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int64 {
		sc.Scan()
		v, _ := strconv.ParseInt(sc.Text(), 10, bitSize)
		return v
	}
	m, n := int(next()), int(next())
	best := make([][]int64, m)
	from := make([][]int, m)
	for i := range best {
		best[i] = make([]int64, n)
		from[i] = make([]int, n)
		fee := make([]int64, n)
		// from below first, then improve along the floor in both directions
		for j := range fee {
			fee[j] = next()
			best[i][j], from[i][j] = fee[j], start
			if i > 0 {
				best[i][j], from[i][j] = fee[j]+best[i-1][j], below
			}
		}
		for j := 1; j < n; j++ {
			if best[i][j-1]+fee[j] < best[i][j] {
				best[i][j], from[i][j] = best[i][j-1]+fee[j], left
			}
		}
		for j := n - 2; j >= 0; j-- {
			if best[i][j+1]+fee[j] < best[i][j] {
				best[i][j], from[i][j] = best[i][j+1]+fee[j], right
			}
		}
	}
	i, j := m-1, 0
	for k := range best[i] {
		if best[i][k] < best[i][j] {
			j = k
		}
	}
	// walk the choices back to the first floor, then print them in order
	rooms := []string{strconv.Itoa(j + 1)}
	for from[i][j] != start {
		switch from[i][j] {
		case below:
			i--
		case left:
			j--
		case right:
			j++
		}
		rooms = append(rooms, strconv.Itoa(j+1))
	}
	for a, b := 0, len(rooms)-1; a < b; a, b = a+1, b-1 {
		rooms[a], rooms[b] = rooms[b], rooms[a]
	}
	fmt.Println(strings.Join(rooms, " "))
}
