package main

import (
	"bufio"
	"os"
	"strconv"
)

type sign struct{ count, kind int }

// typed heap operations avoid boxing a sign for every push and pop.
type pile []sign

func (p pile) down(i, n int) {
	for 2*i+1 < n {
		child := 2*i + 1
		if child+1 < n && p[child+1].count > p[child].count {
			child++
		}
		if p[child].count <= p[i].count {
			break
		}
		p[i], p[child] = p[child], p[i]
		i = child
	}
}

func (p *pile) push(s sign) {
	*p = append(*p, s)
	for i := len(*p) - 1; i > 0; {
		parent := (i - 1) / 2
		if (*p)[i].count <= (*p)[parent].count {
			break
		}
		(*p)[i], (*p)[parent] = (*p)[parent], (*p)[i]
		i = parent
	}
}

func (p *pile) pop() sign {
	n := len(*p) - 1
	(*p)[0], (*p)[n] = (*p)[n], (*p)[0]
	p.down(0, n)
	s := (*p)[n]
	*p = (*p)[:n]
	return s
}

// bufio refills as needed; no bound on whitespace or total bytes is assumed.
func nextInt(in *bufio.Reader) int {
	ch, err := in.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = in.ReadByte()
	}
	value := 0
	for err == nil && ch > ' ' {
		value = value*10 + int(ch-'0')
		ch, err = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	k := nextInt(in)
	storage := make(pile, 0, k)
	p := &storage
	for t := 1; t <= k; t++ {
		c := nextInt(in)
		*p = append(*p, sign{c, t})
	}
	for i := k/2 - 1; i >= 0; i-- {
		p.down(i, k)
	}
	prev := 0
	first := true
	for len(*p) > 0 {
		s := p.pop()
		if s.kind == prev && len(*p) > 0 {
			// the most plentiful kind was just used: take the next one
			other := p.pop()
			p.push(s)
			s = other
		}
		if !first {
			out.WriteByte(' ')
		}
		first = false
		out.WriteString(strconv.Itoa(s.kind))
		prev = s.kind
		if s.count > 1 {
			p.push(sign{s.count - 1, s.kind})
		}
	}
	out.WriteByte('\n')
}
