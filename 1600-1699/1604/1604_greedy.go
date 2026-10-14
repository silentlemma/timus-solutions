package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

type sign struct{ count, kind int }

// pile is a max-heap of kinds by the number of signs left.
type pile []sign

func (p pile) Len() int            { return len(p) }
func (p pile) Less(i, j int) bool  { return p[i].count > p[j].count }
func (p pile) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *pile) Push(x interface{}) { *p = append(*p, x.(sign)) }
func (p *pile) Pop() interface{} {
	old := *p
	x := old[len(old)-1]
	*p = old[:len(old)-1]
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var k int
	if _, err := fmt.Fscan(in, &k); err != nil {
		return
	}
	p := &pile{}
	for t := 1; t <= k; t++ {
		var c int
		fmt.Fscan(in, &c)
		*p = append(*p, sign{c, t})
	}
	heap.Init(p)
	prev := 0
	first := true
	for p.Len() > 0 {
		s := heap.Pop(p).(sign)
		if s.kind == prev && p.Len() > 0 {
			// the most plentiful kind was just used: take the next one
			other := heap.Pop(p).(sign)
			heap.Push(p, s)
			s = other
		}
		if !first {
			out.WriteByte(' ')
		}
		first = false
		out.WriteString(strconv.Itoa(s.kind))
		prev = s.kind
		if s.count > 1 {
			heap.Push(p, sign{s.count - 1, s.kind})
		}
	}
	out.WriteByte('\n')
}
