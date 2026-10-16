package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	mod   = 3
	shift = 32
)

// vec keeps a vector over GF(3) as the masks of coordinates equal to 1
// and to 2
type vec struct{ one, two uint32 }

func add(a, b vec) vec {
	t := (a.one | b.two) ^ (a.two | b.one)
	return vec{(a.two | b.two) ^ t, (a.one | b.one) ^ t}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var k, n int
	if _, err := fmt.Fscan(reader, &k, &n); err != nil {
		return
	}
	m := make([][]int, n)
	for j := range m {
		m[j] = make([]int, k)
	}
	target := make([]int, k)
	for i := 0; i < k; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(reader, &m[j][i])
		}
		fmt.Fscan(reader, &target[i])
	}
	// vectors w that are orthogonal to the column of every variable span the
	// null space of the transposed matrix, and y is Ax for some x exactly when
	// every such w is orthogonal to y
	var pivots []int
	isPivot := make([]bool, k)
	for c := 0; c < k; c++ {
		r, sel := len(pivots), -1
		for i := r; i < n && sel == -1; i++ {
			if m[i][c] != 0 {
				sel = i
			}
		}
		if sel == -1 {
			continue
		}
		m[r], m[sel] = m[sel], m[r]
		if m[r][c] == 2 {
			for j := range m[r] {
				m[r][j] = m[r][j] * 2 % mod
			}
		}
		for i := 0; i < n; i++ {
			if i == r || m[i][c] == 0 {
				continue
			}
			f := m[i][c]
			for j := 0; j < k; j++ {
				m[i][j] = ((m[i][j]-f*m[r][j])%mod + mod) % mod
			}
		}
		pivots = append(pivots, c)
		isPivot[c] = true
	}
	rank := len(pivots)
	var basis [][]int
	for free := 0; free < k; free++ {
		if isPivot[free] {
			continue
		}
		w := make([]int, k)
		w[free] = 1
		for i, c := range pivots {
			w[c] = (mod - m[i][free]) % mod
		}
		basis = append(basis, w)
	}
	// the change that y_i = 1 makes to the syndromes w . y over the basis,
	// and y_i = 2 makes the opposite change, the two masks swapped
	unit := make([]vec, k)
	for i := 0; i < k; i++ {
		for j, w := range basis {
			if w[i] == 1 {
				unit[i].one |= 1 << uint(j)
			} else if w[i] == 2 {
				unit[i].two |= 1 << uint(j)
			}
		}
	}
	syndromes := func(from, to int) []vec {
		sums := []vec{{}}
		for i := from; i < to; i++ {
			var next []vec
			for _, s := range sums {
				for v := 0; v < mod; v++ {
					switch {
					case v == target[i]:
					case v == 0:
						next = append(next, s)
					case v == 1:
						next = append(next, add(s, unit[i]))
					default:
						next = append(next, add(s, vec{unit[i].two, unit[i].one}))
					}
				}
			}
			sums = next
		}
		return sums
	}
	// every y_i has two allowed values: meet in the middle on syndromes
	half := k / 2
	var left []uint64
	for _, s := range syndromes(0, half) {
		left = append(left, uint64(s.one)<<shift|uint64(s.two))
	}
	sort.Slice(left, func(a, b int) bool { return left[a] < left[b] })
	total := int64(0)
	for _, s := range syndromes(half, k) {
		key := uint64(s.two)<<shift | uint64(s.one)
		lo := sort.Search(len(left), func(i int) bool { return left[i] >= key })
		hi := sort.Search(len(left), func(i int) bool { return left[i] > key })
		total += int64(hi - lo)
	}
	for i := rank; i < n; i++ {
		total *= mod
	}
	fmt.Println(total)
}
