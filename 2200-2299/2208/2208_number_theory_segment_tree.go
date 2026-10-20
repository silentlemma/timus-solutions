package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const maxFactors = 7
const outputBuffer = 65536

type primeSets struct {
	offset, length, count     []int
	coordinate, bit, previous []int
}

func (s *primeSets) locate(prime, position int) int {
	left, right := 1, s.length[prime]+1
	offset := s.offset[prime]
	for left < right {
		middle := (left + right) / 2
		if s.coordinate[offset+middle] < position {
			left = middle + 1
		} else {
			right = middle
		}
	}
	return left
}

func (s *primeSets) add(prime, index, delta int) {
	for index <= s.length[prime] {
		s.bit[s.offset[prime]+index] += delta
		index += index & -index
	}
	s.count[prime] += delta
}

func (s *primeSets) prefix(prime, index int) int {
	result := 0
	for index > 0 {
		result += s.bit[s.offset[prime]+index]
		index -= index & -index
	}
	return result
}

func (s *primeSets) selectNode(prime, rank int) int {
	step := 1
	for step*2 <= s.length[prime] {
		step *= 2
	}
	index, offset := 0, s.offset[prime]
	for step > 0 {
		next := index + step
		if next <= s.length[prime] && s.bit[offset+next] < rank {
			rank -= s.bit[offset+next]
			index = next
		}
		step /= 2
	}
	return offset + index + 1
}

type segmentTree struct {
	base    int
	maximum []int
}

func (t *segmentTree) set(position, value int) {
	node := t.base + position - 1
	t.maximum[node] = value
	for node /= 2; node > 0; node /= 2 {
		value = t.maximum[node*2]
		if t.maximum[node*2+1] > value {
			value = t.maximum[node*2+1]
		}
		t.maximum[node] = value
	}
}

func (t *segmentTree) first(node, left, right, queryLeft, queryRight int) int {
	if right < queryLeft || left > queryRight || t.maximum[node] < queryLeft {
		return 0
	}
	if left == right {
		return left
	}
	middle := (left + right) / 2
	answer := t.first(node*2, left, middle, queryLeft, queryRight)
	if answer == 0 {
		answer = t.first(node*2+1, middle+1, right, queryLeft, queryRight)
	}
	return answer
}

