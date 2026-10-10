package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"math/big"
	"os"
)

func main() {
	// letters may be any bytes above 32, so the input is read as bytes
	data, _ := ioutil.ReadAll(os.Stdin)
	var lines [][]byte
	for _, line := range bytes.Split(data, []byte("\n")) {
		lines = append(lines, bytes.TrimFunc(line, func(r rune) bool { return r <= ' ' }))
	}
	var n, m, p int
	fmt.Sscan(string(lines[0]), &n, &m, &p)
	letters := lines[1]
	index := map[byte]int{}
	for k := 0; k < n; k++ {
		index[letters[k]] = k
	}
	var words [][]byte
	for _, line := range lines[2:] {
		if len(line) > 0 && len(words) < p {
			words = append(words, line)
		}
	}
	// Aho-Corasick automaton over the forbidden words; a state is bad when
	// some word ends there
	newState := func() []int {
		row := make([]int, n)
		for c := range row {
			row[c] = -1
		}
		return row
	}
	goTo, bad := [][]int{newState()}, []bool{false}
	for _, w := range words {
		s := 0
		for _, c := range w {
			if goTo[s][index[c]] < 0 {
				goTo[s][index[c]] = len(goTo)
				goTo = append(goTo, newState())
				bad = append(bad, false)
			}
			s = goTo[s][index[c]]
		}
		bad[s] = true
	}
	fail := make([]int, len(goTo))
	var queue []int
	for c := 0; c < n; c++ {
		if goTo[0][c] < 0 {
			goTo[0][c] = 0
		} else {
			queue = append(queue, goTo[0][c])
		}
	}
	for len(queue) > 0 {
		s := queue[0]
		queue = queue[1:]
		bad[s] = bad[s] || bad[fail[s]]
		for c := 0; c < n; c++ {
			if t := goTo[s][c]; t < 0 {
				goTo[s][c] = goTo[fail[s]][c]
			} else {
				fail[t] = goTo[fail[s]][c]
				queue = append(queue, t)
			}
		}
	}
	// count the sentences letter by letter, never stepping into a bad state
	ways := make([]*big.Int, len(goTo))
	for s := range ways {
		ways[s] = new(big.Int)
	}
	ways[0].SetInt64(1)
	for step := 0; step < m; step++ {
		next := make([]*big.Int, len(goTo))
		for s := range next {
			next[s] = new(big.Int)
		}
		for s, w := range ways {
			if w.Sign() > 0 {
				for _, t := range goTo[s] {
					if !bad[t] {
						next[t].Add(next[t], w)
					}
				}
			}
		}
		ways = next
	}
	total := new(big.Int)
	for _, w := range ways {
		total.Add(total, w)
	}
	fmt.Println(total.String())
}
