package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	inf  = 1 << 30
	word = 64 // documents per word of a set
)

type solver struct {
	m, week        int
	off, tail      []int
	topo, waiting  []int
	pre, succ      [][]int
	done           []bool
	bestDay        int
	bestPlan, path []int
	seen           map[[2]uint64]int
}

// firstDay is the first day from t on when the official of v receives.
func (s *solver) firstDay(t, v int) int {
	return t + ((s.off[v]-t)%s.week+s.week)%s.week
}

// lowerBound: no plan from day t on can fetch the last document earlier.
func (s *solver) lowerBound(t int) int {
	earliest := make([]int, s.m)
	bySlot := make([][][2]int, s.week)
	for _, v := range s.topo {
		if s.done[v] {
			continue
		}
		base := t
		for _, p := range s.pre[v] {
			if !s.done[p] && earliest[p]+1 > base {
				base = earliest[p] + 1
			}
		}
		earliest[v] = s.firstDay(base, v)
		bySlot[s.off[v]] = append(bySlot[s.off[v]], [2]int{earliest[v], s.tail[v]})
	}
	// k documents of one reception day that cannot come before day r
	// take k such days from r on, and the last still has a tail ahead
	bound := 0
	for _, here := range bySlot {
		sort.Slice(here, func(i, j int) bool {
			if here[i][0] != here[j][0] {
				return here[i][0] > here[j][0]
			}
			return here[i][1] > here[j][1]
		})
		count, shortest := 0, inf
		for _, d := range here {
			count++
			if d[1] < shortest {
				shortest = d[1]
			}
			if b := d[0] + (count-1)*s.week + shortest; b > bound {
				bound = b
			}
		}
	}
	return bound
}

// choices gives the first day with a document to fetch, and those documents.
func (s *solver) choices(t int, wait []int, taken []bool) (int, []int) {
	day := inf
	var cands []int
	for v := 0; v < s.m; v++ {
		if taken[v] || wait[v] != 0 {
			continue
		}
		d := s.firstDay(t, v)
		if d < day {
			day = d
			cands = cands[:0]
		}
		if d == day {
			cands = append(cands, v)
		}
	}
	sort.Slice(cands, func(i, j int) bool {
		a, b := cands[i], cands[j]
		if s.tail[a] != s.tail[b] {
			return s.tail[a] > s.tail[b]
		}
		return a < b
	})
	return day, cands
}

// greedy fetches the document with the longest chain behind it each time.
func (s *solver) greedy(t, count int) (int, []int) {
	wait := append([]int(nil), s.waiting...)
	taken := append([]bool(nil), s.done...)
	last := t - 1
	plan := make([]int, 0, count)
	for i := 0; i < count; i++ {
		var cands []int
		last, cands = s.choices(t, wait, taken)
		v := cands[0]
		taken[v] = true
		plan = append(plan, v)
		for _, u := range s.succ[v] {
			wait[u]--
		}
		t = last + 1
	}
	return last, plan
}

func (s *solver) search(t int, mask [2]uint64, count int) {
	if count == 0 {
		if t-1 < s.bestDay {
			s.bestDay = t - 1
			s.bestPlan = append([]int(nil), s.path...)
		}
		return
	}
	// the same documents in hand by an earlier day were already tried
	if old, ok := s.seen[mask]; ok && old <= t {
		return
	}
	s.seen[mask] = t
	if s.lowerBound(t) >= s.bestDay {
		return
	}
	// fetching nothing on a day when something can be fetched never helps
	day, cands := s.choices(t, s.waiting, s.done)
	for _, v := range cands {
		s.done[v] = true
		for _, u := range s.succ[v] {
			s.waiting[u]--
		}
		s.path = append(s.path, v)
		last, rest := s.greedy(day+1, count-1)
		if last < s.bestDay {
			s.bestDay = last
			s.bestPlan = append(append([]int(nil), s.path...), rest...)
		}
		if day < s.bestDay {
			next := mask
			next[v/word] |= 1 << uint(v%word)
			s.search(day+1, next, count-1)
		}
		s.path = s.path[:len(s.path)-1]
		for _, u := range s.succ[v] {
			s.waiting[u]++
		}
		s.done[v] = false
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	next := func() int {
		var v int
		fmt.Fscan(in, &v)
		return v
	}
	listed := func() []int {
		var items []int
		for v := next(); v != 0; v = next() {
			items = append(items, v)
		}
		return items
	}
	n, week := next(), next()
	dayOf := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dayOf[i] = next()
	}
	needs := make([][]int, n+1)
	for i := 1; i <= n; i++ {
		needs[i] = listed()
	}
	today := next()
	held := make([]bool, n+1)
	for _, d := range listed() {
		held[d] = true
	}
	// every document still to get: the wanted ones and, behind them, the
	// papers they need, stopping at papers already held
	todo := make([]bool, n+1)
	var stack []int
	for _, d := range listed() {
		if !held[d] {
			stack = append(stack, d)
		}
	}
	for len(stack) > 0 {
		doc := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if todo[doc] {
			continue
		}
		todo[doc] = true
		for _, p := range needs[doc] {
			if !held[p] {
				stack = append(stack, p)
			}
		}
	}
	var docs []int
	index := make([]int, n+1)
	for d := 1; d <= n; d++ {
		if todo[d] {
			index[d] = len(docs)
			docs = append(docs, d)
		}
	}
	m := len(docs)
	s := &solver{m: m, week: week, seen: make(map[[2]uint64]int)}
	s.pre = make([][]int, m)
	s.succ = make([][]int, m)
	s.off = make([]int, m)
	for v, d := range docs {
		for _, p := range needs[d] {
			if todo[p] {
				s.pre[v] = append(s.pre[v], index[p])
				s.succ[index[p]] = append(s.succ[index[p]], v)
			}
		}
		// day t (today is day 0) belongs to an official when t = off mod week
		s.off[v] = ((dayOf[d]-today)%week + week) % week
	}
	// a cycle among them makes the set impossible to get
	s.waiting = make([]int, m)
	for v := range s.waiting {
		s.waiting[v] = len(s.pre[v])
	}
	left := append([]int(nil), s.waiting...)
	for v := 0; v < m; v++ {
		if left[v] == 0 {
			s.topo = append(s.topo, v)
		}
	}
	for i := 0; i < len(s.topo); i++ {
		for _, u := range s.succ[s.topo[i]] {
			left[u]--
			if left[u] == 0 {
				s.topo = append(s.topo, u)
			}
		}
	}
	if len(s.topo) < m {
		fmt.Println("No Solution")
		return
	}
	// tail[v]: days that must pass after v is fetched, along its longest chain
	s.tail = make([]int, m)
	for i := m - 1; i >= 0; i-- {
		v := s.topo[i]
		for _, u := range s.succ[v] {
			gap := ((s.off[u]-s.off[v])%week + week) % week
			if gap == 0 {
				gap = week
			}
			if gap+s.tail[u] > s.tail[v] {
				s.tail[v] = gap + s.tail[u]
			}
		}
	}
	s.done = make([]bool, m)
	if m == 0 {
		fmt.Print("0\n\n")
		return
	}
	s.bestDay, s.bestPlan = s.greedy(0, m)
	s.search(0, [2]uint64{}, m)
	words := make([]string, len(s.bestPlan))
	for i, v := range s.bestPlan {
		words[i] = strconv.Itoa(docs[v])
	}
	fmt.Println(s.bestDay)
	fmt.Println(strings.Join(words, " "))
}
