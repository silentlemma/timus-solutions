package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const short = 3 // any three points on both sides match

type dir struct{ p, q int64 }

func gcd(a, b int64) int64 {
	if a < 0 {
		a = -a
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// directions: the distinct directions as reduced p / q with q > 0, by increasing p / q.
func directions(trees []dir) []dir {
	for i, t := range trees {
		if t.q < 0 {
			t = dir{-t.p, -t.q}
		}
		g := gcd(t.p, t.q)
		trees[i] = dir{t.p / g, t.q / g}
	}
	sort.Slice(trees, func(i, j int) bool { return trees[i].p*trees[j].q < trees[j].p*trees[i].q })
	var out []dir
	for _, t := range trees {
		if len(out) == 0 || out[len(out)-1] != t {
			out = append(out, t)
		}
	}
	return out
}

// ratios: cross-ratio of every four consecutive directions, as small integer ids.
func ratios(d []dir, ids map[[2]int64]int) []int {
	var out []int
	for i := 0; i+short < len(d); i++ {
		a, b, c, e := d[i], d[i+1], d[i+2], d[i+short]
		// (c - a)(d - b) / ((c - b)(d - a)); the denominators q cancel
		num := (c.p*a.q - a.p*c.q) * (e.p*b.q - b.p*e.q)
		den := (c.p*b.q - b.p*c.q) * (e.p*a.q - a.p*e.q)
		g := gcd(num, den)
		key := [2]int64{num / g, den / g}
		id, ok := ids[key]
		if !ok {
			id = len(ids)
			ids[key] = id
		}
		out = append(out, id)
	}
	return out
}

// longestCommon: longest common substring of two sequences, by a suffix automaton of a.
func longestCommon(a, b []int, symbols int64) int {
	link, length, head := []int{-1}, []int{0}, []int{-1}
	var edgeSymbol, edgeNext []int
	// trans[state * symbols + symbol]: the next state; each state lists its symbols
	trans := map[int64]int{}
	key := func(state, symbol int) int64 { return int64(state)*symbols + int64(symbol) }
	add := func(state, symbol, target int) {
		trans[key(state, symbol)] = target
		edgeSymbol = append(edgeSymbol, symbol)
		edgeNext = append(edgeNext, head[state])
		head[state] = len(edgeSymbol) - 1
	}
	last := 0
	for _, ch := range a {
		cur := len(length)
		length = append(length, length[last]+1)
		link = append(link, 0)
		head = append(head, -1)
		p := last
		for p != -1 {
			if _, ok := trans[key(p, ch)]; ok {
				break
			}
			add(p, ch, cur)
			p = link[p]
		}
		if p != -1 {
			q := trans[key(p, ch)]
			if length[p]+1 == length[q] {
				link[cur] = q
			} else {
				clone := len(length)
				length = append(length, length[p]+1)
				link = append(link, link[q])
				head = append(head, -1)
				for e := head[q]; e != -1; e = edgeNext[e] {
					add(clone, edgeSymbol[e], trans[key(q, edgeSymbol[e])])
				}
				for p != -1 {
					if t, ok := trans[key(p, ch)]; !ok || t != q {
						break
					}
					trans[key(p, ch)] = clone
					p = link[p]
				}
				link[q], link[cur] = clone, clone
			}
		}
		last = cur
	}
	best, state, run := 0, 0, 0
	for _, ch := range b {
		for state != 0 {
			if _, ok := trans[key(state, ch)]; ok {
				break
			}
			state = link[state]
			run = length[state]
		}
		if t, ok := trans[key(state, ch)]; ok {
			state = t
			run++
		}
		if run > best {
			best = run
		}
	}
	return best
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	var upper, lower []dir
	for sc.Scan() {
		xi, _ := strconv.Atoi(sc.Text())
		sc.Scan()
		yi, _ := strconv.Atoi(sc.Text())
		x, y := int64(xi), int64(yi)
		if x == 0 && y == 0 {
			break
		}
		if y > 0 {
			upper = append(upper, dir{x, y})
		} else {
			lower = append(lower, dir{x, y})
		}
	}
	up, low := directions(upper), directions(lower)
	answer := short
	if len(up) < answer {
		answer = len(up)
	}
	if len(low) < answer {
		answer = len(low)
	}
	if len(up) > short && len(low) > short {
		ids := map[[2]int64]int{}
		ra, rb := ratios(up, ids), ratios(low, ids)
		if common := longestCommon(ra, rb, int64(len(ids))); common > 0 {
			answer = common + short
		}
	}
	fmt.Println(answer)
}
