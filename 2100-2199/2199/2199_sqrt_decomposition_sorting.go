package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const valueLimit = 1000000000
const infinity = 2*valueLimit + 1

type answer struct{ score, first, second int }
type query struct{ right, left, id int }
type entry struct{ value, rank int }

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// The Fenwick tree stores the occupied ranks in absolute-value order.
type ordered struct {
	tree        []int
	total, step int
}

func (s *ordered) update(rank, delta int) {
	s.total += delta
	for i := rank + 1; i < len(s.tree); i += i & -i {
		s.tree[i] += delta
	}
}

func (s *ordered) count(rank int) int {
	result := 0
	for i := rank; i > 0; i -= i & -i {
		result += s.tree[i]
	}
	return result
}

func (s *ordered) kth(k int) int {
	index := 0
	for step := s.step; step > 0; step >>= 1 {
		next := index + step
		if next < len(s.tree) && s.tree[next] < k {
			index = next
			k -= s.tree[next]
		}
	}
	return index
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, q int
	fmt.Fscan(in, &n, &q)
	days, order := make([]int, n), make([]int, n)
	for i := range days {
		fmt.Fscan(in, &days[i])
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool {
		a, b := order[i], order[j]
		if abs(days[a]) != abs(days[b]) {
			return abs(days[a]) < abs(days[b])
		}
		return a < b
	})
	ranks, values, potential := make([]int, n), make([]int, n), make([]int, n)
	numeric := make([]entry, n)
	for rank, day := range order {
		ranks[day], values[rank] = rank, days[day]
		numeric[rank] = entry{days[day], rank}
	}
	sort.Slice(numeric, func(i, j int) bool {
		if numeric[i].value != numeric[j].value {
			return numeric[i].value < numeric[j].value
		}
		return numeric[i].rank < numeric[j].rank
	})
	for rank, value := range values {
		pos := sort.Search(n, func(i int) bool { return numeric[i].value >= -value })
		potential[rank] = infinity
		for other := max(0, pos-2); other < min(n, pos+2); other++ {
			if numeric[other].rank != rank {
				potential[rank] = min(potential[rank], abs(value+numeric[other].value))
			}
		}
	}
	blockSize := max(1, 2*n/max(1, int(math.Sqrt(float64(q)))))
	buckets := make([][]query, (n+blockSize-1)/blockSize)
	answers := make([]answer, q)
	last := make(map[int]int)
	globalPairs := make([]answer, n)
	globalPair := answer{0, -1, -1}
	globalScore := infinity
	for _, bound := range potential {
		globalScore = min(globalScore, bound)
	}
	for day, value := range days {
		for _, target := range []int{-value - globalScore, -value + globalScore} {
			if first, ok := last[target]; ok && first > globalPair.first {
				globalPair = answer{globalScore, first, day}
			}
		}
		globalPairs[day] = globalPair
		last[value] = day
	}
	for id := 0; id < q; id++ {
		var left, right int
		fmt.Fscan(in, &left, &right)
		left--
		if globalPairs[right-1].first >= left {
			answers[id] = globalPairs[right-1]
		} else {
			block := left / blockSize
			buckets[block] = append(buckets[block], query{right, left, id})
		}
	}
	step := 1
	for step*2 <= n {
		step *= 2
	}
	for block, queries := range buckets {
		sort.Slice(queries, func(i, j int) bool {
			a, b := queries[i], queries[j]
			if a.right != b.right {
				return a.right < b.right
			}
			if a.left != b.left {
				return a.left < b.left
			}
			return a.id < b.id
		})
		boundary := min(n, (block+1)*blockSize)
		end := boundary
		active := ordered{make([]int, n+1), 0, step}
		coreBest := answer{infinity, 0, 0}
		add := func(rank int, best *answer) bool {
			if potential[rank] >= best.score {
				return false
			}
			before := active.count(rank)
			consider := func(other int) {
				score := abs(values[rank] + values[other])
				if score < best.score {
					*best = answer{score, order[rank], order[other]}
				}
			}
			if before > 0 {
				consider(active.kth(before))
			}
			if before < active.total {
				consider(active.kth(before + 1))
			}
			active.update(rank, 1)
			return true
		}
		start := block * blockSize
		suffixBest := make([]answer, boundary-start+1)
		fringeBest := answer{infinity, 0, 0}
		for day := boundary - 1; day >= start; day-- {
			add(ranks[day], &fringeBest)
			suffixBest[day-start] = fringeBest
		}
		active = ordered{make([]int, n+1), 0, step}
		for _, item := range queries {
			for end < item.right && coreBest.score != 0 {
				add(ranks[end], &coreBest)
				end++
			}
			best := coreBest
			if item.right <= boundary {
				temporary := make([]int, 0, blockSize)
				for day := item.left; day < item.right; day++ {
					if add(ranks[day], &best) {
						temporary = append(temporary, ranks[day])
					}
				}
				for _, rank := range temporary {
					active.update(rank, -1)
				}
			} else {
				if suffixBest[item.left-start].score < best.score {
					best = suffixBest[item.left-start]
				}
				for day := item.left; day < boundary; day++ {
					rank := ranks[day]
					if potential[rank] >= best.score {
						continue
					}
					before := active.count(rank)
					consider := func(other int) {
						score := abs(values[rank] + values[other])
						if score < best.score {
							best = answer{score, order[rank], order[other]}
						}
					}
					if before > 0 {
						consider(active.kth(before))
					}
					if before < active.total {
						consider(active.kth(before + 1))
					}
				}
			}
			answers[item.id] = best
		}
	}
	for _, best := range answers {
		fmt.Fprintln(out, min(best.first, best.second)+1, max(best.first, best.second)+1)
	}
}
