package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	neg   = -(1 << 62)
	kinds = 3 // a count of teams: none, one, two or more
)

// tree over f: every node keeps its total, its count of teams (capped at
// 2), its best prefix and suffix with exactly 0, 1 or 2+ teams, and its
// best range with at least two teams
type tree struct {
	size        int
	total, best []int64
	kind        []int
	pre, suf    [kinds][]int64
}

func (t *tree) reset() {
	for v := range t.total {
		t.total[v], t.kind[v], t.best[v] = 0, 0, neg
		for k := 0; k < kinds; k++ {
			t.pre[k][v], t.suf[k][v] = neg, neg
		}
		t.pre[0][v], t.suf[0][v] = 0, 0
	}
}

func max64(x, y int64) int64 {
	if x > y {
		return x
	}
	return y
}

func min2(x int) int {
	if x > 2 {
		return 2
	}
	return x
}

func (t *tree) pull(v int) {
	a, b := 2*v, 2*v+1
	t.total[v] = t.total[a] + t.total[b]
	t.kind[v] = min2(t.kind[a] + t.kind[b])
	for k := 0; k < kinds; k++ {
		t.pre[k][v], t.suf[k][v] = t.pre[k][a], t.suf[k][b]
	}
	for j := 0; j < kinds; j++ {
		// prefixes: inside the left child, or all of it and more
		if t.pre[j][b] != neg {
			k := min2(t.kind[a] + j)
			t.pre[k][v] = max64(t.pre[k][v], t.total[a]+t.pre[j][b])
		}
		if t.suf[j][a] != neg {
			k := min2(t.kind[b] + j)
			t.suf[k][v] = max64(t.suf[k][v], t.suf[j][a]+t.total[b])
		}
	}
	// ranges: inside a child, or across with two or more teams
	top := max64(t.best[a], t.best[b])
	for i := 0; i < kinds; i++ {
		for j := 2 - i; j < kinds; j++ {
			if j >= 0 && t.suf[i][a] != neg && t.pre[j][b] != neg {
				top = max64(top, t.suf[i][a]+t.pre[j][b])
			}
		}
	}
	t.best[v] = top
}

func (t *tree) add(fi int, s int64) {
	v := t.size + fi
	t.total[v] += s
	t.kind[v] = min2(t.kind[v] + 1)
	for k := 0; k < kinds; k++ {
		t.pre[k][v] = neg
		if k == t.kind[v] {
			t.pre[k][v] = t.total[v]
		}
		t.suf[k][v] = t.pre[k][v]
	}
	t.best[v] = neg
	if t.kind[v] == 2 {
		t.best[v] = t.total[v]
	}
	for v /= 2; v > 0; v /= 2 {
		t.pull(v)
	}
}

func distinct(values []int64) []int64 {
	sorted := append([]int64(nil), values...)
	sort.Slice(sorted, func(i, j int) bool { return sorted[i] < sorted[j] })
	k := 0
	for i, x := range sorted {
		if i == 0 || x != sorted[k-1] {
			sorted[k] = x
			k++
		}
	}
	return sorted[:k]
}

func position(values []int64, x int64) int {
	return sort.Search(len(values), func(i int) bool { return values[i] >= x })
}

type team struct {
	fi int
	s  int64
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	a, f, s := make([]int64, n), make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &a[i], &f[i], &s[i])
	}
	ages, fs := distinct(a), distinct(f)
	byAge := make([][]team, len(ages))
	for i := 0; i < n; i++ {
		ai := position(ages, a[i])
		byAge[ai] = append(byAge[ai], team{position(fs, f[i]), s[i]})
	}
	t := &tree{size: 1}
	for t.size < len(fs) {
		t.size *= 2
	}
	t.total, t.best, t.kind = make([]int64, 2*t.size), make([]int64, 2*t.size), make([]int, 2*t.size)
	for k := 0; k < kinds; k++ {
		t.pre[k], t.suf[k] = make([]int64, 2*t.size), make([]int64, 2*t.size)
	}
	answer := int64(neg)
	bestLeft, bestRight := 0, 0
	for left := range ages {
		t.reset()
		for right := left; right < len(ages); right++ {
			for _, tm := range byAge[right] {
				t.add(tm.fi, tm.s)
			}
			if t.best[1] > answer {
				answer, bestLeft, bestRight = t.best[1], left, right
			}
		}
	}
	// the range of f values with the largest total holding at least two
	// teams: for each right end the best left end has the least prefix sum
	// among those leaving at least two teams inside
	nf := len(fs)
	prefix, inside := make([]int64, nf+1), make([]int, nf+1)
	for r := bestLeft; r <= bestRight; r++ {
		for _, tm := range byAge[r] {
			prefix[tm.fi+1] += tm.s
			inside[tm.fi+1]++
		}
	}
	for i := 0; i < nf; i++ {
		prefix[i+1] += prefix[i]
		inside[i+1] += inside[i]
	}
	top, low := int64(neg), int64(neg)
	lo, hi, lowAt := 0, 0, 0
	for r, t := 1, 0; r <= nf; r++ {
		for ; t < r && inside[t] <= inside[r]-2; t++ {
			if low == neg || prefix[t] < low {
				low, lowAt = prefix[t], t
			}
		}
		if low != neg && prefix[r]-low > top {
			top, lo, hi = prefix[r]-low, lowAt, r-1
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fprintln(w, ages[bestLeft], ages[bestRight])
	fmt.Fprintln(w, fs[lo], fs[hi])
}
