package main

import (
	"bufio"
	"os"
	"strconv"
)

var keys = []string{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

const (
	slowest = 4
	longest = 100000 // total length of all names
)

type move struct{ to, cost int }

func main() {
	var presses ['z' + 1]int
	for _, key := range keys {
		for k := 0; k < len(key); k++ {
			presses[key[k]] = k + 1
		}
	}
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Buffer(make([]byte, longest+1), longest+1)
	scanner.Split(bufio.ScanWords)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	words := make([]string, n)
	for i := range words {
		scanner.Scan()
		words[i] = scanner.Text()
	}
	// state offset[x] + d: name x is current and its first d letters are
	// typed; nodeOf[state] is the trie node of the typed letters
	offset := make([]int, n+1)
	for x, w := range words {
		offset[x+1] = offset[x] + len(w) + 1
	}
	states := offset[n]
	nodeOf, owner := make([]int, states), make([]int, states)
	low, high := []int{0}, []int{n - 1} // the names below a node form a range
	children := [][]move{nil}
	path := []int{0}
	for x, w := range words {
		same := 0
		if x > 0 {
			p := words[x-1]
			for same < len(w) && same < len(p) && w[same] == p[same] {
				same++
			}
		}
		path = path[:same+1]
		for d := same + 1; d <= len(w); d++ {
			v := len(low)
			low = append(low, x)
			high = append(high, x)
			children = append(children, nil)
			top := path[len(path)-1]
			children[top] = append(children[top], move{offset[x] + d, presses[w[d-1]]})
			path = append(path, v)
		}
		for d := 0; d <= len(w); d++ {
			nodeOf[offset[x]+d] = path[d]
			owner[offset[x]+d] = x
			high[path[d]] = x
		}
	}
	hubs := len(low)
	const inf = 1 << 30
	dist := make([]int, states+hubs)
	for i := range dist {
		dist[i] = inf
	}
	// every move costs at most slowest, so slowest + 1 buckets in a circle
	buckets := make([][]int, slowest+1)
	dist[0] = 0
	buckets[0] = append(buckets[0], 0)
	pending := 1
	moves, buf := []move{}, make([]move, 0, slowest)
	for now := 0; pending > 0; now++ {
		b := now % (slowest + 1)
		for len(buckets[b]) > 0 {
			s := buckets[b][len(buckets[b])-1]
			buckets[b] = buckets[b][:len(buckets[b])-1]
			pending--
			if dist[s] != now {
				continue
			}
			if s >= states {
				moves = children[s-states]
			} else {
				x := owner[s]
				d := s - offset[x]
				v := nodeOf[s]
				nxt, prv := low[v], high[v]
				if x < high[v] {
					nxt = x + 1
				}
				if x > low[v] {
					prv = x - 1
				}
				moves = append(buf[:0], move{offset[nxt] + d, 1}, move{offset[prv] + d, 1})
				moves = append(moves, move{states + v, 0})
				if d > 0 {
					moves = append(moves, move{s - 1, 1})
				}
			}
			for _, m := range moves {
				if now+m.cost < dist[m.to] {
					dist[m.to] = now + m.cost
					c := (now + m.cost) % (slowest + 1)
					buckets[c] = append(buckets[c], m.to)
					pending++
				}
			}
		}
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for x := 0; x < n; x++ {
		best := inf
		for s := offset[x]; s < offset[x+1]; s++ {
			if dist[s] < best {
				best = dist[s]
			}
		}
		if x > 0 {
			writer.WriteByte(' ')
		}
		writer.WriteString(strconv.Itoa(best))
	}
	writer.WriteByte('\n')
}