func nextInt(data []byte, cursor *int) int {
	for *cursor < len(data) && data[*cursor] <= ' ' {
		*cursor++
	}
	value := 0
	for *cursor < len(data) && data[*cursor] >= '0' && data[*cursor] <= '9' {
		value = value*10 + int(data[*cursor]-'0')
		*cursor++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	cursor := 0
	n, q := nextInt(data, &cursor), nextInt(data, &cursor)
	values := make([]int, n+1)
	maximum := 2
	for position := 1; position <= n; position++ {
		values[position] = nextInt(data, &cursor)
		if values[position] > maximum {
			maximum = values[position]
		}
	}
	kinds, first, second := make([]int, q), make([]int, q), make([]int, q)
	for index := 0; index < q; index++ {
		kinds[index] = nextInt(data, &cursor)
		first[index], second[index] = nextInt(data, &cursor), nextInt(data, &cursor)
		if kinds[index] == 2 && second[index] > maximum {
			maximum = second[index]
		}
	}
	spf := make([]int, maximum+1)
	for prime := 2; prime <= maximum; prime++ {
		if spf[prime] != 0 {
			continue
		}
		spf[prime] = prime
		if prime <= maximum/prime {
			for multiple := prime * prime; multiple <= maximum; multiple += prime {
				if spf[multiple] == 0 {
					spf[multiple] = prime
				}
			}
		}
	}
	raw := make([][]int, maximum+1)
	used := make([]int, 0)
	collect := func(position, value int) {
		for value > 1 {
			prime := spf[value]
			if raw[prime] == nil {
				used = append(used, prime)
			}
			raw[prime] = append(raw[prime], position)
			for value%prime == 0 {
				value /= prime
			}
		}
	}
	for position := 1; position <= n; position++ {
		collect(position, values[position])
	}
	for index := 0; index < q; index++ {
		if kinds[index] == 2 {
			collect(first[index], second[index])
		}
	}
	sets := primeSets{offset: make([]int, maximum+1), length: make([]int, maximum+1),
		count: make([]int, maximum+1), coordinate: []int{0}}
	for _, prime := range used {
		positions := raw[prime]
		sort.Ints(positions)
		sets.offset[prime] = len(sets.coordinate) - 1
		last := 0
		for _, position := range positions {
			if position != last {
				sets.coordinate = append(sets.coordinate, position)
				sets.length[prime]++
				last = position
			}
		}
		raw[prime] = nil
	}
	raw = nil
	sets.bit = make([]int, len(sets.coordinate))
	sets.previous = make([]int, len(sets.coordinate))
	members := make([]int, (n+1)*maxFactors)
	last := make([]int, maximum+1)
	tree := segmentTree{base: 1}
	for tree.base < n {
		tree.base *= 2
	}
	tree.maximum = make([]int, tree.base*2)
	for position := 1; position <= n; position++ {
		slot, best := position*maxFactors, 0
		for value := values[position]; value > 1; {
			prime := spf[value]
			node := sets.offset[prime] + sets.locate(prime, position)
			members[slot], sets.previous[node], sets.bit[node] = node, last[prime], 1
			if last[prime] > best {
				best = last[prime]
			}
			last[prime] = position
			sets.count[prime]++
			slot++
			for value%prime == 0 {
				value /= prime
			}
		}
		tree.maximum[tree.base+position-1] = best
	}
	for _, prime := range used {
		offset := sets.offset[prime]
		for index := 1; index <= sets.length[prime]; index++ {
			parent := index + (index & -index)
			if parent <= sets.length[prime] {
				sets.bit[offset+parent] += sets.bit[offset+index]
			}
		}
	}
	for node := tree.base - 1; node > 0; node-- {
		tree.maximum[node] = tree.maximum[node*2]
		if tree.maximum[node*2+1] > tree.maximum[node] {
			tree.maximum[node] = tree.maximum[node*2+1]
		}
	}
	refresh := func(position int) {
		best := 0
		for slot := position * maxFactors; slot < (position+1)*maxFactors; slot++ {
			if sets.previous[members[slot]] > best {
				best = sets.previous[members[slot]]
			}
		}
		tree.set(position, best)
	}
	output := bufio.NewWriterSize(os.Stdout, outputBuffer)
	defer output.Flush()
	for query := 0; query < q; query++ {
		left, right := first[query], second[query]
		if kinds[query] == 1 {
			position := tree.first(1, 1, tree.base, left, right)
			if position == 0 {
				fmt.Fprintln(output, -1)
			} else {
				fmt.Fprintln(output, tree.maximum[tree.base+position-1], position)
			}
			continue
		}
		oldValue := values[left]
		if oldValue == right {
			continue
		}
		for value := oldValue; value > 1; {
			prime := spf[value]
			if right%prime != 0 {
				index := sets.locate(prime, left)
				node := sets.offset[prime] + index
				rank := sets.prefix(prime, index)
				if rank < sets.count[prime] {
					next := sets.selectNode(prime, rank+1)
					sets.previous[next] = sets.previous[node]
					refresh(sets.coordinate[next])
				}
				sets.add(prime, index, -1)
			}
			for value%prime == 0 {
				value /= prime
			}
		}
		for value := right; value > 1; {
			prime := spf[value]
			if oldValue%prime != 0 {
				index := sets.locate(prime, left)
				node := sets.offset[prime] + index
				rank := sets.prefix(prime, index-1)
				sets.previous[node] = 0
				if rank > 0 {
					sets.previous[node] = sets.coordinate[sets.selectNode(prime, rank)]
				}
				if rank < sets.count[prime] {
					next := sets.selectNode(prime, rank+1)
					sets.previous[next] = left
					refresh(sets.coordinate[next])
				}
				sets.add(prime, index, 1)
			}
			for value%prime == 0 {
				value /= prime
			}
		}
		values[left] = right
		slot := left * maxFactors
		for index := slot; index < slot+maxFactors; index++ {
			members[index] = 0
		}
		for value := right; value > 1; {
			prime := spf[value]
			members[slot] = sets.offset[prime] + sets.locate(prime, left)
			slot++
			for value%prime == 0 {
				value /= prime
			}
		}
		refresh(left)
	}
}
