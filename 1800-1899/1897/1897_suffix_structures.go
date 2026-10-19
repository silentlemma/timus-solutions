package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	byteValues        = 256
	letters           = 26
	prefixKeyBits     = 60
	nodesPerCharacter = 4
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type node struct {
	depth, first, next, parent, terminal, representative int
	parity, winning                                      bool
}

type gameIndex struct {
	text, combined                                 string
	n, size, alphabetSize, prefixBits, prefixPairs int
	order, rank, compact, logs                     []int
	table                                          [][]int
	nodes                                          []node
	roots, counts                                  []int
	emptyWinning                                   bool
	total                                          int64
}

func (index *gameIndex) buildSuffixArray() {
	size := index.size
	order, rank := make([]int, size), make([]int, size)
	countSize := size
	if countSize < byteValues {
		countSize = byteValues
	}
	count, shifted, following := make([]int, countSize), make([]int, size), make([]int, size)
	for i := range rank {
		rank[i] = int(index.combined[i])
		count[rank[i]]++
	}
	for i := 1; i < byteValues; i++ {
		count[i] += count[i-1]
	}
	for i := size - 1; i >= 0; i-- {
		count[rank[i]]--
		order[count[rank[i]]] = i
	}
	classes := byteValues
	for distance := 1; ; distance *= 2 {
		used := 0
		start := size - distance
		if start < 0 {
			start = 0
		}
		for i := start; i < size; i++ {
			shifted[used] = i
			used++
		}
		for _, i := range order {
			if i >= distance {
				shifted[used] = i - distance
				used++
			}
		}
		for i := 0; i < classes; i++ {
			count[i] = 0
		}
		for _, i := range shifted {
			count[rank[i]]++
		}
		for i := 1; i < classes; i++ {
			count[i] += count[i-1]
		}
		for i := size - 1; i >= 0; i-- {
			count[rank[shifted[i]]]--
			order[count[rank[shifted[i]]]] = shifted[i]
		}
		classes = 1
		following[order[0]] = 0
		for i := 1; i < size; i++ {
			a, b := order[i-1], order[i]
			secondA, secondB := -1, -1
			if a+distance < size {
				secondA = rank[a+distance]
			}
			if b+distance < size {
				secondB = rank[b+distance]
			}
			if rank[a] != rank[b] || secondA != secondB {
				classes++
			}
			following[b] = classes - 1
		}
		rank, following = following, rank
		if classes == size {
			break
		}
	}
	index.order, index.rank = order, rank
	lcp := make([]int, size)
	height := 0
	for position := 0; position < size; position++ {
		place := rank[position]
		if place == 0 {
			height = 0
			continue
		}
		other := order[place-1]
		for position+height < size && other+height < size &&
			index.combined[position+height] == index.combined[other+height] {
			height++
		}
		lcp[place] = height
		if height > 0 {
			height--
		}
	}
	index.table = [][]int{lcp}
	for span := 1; 2*span <= size; span *= 2 {
		previous := index.table[len(index.table)-1]
		row := make([]int, size-2*span+1)
		for i := range row {
			row[i] = min(previous[i], previous[i+span])
		}
		index.table = append(index.table, row)
	}
	index.logs = make([]int, size+1)
	for i := 2; i <= size; i++ {
		index.logs[i] = index.logs[i/2] + 1
	}
}

func (index *gameIndex) lce(a, b int) int {
	if a == b {
		return index.size - a
	}
	left, right := index.rank[a], index.rank[b]
	if left > right {
		left, right = right, left
	}
	level := index.logs[right-left]
	return min(index.table[level][left+1], index.table[level][right-(1<<uint(level))+1])
}

func (index *gameIndex) radius(center, parity int) int {
	return min(center, index.n-center-parity)
}

func (index *gameIndex) common(a, b, parity int) int {
	cap := min(index.radius(a, parity), index.radius(b, parity))
	if cap == 0 {
		return 0
	}
	left := index.lce(2*index.n+1-a, 2*index.n+1-b)
	right := index.lce(a+parity, b+parity)
	return min(cap, min(left, right))
}

func (index *gameIndex) less(a, b, parity int) bool {
	shared := index.common(a, b, parity)
	cap := min(index.radius(a, parity), index.radius(b, parity))
	if shared == cap {
		return index.radius(a, parity) < index.radius(b, parity)
	}
	leftA, leftB := index.text[a-shared-1], index.text[b-shared-1]
	if leftA != leftB {
		return leftA < leftB
	}
	return index.text[a+shared+parity] < index.text[b+shared+parity]
}

func (index *gameIndex) newNode(depth, parity, center int) int {
	id := len(index.nodes)
	index.nodes = append(index.nodes, node{depth, -1, -1, -1, center, -1, parity != 0, false})
	return id
}

func (index *gameIndex) attach(parent, child int) {
	index.nodes[child].parent = parent
	index.nodes[child].next = index.nodes[parent].first
	index.nodes[parent].first = child
}

