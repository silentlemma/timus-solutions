package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

const (
	indexBits = 10 // edges are packed as length, then both indices
	indexMask = 1<<indexBits - 1
	wordBits  = 64
)

// counts are bit sets: bit k says that k bases are possible
type counts []uint64

// orShifted sets res |= a << k
func orShifted(res, a counts, k int) {
	words, bits := k/wordBits, uint(k%wordBits)
	for i := len(res) - 1; i >= words; i-- {
		v := a[i-words] << bits
		if bits > 0 && i-words-1 >= 0 {
			v |= a[i-words-1] >> (wordBits - bits)
		}
		res[i] |= v
	}
}

func solve(xs, ys []int64) string {
	n := len(xs)
	dist := func(a, b int) int64 {
		dx, dy := xs[a]-xs[b], ys[a]-ys[b]
		return dx*dx + dy*dy
	}
	var edges []int64
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			edges = append(edges, dist(i, j)<<(2*indexBits)|int64(i)<<indexBits|int64(j))
		}
	}
	sort.Slice(edges, func(a, b int) bool { return edges[a] < edges[b] })

	// the single-linkage tree: nodes 0 .. n-1 are the objects, then each
	// component formed after a group of equal distances is a new node
	kids := make([][]int, n)
	width := make([]int64, n)
	out := make([]int64, n)
	parent := make([]int, n)
	members := make([][]int, n)
	compWidth := make([]int64, n)
	compNode := make([]int, n)
	for i := 0; i < n; i++ {
		out[i] = -1
		parent[i] = i
		members[i] = []int{i}
		compNode[i] = i
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	for e := 0; e < len(edges); {
		w := edges[e] >> (2 * indexBits)
		grown := map[int][]int{} // a root -> the nodes it swallowed in this group
		for ; e < len(edges) && edges[e]>>(2*indexBits) == w; e++ {
			ra, rb := find(int(edges[e]>>indexBits&indexMask)), find(int(edges[e]&indexMask))
			if ra == rb {
				continue
			}
			far := compWidth[ra]
			if compWidth[rb] > far {
				far = compWidth[rb]
			}
			for _, p := range members[ra] {
				for _, q := range members[rb] {
					if d := dist(p, q); d > far {
						far = d
					}
				}
			}
			parent[rb] = ra
			members[ra] = append(members[ra], members[rb]...)
			compWidth[ra] = far
			swallowed, ok := grown[ra]
			if !ok {
				swallowed = []int{compNode[ra]}
			}
			if more, ok := grown[rb]; ok {
				swallowed = append(swallowed, more...)
				delete(grown, rb)
			} else {
				swallowed = append(swallowed, compNode[rb])
			}
			grown[ra] = swallowed
		}
		for root, swallowed := range grown {
			for _, c := range swallowed {
				out[c] = w
			}
			compNode[root] = len(kids)
			kids = append(kids, swallowed)
			width = append(width, compWidth[root])
			out = append(out, -1)
		}
	}

	// a node can be a base when it is narrower than its distance to the rest
	size := (n + 1 + wordBits - 1) / wordBits
	all := make([]counts, len(kids))
	for v := range kids {
		all[v] = make(counts, size)
		if out[v] < 0 || width[v] < out[v] {
			all[v][0] |= 1 << 1
		}
		if len(kids[v]) == 0 {
			continue
		}
		total := make(counts, size)
		total[0] = 1
		for _, c := range kids[v] {
			combined := make(counts, size)
			for k := 1; k <= n; k++ {
				if all[c][k/wordBits]>>(k%wordBits)&1 == 1 {
					orShifted(combined, total, k)
				}
			}
			total = combined
		}
		for i := range total {
			all[v][i] |= total[i]
		}
	}
	root := all[len(all)-1]
	var s strings.Builder
	for k := 1; k <= n; k++ {
		s.WriteByte(byte('0' + root[k/wordBits]>>(k%wordBits)&1))
	}
	return s.String()
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for {
		var n int
		if _, err := fmt.Fscan(reader, &n); err != nil || n == 0 {
			return
		}
		xs, ys := make([]int64, n), make([]int64, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &xs[i], &ys[i])
		}
		fmt.Fprintln(writer, solve(xs, ys))
	}
}
