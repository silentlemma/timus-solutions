package main

import (
	"container/heap"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
)

type roleState struct {
	positions []int
	tree      []int
	score     int64
	count     int
	step      int
}

func (role *roleState) prepare() {
	sort.Ints(role.positions)
	length := 0
	for _, position := range role.positions {
		if length == 0 || role.positions[length-1] != position {
			role.positions[length] = position
			length++
		}
	}
	role.positions = role.positions[:length]
	role.tree = make([]int, length+1)
	role.step = 1
	for role.step*2 <= length {
		role.step *= 2
	}
}

func (role *roleState) prefix(index int) int {
	result := 0
	for index > 0 {
		result += role.tree[index]
		index -= index & -index
	}
	return result
}

func (role *roleState) kth(order int) int {
	index := 0
	for jump := role.step; jump > 0; jump /= 2 {
		next := index + jump
		if next < len(role.tree) && role.tree[next] < order {
			index = next
			order -= role.tree[next]
		}
	}
	return index + 1
}

func (role *roleState) change(position, delta, size int) {
	rank := sort.SearchInts(role.positions, position) + 1
	before := role.prefix(rank - 1)
	left := 0
	if before > 0 {
		left = role.positions[role.kth(before)-1]
	}
	nextOrder := before + 1
	if delta < 0 {
		nextOrder++
	}
	right := size + 1
	if nextOrder <= role.count {
		right = role.positions[role.kth(nextOrder)-1]
	}
	// Splitting a gap removes exactly the intervals crossing this position.
	difference := int64(position-left) * int64(right-position)
	role.score -= int64(delta) * difference
	role.count += delta
	for index := rank; index < len(role.tree); index += index & -index {
		role.tree[index] += delta
	}
}

type query struct {
	position int
	role     int
}

type entry struct {
	score int64
	role  int
}

type scoreHeap []entry

func (values scoreHeap) Len() int { return len(values) }

func (values scoreHeap) Less(left, right int) bool {
	return values[left].score < values[right].score
}

func (values scoreHeap) Swap(left, right int) {
	values[left], values[right] = values[right], values[left]
}

func (values *scoreHeap) Push(value interface{}) { *values = append(*values, value.(entry)) }

func (values *scoreHeap) Pop() interface{} {
	last := len(*values) - 1
	value := (*values)[last]
	*values = (*values)[:last]
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	offset := 0
	nextInt := func() int {
		for data[offset] <= ' ' {
			offset++
		}
		value := 0
		for offset < len(data) && data[offset] >= '0' && data[offset] <= '9' {
			value = value*10 + int(data[offset]-'0')
			offset++
		}
		return value
	}
	size, queryCount := nextInt(), nextInt()
	total := int64(size) * int64(size+1) / 2
	roles := make([]roleState, 0, size+queryCount)
	ids := make(map[int]int, size+queryCount)
	getRole := func(value int) int {
		if id, exists := ids[value]; exists {
			return id
		}
		id := len(roles)
		ids[value] = id
		roles = append(roles, roleState{score: total})
		return id
	}
	current := make([]int, size+1)
	for position := 1; position <= size; position++ {
		id := getRole(nextInt())
		current[position] = id
		roles[id].positions = append(roles[id].positions, position)
	}
	queries := make([]query, queryCount)
	for index := range queries {
		position, value := nextInt(), nextInt()
		id := getRole(value)
		queries[index] = query{position, id}
		roles[id].positions = append(roles[id].positions, position)
	}
	for index := range roles {
		roles[index].prepare()
	}
	for position := 1; position <= size; position++ {
		roles[current[position]].change(position, 1, size)
	}
	minimum := make(scoreHeap, len(roles))
	for id := range roles {
		minimum[id] = entry{roles[id].score, id}
	}
	heap.Init(&minimum)
	output := make([]byte, 0)
	for _, update := range queries {
		old := current[update.position]
		if old != update.role {
			roles[old].change(update.position, -1, size)
			roles[update.role].change(update.position, 1, size)
			current[update.position] = update.role
			heap.Push(&minimum, entry{roles[old].score, old})
			heap.Push(&minimum, entry{roles[update.role].score, update.role})
		}
		for minimum[0].score != roles[minimum[0].role].score {
			heap.Pop(&minimum)
		}
		output = strconv.AppendInt(output, minimum[0].score, 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
