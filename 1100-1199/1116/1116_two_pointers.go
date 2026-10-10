package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type piece struct{ a, b, y int }

func read(in *bufio.Reader) []piece {
	var n int
	fmt.Fscan(in, &n)
	f := make([]piece, n)
	for i := range f {
		fmt.Fscan(in, &f[i].a, &f[i].b, &f[i].y)
	}
	return f
}

func main() {
	in := bufio.NewReader(os.Stdin)
	first, second := read(in), read(in)
	var out []piece
	j := 0
	for _, p := range first {
		cur := p.a
		// walk through [a, b) and keep what no interval of the second covers
		for cur < p.b {
			for j < len(second) && second[j].b <= cur {
				j++
			}
			if j < len(second) && second[j].a <= cur {
				cur = second[j].b
				continue
			}
			end := p.b
			if j < len(second) && second[j].a < end {
				end = second[j].a
			}
			out = append(out, piece{cur, end, p.y})
			cur = end
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.WriteString(strconv.Itoa(len(out)))
	for _, p := range out {
		fmt.Fprintf(w, " %d %d %d", p.a, p.b, p.y)
	}
	w.WriteString("\n")
}
