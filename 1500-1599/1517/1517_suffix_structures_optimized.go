package main

import (
	"bufio"
	"fmt"
	"os"
)

const edgeFactor = 3 // a suffix automaton has fewer than 3N edges

type state struct{ length, link, head int32 }
type edge struct {
	target, following int32
	letter            byte
}
type automaton struct {
	states []state
	edges  []edge
}

func (a *automaton) find(s int32, ch byte) int32 {
	// A sparse outgoing list contains at most the 26 alphabet letters.
	e := a.states[s].head
	for e >= 0 && a.edges[e].letter != ch {
		e = a.edges[e].following
	}
	return e
}

func (a *automaton) add(s int32, ch byte, target int32) {
	a.edges = append(a.edges, edge{target, a.states[s].head, ch})
	a.states[s].head = int32(len(a.edges) - 1)
}

func build(text string) *automaton {
	a := &automaton{make([]state, 1, 2*len(text)+1), make([]edge, 0, edgeFactor*len(text))}
	a.states[0] = state{0, -1, -1}
	last := int32(0)
	for i := range text {
		ch := text[i]
		current := int32(len(a.states))
		a.states = append(a.states, state{a.states[last].length + 1, 0, -1})
		s := last
		for s >= 0 && a.find(s, ch) < 0 {
			a.add(s, ch, current)
			s = a.states[s].link
		}
		if s >= 0 {
			target := a.edges[a.find(s, ch)].target
			if a.states[s].length+1 == a.states[target].length {
				a.states[current].link = target
			} else {
				clone := int32(len(a.states))
				a.states = append(a.states, state{a.states[s].length + 1, a.states[target].link, -1})
				// Copy actual edges independently, so later redirects cannot
				// accidentally modify both the original state and its clone.
				for e := a.states[target].head; e >= 0; {
					old := a.edges[e]
					a.add(clone, old.letter, old.target)
					e = old.following
				}
				for s >= 0 {
					e := a.find(s, ch)
					if e < 0 || a.edges[e].target != target {
						break
					}
					a.edges[e].target = clone
					s = a.states[s].link
				}
				a.states[target].link = clone
				a.states[current].link = clone
			}
		}
		last = current
	}
	return a
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var n int
	var first, second string
	fmt.Fscan(input, &n, &first, &second)
	a := build(first)
	s := int32(0)
	run, best, end := 0, 0, 0
	for i := range second {
		e := a.find(s, second[i])
		for s != 0 && e < 0 {
			s = a.states[s].link
			run = int(a.states[s].length)
			e = a.find(s, second[i])
		}
		if e >= 0 {
			s = a.edges[e].target
			run++
		} else {
			run = 0
		}
		if run > best {
			best, end = run, i+1
		}
	}
	fmt.Println(second[end-best : end])
}
