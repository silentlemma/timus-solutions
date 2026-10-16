package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const word = 64

type edge struct{ cost, from, to int }

func main() {
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Split(bufio.ScanWords)
	next := func() int {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return v
	}
	n, k := next(), next()
	cheapest := map[int]int{}
	for i := 0; i < k; i++ {
		x, y, c := next(), next(), next()
		key := (x-1)*n + y - 1
		if old, ok := cheapest[key]; !ok || c < old {
			cheapest[key] = c
		}
	}
	// the edges sorted by cost; the first m of them are those of cost up to
	// the m-th cost
	edges := make([]edge, 0, len(cheapest))
	for key, c := range cheapest {
		edges = append(edges, edge{c, key / n, key % n})
	}
	sort.Slice(edges, func(a, b int) bool { return edges[a].cost < edges[b].cost })
	words, total := (n+word-1)/word, len(edges)
	// reach[x]: the targets x pays for, as a bit set
	reach := make([][]uint64, n)
	for x := range reach {
		reach[x] = make([]uint64, words)
	}
	size := make([]int, n)
	into := make([][][2]int, n) // (edge index, operator)
	for i, e := range edges {
		into[e.to] = append(into[e.to], [2]int{i, e.from})
	}
	// the target with the fewest ways in comes first when picking a witness
	rare := make([]int, n)
	for y := range rare {
		rare[y] = y
	}
	sort.Slice(rare, func(a, b int) bool { return len(into[rare[a]]) < len(into[rare[b]]) })
	full := make([]uint64, words)
	for w := range full {
		full[w] = ^uint64(0)
	}
	if n%word != 0 {
		full[words-1] = 1<<uint(n%word) - 1
	}
	missing := make([]uint64, words)
	half := (n + 1) / 2

	feasible := func(m int) bool {
		for a := 0; a < n; a++ {
			// one operator of a covering pair pays for at least half
			if size[a] < half {
				continue
			}
			any := false
			for w := range missing {
				missing[w] = full[w] ^ reach[a][w]
				any = any || missing[w] != 0
			}
			if !any {
				return true
			}
			t := 0
			for _, y := range rare {
				if missing[y/word]>>uint(y%word)&1 == 1 {
					t = y
					break
				}
			}
			for _, pair := range into[t] {
				if pair[0] >= m {
					continue
				}
				covers := true
				for w := 0; w < words && covers; w++ {
					covers = reach[pair[1]][w]&missing[w] == missing[w]
				}
				if covers {
					return true
				}
			}
		}
		return false
	}
	// take the edges between two prefixes in or out
	now := 0
	move := func(to int) {
		for ; now < to; now++ {
			e := edges[now]
			reach[e.from][e.to/word] ^= 1 << uint(e.to%word)
			size[e.from]++
		}
		for ; now > to; now-- {
			e := edges[now-1]
			reach[e.from][e.to/word] ^= 1 << uint(e.to%word)
			size[e.from]--
		}
	}
	move(total)
	if total == 0 || !feasible(total) {
		fmt.Println("No solution")
		return
	}
	lo, hi := 1, total
	for lo < hi {
		mid := (lo + hi) / 2
		move(mid)
		if feasible(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	fmt.Println(edges[lo-1].cost)
}