func (index *gameIndex) buildCenters(centers []int, parity int) int {
	root := index.newNode(0, parity, -1)
	keys := make([]uint64, index.n)
	for _, center := range centers {
		var key uint64
		cap := index.radius(center, parity)
		for offset := 0; offset < index.prefixPairs; offset++ {
			key <<= uint(index.prefixBits)
			if offset < cap {
				key += uint64(index.compact[index.text[center-offset-1]] * index.alphabetSize)
				key += uint64(index.compact[index.text[center+offset+parity]] + 1)
			}
		}
		keys[center] = key
	}
	sort.Slice(centers, func(i, j int) bool { return keys[centers[i]] < keys[centers[j]] })
	for begin := 0; begin < len(centers); {
		end := begin + 1
		for end < len(centers) && keys[centers[end]] == keys[centers[begin]] {
			end++
		}
		group := centers[begin:end]
		sort.Slice(group, func(i, j int) bool { return index.less(group[i], group[j], parity) })
		begin = end
	}
	stack, previousCenter := []int{root}, -1
	for _, center := range centers {
		shared := 0
		if previousCenter >= 0 {
			shared = index.common(previousCenter, center, parity)
		}
		last := -1
		for index.nodes[stack[len(stack)-1]].depth > shared {
			popped := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if last != -1 {
				index.attach(popped, last)
			}
			last = popped
		}
		if index.nodes[stack[len(stack)-1]].depth < shared {
			node := index.newNode(shared, parity, -1)
			index.attach(node, last)
			stack = append(stack, node)
		} else if last != -1 {
			index.attach(stack[len(stack)-1], last)
		}
		cap := index.radius(center, parity)
		if cap > index.nodes[stack[len(stack)-1]].depth {
			stack = append(stack, index.newNode(cap, parity, center))
		} else {
			node := &index.nodes[stack[len(stack)-1]]
			old := node.terminal
			if old < 0 || index.rank[center-cap] < index.rank[old-cap] {
				node.terminal = center
			}
		}
		previousCenter = center
	}
	for len(stack) > 1 {
		child := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		index.attach(stack[len(stack)-1], child)
	}
	return root
}

func newGameIndex(text string) *gameIndex {
	n := len(text)
	reversed := []byte(text)
	for left, right := 0, n-1; left < right; left, right = left+1, right-1 {
		reversed[left], reversed[right] = reversed[right], reversed[left]
	}
	index := &gameIndex{text: text, n: n, combined: text + "#" + string(reversed)}
	index.size = len(index.combined)
	index.compact = make([]int, byteValues)
	present := make([]bool, byteValues)
	for i := range text {
		present[text[i]] = true
	}
	for letter := byte('a'); letter <= 'z'; letter++ {
		if present[letter] {
			index.compact[letter] = index.alphabetSize
			index.alphabetSize++
		}
	}
	for value := index.alphabetSize * index.alphabetSize; value > 0; value >>= 1 {
		index.prefixBits++
	}
	index.prefixPairs = 1
	if index.alphabetSize > 1 {
		index.prefixPairs = prefixKeyBits / index.prefixBits
	}
	index.buildSuffixArray()
	index.nodes = make([]node, 0, nodesPerCharacter*n+letters+1)
	even := make([]int, n-1)
	for i := range even {
		even[i] = i + 1
	}
	index.roots = []int{index.buildCenters(even, 0)}
	groups := make([][]int, letters)
	for c := range text {
		groups[text[c]-'a'] = append(groups[text[c]-'a'], c)
	}
	for _, centers := range groups {
		if len(centers) > 0 {
			index.roots = append(index.roots, index.buildCenters(centers, 1))
		}
	}
	traversal, stack := []int{}, append([]int(nil), index.roots...)
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		traversal = append(traversal, node)
		for child := index.nodes[node].first; child != -1; child = index.nodes[child].next {
			stack = append(stack, child)
		}
	}
	for at := len(traversal) - 1; at >= 0; at-- {
		node := &index.nodes[traversal[at]]
		best := node.terminal
		for child := node.first; child != -1; child = index.nodes[child].next {
			next := &index.nodes[child]
			immediate := next.winning != ((next.depth-node.depth-1)&1 != 0)
			if !immediate {
				node.winning = true
			}
			center := next.representative
			if best < 0 || index.rank[center-node.depth] < index.rank[best-node.depth] {
				best = center
			}
		}
		node.representative = best
	}
	index.counts = make([]int, n+2)
	for _, node := range index.nodes {
		if node.parent == -1 {
			if node.parity && node.winning {
				index.counts[node.representative]++
				index.counts[node.representative+2]--
			}
			continue
		}
		low, high := index.nodes[node.parent].depth+1, node.depth
		winning := 0
		if node.winning {
			winning = 1
		}
		wanted := (node.representative - ((high + 1 - winning) & 1)) & 1
		left, right := node.representative-high, node.representative-low
		if left&1 != wanted {
			left++
		}
		if right&1 != wanted {
			right--
		}
		if left <= right {
			index.counts[left]++
			index.counts[right+2]--
		}
	}
	for i := 2; i < n; i++ {
		index.counts[i] += index.counts[i-2]
	}
	index.emptyWinning = index.nodes[index.roots[0]].winning
	if index.emptyWinning {
		index.total = 1
	}
	for i := 0; i < n; i++ {
		index.total += int64(index.counts[i])
	}
	return index
}

func (index *gameIndex) kth(k int64) string {
	if k > index.total {
		return "no solution"
	}
	if index.emptyWinning {
		if k == 1 {
			return "-"
		}
		k--
	}
	start := -1
	for _, position := range index.order {
		if position >= index.n {
			continue
		}
		if k > int64(index.counts[position]) {
			k -= int64(index.counts[position])
		} else {
			start = position
			break
		}
	}
	lengths := []int{}
	for _, node := range index.nodes {
		if node.parent == -1 {
			if node.parity && node.winning && node.representative == start {
				lengths = append(lengths, 1)
			}
		} else {
			radius := node.representative - start
			if index.nodes[node.parent].depth < radius && radius <= node.depth &&
				(node.winning != ((node.depth-radius)&1 != 0)) {
				parity := 0
				if node.parity {
					parity = 1
				}
				lengths = append(lengths, 2*radius+parity)
			}
		}
	}
	sort.Ints(lengths)
	return index.text[start : start+lengths[k-1]]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var text string
	var k int64
	fmt.Fscan(in, &text, &k)
	fmt.Println(newGameIndex(text).kth(k))
}
