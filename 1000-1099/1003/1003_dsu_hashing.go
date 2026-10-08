package main

import (
	"bufio"
	"fmt"
	"os"
)

const endOfInput = -1

// Disjoint sets of prefix positions; parity[x] is the parity of the number of
// ones between x and its parent.
type dsu struct {
	parent, parity, rank []int
}

func (d *dsu) add() int {
	d.parent = append(d.parent, len(d.parent))
	d.parity = append(d.parity, 0)
	d.rank = append(d.rank, 0)
	return len(d.parent) - 1
}

func (d *dsu) find(x int) (int, int) {
	if d.parent[x] == x {
		return x, 0
	}
	root, p := d.find(d.parent[x])
	d.parent[x] = root
	d.parity[x] ^= p
	return root, d.parity[x]
}

// union records that x and y differ by parity w; false on a contradiction.
func (d *dsu) union(x, y, w int) bool {
	rx, px := d.find(x)
	ry, py := d.find(y)
	if rx == ry {
		return px^py == w
	}
	if d.rank[rx] < d.rank[ry] {
		rx, ry = ry, rx
	}
	d.parent[ry] = rx
	d.parity[ry] = px ^ py ^ w
	if d.rank[rx] == d.rank[ry] {
		d.rank[rx]++
	}
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	for {
		var length, q int
		if _, err := fmt.Fscan(reader, &length); err != nil || length == endOfInput {
			return
		}
		fmt.Fscan(reader, &q)
		d := &dsu{}
		ids := make(map[int]int)
		id := func(pos int) int {
			if v, ok := ids[pos]; ok {
				return v
			}
			ids[pos] = d.add()
			return ids[pos]
		}
		answer := q
		for i := 0; i < q; i++ {
			var l, r int
			var word string
			fmt.Fscan(reader, &l, &r, &word)
			if answer != q {
				continue
			}
			w := 0
			if word == "odd" {
				w = 1
			}
			// ones in [l, r] = prefix(r) - prefix(l - 1)
			if !d.union(id(l-1), id(r), w) {
				answer = i
			}
		}
		fmt.Fprintln(writer, answer)
	}
}
