package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
)

const half = 0.5
const boundariesPerEvent = 3
const outputPrecision = 17
const outputCapacity = 128
const floatBits = 64

type scanner struct {
	data []byte
	at   int
}

func (s *scanner) word() []byte {
	for s.at < len(s.data) && s.data[s.at] <= ' ' {
		s.at++
	}
	start := s.at
	for s.at < len(s.data) && s.data[s.at] > ' ' {
		s.at++
	}
	return s.data[start:s.at]
}
func (s *scanner) number() int {
	value := 0
	for _, c := range s.word() {
		value = value*10 + int(c-'0')
	}
	return value
}

type event struct {
	time, first, second int
	enforce             bool
}
type energyTree struct {
	xs               []int
	total, low, high []float64
	cleared          []bool
}

func newTree(xs []int) *energyTree {
	nodes := 2*(len(xs)-1) - 1
	return &energyTree{xs, make([]float64, nodes), make([]float64, nodes),
		make([]float64, nodes), make([]bool, nodes)}
}
func (t *energyTree) apply(node, length int, first, last float64) {
	t.total[node] += (first + last) * half * float64(length)
	t.low[node] += first
	t.high[node] += last
}
func (t *energyTree) push(node, left, middle, right int) {
	child, other := node+1, node+2*(middle-left)
	if t.cleared[node] {
		t.total[child], t.low[child], t.high[child] = 0, 0, 0
		t.total[other], t.low[other], t.high[other] = 0, 0, 0
		t.cleared[child], t.cleared[other], t.cleared[node] = true, true, false
	}
	first, last := t.low[node], t.high[node]
	if first == 0 && last == 0 {
		return
	}
	length := t.xs[right] - t.xs[left]
	a := t.xs[middle] - t.xs[left]
	b := length - a
	if first == last {
		t.apply(child, a, first, first)
		t.apply(other, b, first, first)
	} else {
		denominator := float64(length - 1)
		leftLast := (first*float64(b) + last*float64(a-1)) / denominator
		rightFirst := (first*float64(b-1) + last*float64(a)) / denominator
		t.apply(child, a, first, leftLast)
		t.apply(other, b, rightFirst, last)
	}
	t.low[node], t.high[node] = 0, 0
}
func (t *energyTree) add(node, left, right, begin, end, origin, direction int, scale float64) {
	if begin <= left && right <= end {
		first := scale * float64(origin+direction*t.xs[left])
		last := scale * float64(origin+direction*(t.xs[right]-1))
		t.apply(node, t.xs[right]-t.xs[left], first, last)
		return
	}
	middle := (left + right) / 2
	t.push(node, left, middle, right)
	if begin < middle {
		t.add(node+1, left, middle, begin, end, origin, direction, scale)
	}
	other := node + 2*(middle-left)
	if end > middle {
		t.add(other, middle, right, begin, end, origin, direction, scale)
	}
	t.total[node] = t.total[node+1] + t.total[other]
}
func (t *energyTree) take(node, left, right, begin, end int) float64 {
	if begin <= left && right <= end {
		answer := t.total[node]
		t.total[node], t.low[node], t.high[node] = 0, 0, 0
		t.cleared[node] = true
		return answer
	}
	middle := (left + right) / 2
	t.push(node, left, middle, right)
	answer := 0.0
	if begin < middle {
		answer += t.take(node+1, left, middle, begin, end)
	}
	other := node + 2*(middle-left)
	if end > middle {
		answer += t.take(other, middle, right, begin, end)
	}
	t.total[node] = t.total[node+1] + t.total[other]
	return answer
}
func solve(s *scanner, out *bufio.Writer) {
	length, rate, count := s.number(), s.number(), s.number()
	events := make([]event, count)
	xs := make([]int, 2, boundariesPerEvent*count+2)
	xs[0], xs[1] = 1, length+1
	for i := range events {
		time := s.number()
		enforce := s.word()[0] == 'e'
		a, b := s.number(), s.number()
		events[i] = event{time, a, b, enforce}
		if enforce {
			xs = append(xs, a-b+1, a+1, a+b)
		} else {
			xs = append(xs, a, b+1)
		}
	}
	sort.Ints(xs)
	unique := 0
	for _, x := range xs {
		if unique == 0 || xs[unique-1] != x {
			xs[unique] = x
			unique++
		}
	}
	xs = xs[:unique]
	tree := newTree(xs)
	leaves, previous := len(xs)-1, 0
	reserve := 0.0
	buffer := make([]byte, 0, outputCapacity)
	for _, e := range events {
		growth := float64(rate) * float64(e.time-previous)
		if growth != 0 {
			tree.apply(0, length, growth, growth)
		}
		previous = e.time
		if e.enforce {
			if reserve == 0 {
				continue
			}
			begin, middle, end := e.first-e.second+1, e.first+1, e.first+e.second
			a, b, c := sort.SearchInts(xs, begin), sort.SearchInts(xs, middle), sort.SearchInts(xs, end)
			scale := reserve / (float64(e.second) * float64(e.second))
			tree.add(0, 0, leaves, a, b, 1-begin, 1, scale)
			if b < c {
				tree.add(0, 0, leaves, b, c, end, -1, scale)
			}
			reserve = 0
		} else {
			a, b := sort.SearchInts(xs, e.first), sort.SearchInts(xs, e.second+1)
			reserve += tree.take(0, 0, leaves, a, b)
			buffer = strconv.AppendFloat(buffer[:0], reserve, 'g', outputPrecision, floatBits)
			out.Write(buffer)
			out.WriteByte('\n')
		}
	}
}
func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	s := scanner{data: data}
	out := bufio.NewWriter(os.Stdout)
	solve(&s, out)
	out.Flush()
}
