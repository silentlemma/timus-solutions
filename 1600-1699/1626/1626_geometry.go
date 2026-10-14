package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

const word = 64

var (
	n, words int
	xs, ys   []int
	lastMask uint64
)

func cross(ox, oy, ax, ay, bx, by int) int {
	return (ax-ox)*(by-oy) - (ay-oy)*(bx-ox)
}

func set(b []uint64, k int)      { b[k/word] |= 1 << uint(k%word) }
func has(b []uint64, k int) bool { return b[k/word]>>uint(k%word)&1 != 0 }
func clear(b []uint64, k int)    { b[k/word] &^= 1 << uint(k%word) }

// inCone: j lies strictly inside the interior angle of the polygon at i.
func inCone(i, j int) bool {
	prv, nxt := (i+n-1)%n, (i+1)%n
	base := cross(xs[i], ys[i], xs[nxt], ys[nxt], xs[prv], ys[prv])
	toNext := cross(xs[i], ys[i], xs[nxt], ys[nxt], xs[j], ys[j])
	toPrev := cross(xs[i], ys[i], xs[prv], ys[prv], xs[j], ys[j])
	if base >= 0 {
		return toNext > 0 && toPrev < 0
	}
	return toNext > 0 || toPrev < 0
}

func main() {
	in := bufio.NewReader(os.Stdin)
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	xs, ys = make([]int, n), make([]int, n)
	orig := make([]int, n)
	area := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &xs[i], &ys[i])
		orig[i] = i
	}
	var sx1, sy1, sx2, sy2 int
	fmt.Fscan(in, &sx1, &sy1, &sx2, &sy2)
	for i := 0; i < n; i++ {
		j := (i + 1) % n
		area += xs[i]*ys[j] - xs[j]*ys[i]
	}
	if area < 0 { // counterclockwise from now on
		for l, r := 0, n-1; l < r; l, r = l+1, r-1 {
			xs[l], xs[r] = xs[r], xs[l]
			ys[l], ys[r] = ys[r], ys[l]
			orig[l], orig[r] = orig[r], orig[l]
		}
	}
	words = (n + word - 1) / word
	lastMask = ^uint64(0)
	if n%word != 0 {
		lastMask = 1<<uint(n%word) - 1
	}
	row := func(arr []uint64, i int) []uint64 { return arr[i*words : (i+1)*words] }

	// left[a][b] for a < b: the vertices strictly left of the line a -> b
	pairIndex := make([]int, n*n)
	pairs := 0
	for a := 0; a < n; a++ {
		for b := a + 1; b < n; b++ {
			pairIndex[a*n+b], pairIndex[b*n+a] = pairs, pairs
			pairs++
		}
	}
	left := make([]uint64, pairs*words)
	for a := 0; a < n; a++ {
		for b := a + 1; b < n; b++ {
			bs := row(left, pairIndex[a*n+b])
			for k := 0; k < n; k++ {
				if cross(xs[a], ys[a], xs[b], ys[b], xs[k], ys[k]) > 0 {
					set(bs, k)
				}
			}
		}
	}
	// strictlyLeft writes the vertices strictly left of a -> b into out; for
	// a > b it is the complement of the other side, which also counts the
	// points on the line, so it is used only where those cannot occur
	strictlyLeft := func(a, b int, out []uint64) {
		src := row(left, pairIndex[a*n+b])
		for w := range out {
			if a < b {
				out[w] = src[w]
			} else {
				out[w] = ^src[w]
			}
		}
		out[words-1] &= lastMask
	}
	edgeLeft := make([]uint64, n*words) // bit k: the vertex is strictly left of edge k -> k + 1
	for v := 0; v < n; v++ {
		for k := 0; k < n; k++ {
			kn := (k + 1) % n
			if cross(xs[k], ys[k], xs[kn], ys[kn], xs[v], ys[v]) > 0 {
				set(row(edgeLeft, v), k)
			}
		}
	}

	// vis[a]: the vertices joined to a by an edge or a diagonal
	vis := make([]uint64, n*words)
	for i := 0; i < n; i++ {
		set(row(vis, i), (i+1)%n)
		set(row(vis, (i+1)%n), i)
	}
	line := make([]uint64, words)
	hits := make([]uint64, words)
	for i := 0; i < n; i++ {
		for j := i + 2; j < n; j++ {
			if (j+1)%n == i || !inCone(i, j) || !inCone(j, i) {
				continue
			}
			copy(line, row(left, pairIndex[i*n+j]))
			// edges whose ends lie on different sides of the line, and whose
			// line separates i from j; those touching i or j cannot cross
			eli, elj := row(edgeLeft, i), row(edgeLeft, j)
			for w := 0; w < words; w++ {
				shifted := line[w] >> 1
				if w+1 < words {
					shifted |= line[w+1] << (word - 1)
				}
				hits[w] = (line[w] ^ shifted) & (eli[w] ^ elj[w])
			}
			if has(line, 0) != has(line, n-1) { // edge n - 1 -> 0 wraps around
				set(hits, n-1)
			} else {
				clear(hits, n-1)
			}
			hits[words-1] &= lastMask
			if !(has(eli, n-1) != has(elj, n-1)) {
				clear(hits, n-1)
			}
			for _, k := range []int{(i + n - 1) % n, i, (j + n - 1) % n, j} {
				clear(hits, k)
			}
			crossing := false
			for w := 0; w < words && !crossing; w++ {
				for m := hits[w]; m != 0; m &= m - 1 {
					k := w*word + bits.TrailingZeros64(m)
					kn := (k + 1) % n
					d1 := cross(xs[i], ys[i], xs[j], ys[j], xs[k], ys[k])
					d2 := cross(xs[i], ys[i], xs[j], ys[j], xs[kn], ys[kn])
					if (d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0) {
						crossing = true
						break
					}
				}
			}
			if crossing {
				continue
			}
			// no vertex may lie on the open segment
			blocked := false
			for k := 0; k < n && !blocked; k++ {
				if k != i && k != j && cross(xs[i], ys[i], xs[j], ys[j], xs[k], ys[k]) == 0 &&
					(xs[k]-xs[i])*(xs[k]-xs[j])+(ys[k]-ys[i])*(ys[k]-ys[j]) < 0 {
					blocked = true
				}
			}
			if !blocked {
				set(row(vis, i), j)
				set(row(vis, j), i)
			}
		}
	}

	left1 := make([]uint64, n*words) // bit k: k strictly left of the line a -> s1
	left2 := make([]uint64, n*words)
	for a := 0; a < n; a++ {
		for k := 0; k < n; k++ {
			if cross(xs[a], ys[a], sx1, sy1, xs[k], ys[k]) > 0 {
				set(row(left1, a), k)
			}
			if cross(xs[a], ys[a], sx2, sy2, xs[k], ys[k]) > 0 {
				set(row(left2, a), k)
			}
		}
	}
	// a triangle a, b, k counterclockwise whose sides are edges or diagonals,
	// with both ends of S strictly inside and no vertex inside
	right1, right2 := make([]uint64, words), make([]uint64, words)
	cand, ab := make([]uint64, words), make([]uint64, words)
	bk, ka := make([]uint64, words), make([]uint64, words)
	for b := 0; b < n; b++ {
		for w := range right1 {
			right1[w], right2[w] = 0, 0
		}
		for k := 0; k < n; k++ {
			if cross(xs[b], ys[b], sx1, sy1, xs[k], ys[k]) < 0 {
				set(right1, k)
			}
			if cross(xs[b], ys[b], sx2, sy2, xs[k], ys[k]) < 0 {
				set(right2, k)
			}
		}
		for a := 0; a < n; a++ {
			if a == b || !has(row(vis, a), b) {
				continue
			}
			if cross(xs[a], ys[a], xs[b], ys[b], sx1, sy1) <= 0 ||
				cross(xs[a], ys[a], xs[b], ys[b], sx2, sy2) <= 0 {
				continue
			}
			va, vb, l1, l2 := row(vis, a), row(vis, b), row(left1, a), row(left2, a)
			for w := 0; w < words; w++ {
				cand[w] = va[w] & vb[w] & l1[w] & l2[w] & right1[w] & right2[w]
			}
			clear(cand, a)
			clear(cand, b)
			strictlyLeft(a, b, ab)
			for w := 0; w < words; w++ {
				for m := cand[w]; m != 0; m &= m - 1 {
					k := w*word + bits.TrailingZeros64(m)
					strictlyLeft(b, k, bk)
					strictlyLeft(k, a, ka)
					empty := true
					for u := 0; u < words && empty; u++ {
						inside := ab[u] & bk[u] & ka[u]
						for _, v := range []int{a, b, k} {
							if v/word == u {
								inside &^= 1 << uint(v%word)
							}
						}
						empty = inside == 0
					}
					if empty {
						fmt.Println(orig[a]+1, orig[b]+1, orig[k]+1)
						return
					}
				}
			}
		}
	}
	fmt.Println("Impossible")
}
