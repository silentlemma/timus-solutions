package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const infinity int64 = 10_000_000_000

type DSU []int

func newDSU(n int) DSU {
	p := make(DSU, n)
	for i := range p {
		p[i] = -1
	}
	return p
}

func (p DSU) find(v int) int {
	if p[v] < 0 {
		return v
	}
	p[v] = p.find(p[v])
	return p[v]
}

func (p DSU) join(a, b int) bool {
	a, b = p.find(a), p.find(b)
	if a == b {
		return false
	}
	if p[a] > p[b] {
		a, b = b, a
	}
	p[a] += p[b]
	p[b] = a
	return true
}

func minimum(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

type Sweep struct {
	order, rank []int
	value       []int64
}

type Edge struct {
	distance int64
	u, v     int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var width, height, n, m int
	fmt.Fscan(in, &width, &height, &n, &m)
	count := n + m
	x, y := make([]int64, count), make([]int64, count)
	people, jobs := make([]int64, count), make([]int64, count)
	var totalPeople, totalJobs int64
	for i := range x {
		var amount int64
		fmt.Fscan(in, &x[i], &y[i], &amount)
		if i < n {
			people[i] = amount
			totalPeople += amount
		} else {
			jobs[i] = amount
			totalJobs += amount
		}
	}
	target := minimum(totalPeople, totalJobs)
	ys := append([]int64(nil), y...)
	sort.Slice(ys, func(i, j int) bool { return ys[i] < ys[j] })
	unique := ys[:0]
	for _, value := range ys {
		if len(unique) == 0 || unique[len(unique)-1] != value {
			unique = append(unique, value)
		}
	}
	span := len(unique)
	var sweeps []Sweep
	for _, sx := range []int64{1, -1} {
		for _, sy := range []int64{1, -1} {
			s := Sweep{make([]int, count), make([]int, count), make([]int64, count+1)}
			for i := range x {
				s.order[i] = i
				rank := sort.Search(len(unique), func(j int) bool { return unique[j] >= y[i] })
				s.rank[i] = rank + 1
				if sy == -1 {
					s.rank[i] = span - rank
				}
				s.value[i] = sx*x[i] + sy*y[i]
			}
			s.value[count] = -infinity
			sort.Slice(s.order, func(a, b int) bool {
				i, j := s.order[a], s.order[b]
				if x[i] == x[j] {
					return sy*y[i] < sy*y[j]
				}
				return sx*x[i] < sx*x[j]
			})
			sweeps = append(sweeps, s)
		}
	}

	dsu, components := newDSU(count), count
	var edges []Edge
	for components > 1 {
		roots, from, to := make([]int, count+1), make([]int, count), make([]int, count)
		best := make([]int64, count)
		roots[count] = -1
		for i := range x {
			roots[i], from[i], best[i] = dsu.find(i), -1, infinity
		}
		for _, s := range sweeps {
			var first, second [2][]int
			for color := 0; color < 2; color++ {
				first[color], second[color] = make([]int, span+1), make([]int, span+1)
				for k := 0; k <= span; k++ {
					first[color][k], second[color][k] = count, count
				}
			}
			for _, i := range s.order {
				color := 0
				if i >= n {
					color = 1
				}
				root, candidate := roots[i], count
				for k := s.rank[i]; k > 0; k -= k & -k {
					v := first[1-color][k]
					if roots[v] == root {
						v = second[1-color][k]
					}
					if s.value[v] > s.value[candidate] {
						candidate = v
					}
				}
				if candidate != count && s.value[i]-s.value[candidate] < best[root] {
					best[root], from[root], to[root] = s.value[i]-s.value[candidate], i, candidate
				}
				// Keep maxima from two distinct frozen components.
				for k := s.rank[i]; k <= span; k += k & -k {
					v := first[color][k]
					if s.value[i] > s.value[v] {
						if roots[v] != root {
							second[color][k] = v
						}
						first[color][k] = i
					} else if roots[v] != root && s.value[i] > s.value[second[color][k]] {
						second[color][k] = i
					}
				}
			}
		}
		for r := range x {
			if from[r] != -1 && dsu.join(from[r], to[r]) {
				edges = append(edges, Edge{best[r], from[r], to[r]})
				components--
			}
		}
	}
	sort.Slice(edges, func(i, j int) bool { return edges[i].distance < edges[j].distance })
	dsu = newDSU(count)
	var score int64
	for _, edge := range edges {
		a, b := dsu.find(edge.u), dsu.find(edge.v)
		score -= minimum(people[a], jobs[a]) + minimum(people[b], jobs[b])
		population, capacity := people[a]+people[b], jobs[a]+jobs[b]
		dsu.join(a, b)
		root := dsu.find(a)
		people[root], jobs[root] = population, capacity
		score += minimum(population, capacity)
		if score == target {
			fmt.Println(target, edge.distance)
			return
		}
	}
}
