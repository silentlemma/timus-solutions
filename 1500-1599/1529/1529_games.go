package main

import (
	"fmt"
	"sort"
	"strings"
)

var (
	k                    int
	bound, radix, grundy []int
	cutsOf               [][]int // legal cuts by edge length
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func offset(x []int) int {
	idx := 0
	for i, v := range x {
		idx += v * radix[i]
	}
	return idx
}

// advance steps x through all tuples below dims, last axis fastest, and
// reports false when done.
func advance(x, dims []int) bool {
	i := len(dims) - 1
	for i >= 0 {
		x[i]++
		if x[i] < dims[i] {
			return true
		}
		x[i] = 0
		i--
	}
	return false
}

// cutValues gives the XOR over all parts for every tuple of cuts, last cut
// fastest, from the values of the parts by piece lengths: each axis in turn
// is replaced by its cuts, a cut c of an edge d joining pieces c - 1, d - c.
func cutValues(table, dims []int) []int {
	sizes := append([]int(nil), dims...)
	for axis := k - 1; axis >= 0; axis-- {
		inner := 1
		for _, s := range sizes[axis+1:] {
			inner *= s
		}
		d := sizes[axis]
		cuts := cutsOf[d]
		out := make([]int, 0, len(table)/d*len(cuts))
		for start := 0; start < len(table); start += d * inner {
			for _, c := range cuts {
				low, high := start+(c-1)*inner, start+(d-c)*inner
				for j := 0; j < inner; j++ {
					out = append(out, table[low+j]^table[high+j])
				}
			}
		}
		table = out
		sizes[axis] = len(cuts)
	}
	return table
}

// nextPermutation turns a into the next ordering, false after the last one.
func nextPermutation(a []int) bool {
	i := len(a) - 2
	for i >= 0 && a[i] >= a[i+1] {
		i--
	}
	if i < 0 {
		return false
	}
	j := len(a) - 1
	for a[j] <= a[i] {
		j--
	}
	a[i], a[j] = a[j], a[i]
	for l, r := i+1, len(a)-1; l < r; l, r = l+1, r-1 {
		a[l], a[r] = a[r], a[l]
	}
	return true
}

func main() {
	fmt.Scan(&k)
	edges := make([]int, k)
	hasOne := false
	for i := range edges {
		fmt.Scan(&edges[i])
		hasOne = hasOne || edges[i] == 1
	}
	if k == 1 {
		// pieces of a segment of length d total d - 1, so by induction its
		// value is d mod 2, and from an odd length every cut wins
		if edges[0]%2 == 1 {
			fmt.Println("1\n1")
		} else {
			fmt.Println(2)
		}
		return
	}
	if hasOne {
		// any cut empties a box with an edge of 1, so Alice cuts and wins
		fmt.Println(1)
		fmt.Println(strings.TrimSpace(strings.Repeat("1 ", k)))
		return
	}
	// every ordering of a box's edges is stored with the same value, indexed
	// by a mixed radix over the sorted edges of the whole box
	bound = append([]int(nil), edges...)
	sort.Ints(bound)
	radix = make([]int, k)
	radix[k-1] = 1
	for i := k - 2; i >= 0; i-- {
		radix[i] = radix[i+1] * (bound[i+1] + 1)
	}
	grundy = make([]int, radix[0]*(bound[0]+1)) // boxes with an empty edge stay 0
	longest := bound[k-1]
	cutsOf = make([][]int, longest+1)
	for d := 2; d <= longest; d++ {
		for c := 1; c <= d; c++ {
			if (c > 1 && gcd(c-1, d) == 1) || (d > c && gcd(d-c, d) == 1) {
				cutsOf[d] = append(cutsOf[d], c)
			}
		}
	}
	// the boxes with sorted edges, smaller ones first
	var boxes [][]int
	box := make([]int, k)
	for {
		b := make([]int, k)
		for i := range b {
			b[i] = box[i] + 1
		}
		if sort.IntsAreSorted(b) {
			boxes = append(boxes, b)
		}
		if !advance(box, bound) {
			break
		}
	}
	sum := func(b []int) int {
		s := 0
		for _, v := range b {
			s += v
		}
		return s
	}
	sort.SliceStable(boxes, func(i, j int) bool { return sum(boxes[i]) < sum(boxes[j]) })
	seen := make([]int, len(grundy)+2)
	stamp := 0
	for _, b := range boxes {
		g := 0
		movable := true
		for _, d := range b {
			movable = movable && len(cutsOf[d]) > 0
		}
		if b[0] == 1 {
			g = 1
		} else if movable {
			// the parts by piece lengths, a row along the last axis at a time
			var table []int
			prefix := make([]int, k)
			head := b[:k-1]
			for {
				base := offset(prefix)
				table = append(table, grundy[base:base+b[k-1]]...)
				if !advance(prefix[:k-1], head) {
					break
				}
			}
			stamp++
			for _, v := range cutValues(table, b) {
				seen[v] = stamp
			}
			for seen[g] == stamp {
				g++
			}
		}
		// only orderings within the bounds are ever looked up
		for {
			fits := true
			for i := range b {
				fits = fits && b[i] <= bound[i]
			}
			if fits {
				grundy[offset(b)] = g
			}
			if !nextPermutation(b) {
				break
			}
		}
	}
	if grundy[offset(bound)] == 0 {
		fmt.Println(2)
		return
	}
	// the first winning cut in lexicographic order, in the input's order
	var table []int
	x := make([]int, k)
	for {
		sorted := append([]int(nil), x...)
		sort.Ints(sorted)
		table = append(table, grundy[offset(sorted)])
		if !advance(x, edges) {
			break
		}
	}
	counts := make([]int, k)
	for i, e := range edges {
		counts[i] = len(cutsOf[e])
	}
	pos := make([]int, k)
	for _, v := range cutValues(table, edges) {
		if v == 0 {
			fmt.Println(1)
			parts := make([]string, k)
			for i := range parts {
				parts[i] = fmt.Sprint(cutsOf[edges[i]][pos[i]])
			}
			fmt.Println(strings.Join(parts, " "))
			return
		}
		advance(pos, counts)
	}
}
