package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const unseen = -1

type input struct {
	data []byte
	pos  int
}

func (in *input) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	sign := 1
	if in.data[in.pos] == '-' {
		sign = unseen
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value * sign
}

type endpoint struct {
	position int
	chord    int
}

type segmentTree struct {
	size    int
	missing int
	minimum []int
	maximum []int
}

func newSegmentTree(mate []int) *segmentTree {
	size := 1
	for size < len(mate) {
		size *= 2
	}
	tree := &segmentTree{
		size: size, missing: len(mate),
		minimum: make([]int, 2*size), maximum: make([]int, 2*size),
	}
	for i := range tree.minimum {
		tree.minimum[i] = tree.missing
		tree.maximum[i] = unseen
	}
	for i, other := range mate {
		tree.minimum[size+i] = other
		tree.maximum[size+i] = other
	}
	for node := size - 1; node > 0; node-- {
		tree.pull(node)
	}
	return tree
}

func (tree *segmentTree) pull(node int) {
	left, right := 2*node, 2*node+1
	tree.minimum[node] = tree.minimum[left]
	if tree.minimum[right] < tree.minimum[node] {
		tree.minimum[node] = tree.minimum[right]
	}
	tree.maximum[node] = tree.maximum[left]
	if tree.maximum[right] > tree.maximum[node] {
		tree.maximum[node] = tree.maximum[right]
	}
}

func (tree *segmentTree) remove(position int) {
	node := tree.size + position
	tree.minimum[node] = tree.missing
	tree.maximum[node] = unseen
	for node /= 2; node > 0; node /= 2 {
		tree.pull(node)
	}
}

func (tree *segmentTree) witness(node, left, right int) int {
	if tree.minimum[node] < left {
		return tree.minimum[node]
	}
	if tree.maximum[node] > right {
		return tree.maximum[node]
	}
	return unseen
}

func (tree *segmentTree) crossing(left, right int) int {
	start, finish := tree.size+left+1, tree.size+right
	for start < finish {
		if start%2 == 1 {
			if found := tree.witness(start, left, right); found >= 0 {
				return found
			}
			start++
		}
		if finish%2 == 1 {
			finish--
			if found := tree.witness(finish, left, right); found >= 0 {
				return found
			}
		}
		start /= 2
		finish /= 2
	}
	return unseen
}

func location(x, y, width, height int) int {
	if x < 0 || x > width || y < 0 || y > height {
		return unseen
	}
	if x == 0 || x == width || y == 0 || y == height {
		return 0
	}
	return 1
}

func perimeter(x, y, width, height int) int {
	if y == 0 {
		return x
	}
	if x == width {
		return width + y
	}
	if y == height {
		return width + height + width - x
	}
	return 2*width + height + height - y
}

func solve(in *input) bool {
	count, width, height := in.nextInt(), in.nextInt(), in.nextInt()
	points := make([]endpoint, 0, 2*count)
	chords := 0
	for pair := 0; pair < count; pair++ {
		x1, y1, x2, y2 := in.nextInt(), in.nextInt(), in.nextInt(), in.nextInt()
		first, second := location(x1, y1, width, height), location(x2, y2, width, height)
		if first*second == unseen {
			return false
		}
		if first == 0 && second == 0 {
			points = append(points, endpoint{perimeter(x1, y1, width, height), chords})
			points = append(points, endpoint{perimeter(x2, y2, width, height), chords})
			chords++
		}
	}
	sort.Slice(points, func(i, j int) bool { return points[i].position < points[j].position })
	owner, mate := make([]int, len(points)), make([]int, len(points))
	left, right, color := make([]int, chords), make([]int, chords), make([]int, chords)
	for chord := range left {
		left[chord], color[chord] = unseen, unseen
	}
	for rank, point := range points {
		owner[rank] = point.chord
		if left[point.chord] == unseen {
			left[point.chord] = rank
		} else {
			right[point.chord] = rank
			mate[rank] = left[point.chord]
			mate[left[point.chord]] = rank
		}
	}
	tree := newSegmentTree(mate)
	queue := make([]int, 0, chords)
	for root := 0; root < chords; root++ {
		if color[root] != unseen {
			continue
		}
		color[root] = 0
		tree.remove(left[root])
		tree.remove(right[root])
		queue = append(queue[:0], root)
		for head := 0; head < len(queue); head++ {
			chord := queue[head]
			for {
				other := tree.crossing(left[chord], right[chord])
				if other == unseen {
					break
				}
				next := owner[other]
				color[next] = color[chord] ^ 1
				tree.remove(left[next])
				tree.remove(right[next])
				queue = append(queue, next)
			}
		}
	}
	// Chords of one color must form properly nested pairs of endpoints.
	stacks := [2][]int{}
	for rank, chord := range owner {
		side := color[chord]
		if rank == left[chord] {
			stacks[side] = append(stacks[side], chord)
		} else {
			last := len(stacks[side]) - 1
			if last < 0 || stacks[side][last] != chord {
				return false
			}
			stacks[side] = stacks[side][:last]
		}
	}
	return true
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if solve(&in) {
		fmt.Fprintln(out, "YES")
	} else {
		fmt.Fprintln(out, "NO")
	}
}
