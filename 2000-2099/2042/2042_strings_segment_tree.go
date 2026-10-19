package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const treeFactor = 4

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

func radii(s []byte, oddCap, evenCap int) ([]int, []int) {
	n := len(s)
	odd, even := make([]int, n), make([]int, n)
	left, right := 0, -1
	for i := range s {
		d := 1
		if i <= right {
			d = min(odd[left+right-i], right-i+1)
		}
		for d < oddCap && i >= d && i+d < n && s[i-d] == s[i+d] {
			d++
		}
		odd[i] = d
		if i+d-1 > right {
			left, right = i-d+1, i+d-1
		}
	}
	left, right = 0, -1
	for i := range s {
		d := 0
		if i <= right {
			d = min(even[left+right-i+1], right-i+1)
		}
		for d < evenCap && i > d && i+d < n && s[i-d-1] == s[i+d] {
			d++
		}
		even[i] = d
		if i+d-1 > right {
			left, right = i-d, i+d-1
		}
	}
	return odd, even
}

type characters struct {
	n   int
	tag []byte
}

func newCharacters(s []byte) *characters {
	t := &characters{len(s), make([]byte, treeFactor*len(s))}
	t.build(1, 0, len(s), s)
	return t
}
func (t *characters) build(v, a, b int, s []byte) {
	if b-a == 1 {
		t.tag[v] = s[a]
		return
	}
	mid := (a + b) / 2
	t.build(2*v, a, mid, s)
	t.build(2*v+1, mid, b, s)
	if t.tag[2*v] == t.tag[2*v+1] {
		t.tag[v] = t.tag[2*v]
	}
}
func (t *characters) assign(v, a, b, left, right int, c byte) {
	if left <= a && b <= right {
		t.tag[v] = c
		return
	}
	mid := (a + b) / 2
	if t.tag[v] != 0 {
		t.tag[2*v], t.tag[2*v+1] = t.tag[v], t.tag[v]
		t.tag[v] = 0
	}
	if left < mid {
		t.assign(2*v, a, mid, left, right, c)
	}
	if mid < right {
		t.assign(2*v+1, mid, b, left, right, c)
	}
	if t.tag[2*v] == t.tag[2*v+1] {
		t.tag[v] = t.tag[2*v]
	}
}
func (t *characters) collect(v, a, b, left, right int, out *[]byte) {
	if t.tag[v] != 0 {
		for count := min(b, right) - max(a, left); count > 0; count-- {
			*out = append(*out, t.tag[v])
		}
		return
	}
	mid := (a + b) / 2
	if left < mid {
		t.collect(2*v, a, mid, left, right, out)
	}
	if mid < right {
		t.collect(2*v+1, mid, b, left, right, out)
	}
}
func (t *characters) extract(left, right int) []byte {
	out := make([]byte, 0, right-left)
	t.collect(1, 0, t.n, left, right, &out)
	return out
}

type counts struct {
	n     int
	total []int
	tag   []byte
}

func newCounts(values []int) *counts {
	t := &counts{
		len(values),
		make([]int, treeFactor*len(values)),
		make([]byte, treeFactor*len(values)),
	}
	t.build(1, 0, len(values), values)
	return t
}
func (t *counts) pull(v int) {
	t.total[v] = t.total[2*v] + t.total[2*v+1]
	t.tag[v] = 0
	if t.tag[2*v] == t.tag[2*v+1] {
		t.tag[v] = t.tag[2*v]
	}
}
func (t *counts) build(v, a, b int, values []int) {
	if b-a == 1 {
		t.total[v] = values[a]
		t.tag[v] = byte(values[a] + 1)
		return
	}
	mid := (a + b) / 2
	t.build(2*v, a, mid, values)
	t.build(2*v+1, mid, b, values)
	t.pull(v)
}
func (t *counts) replace(v, a, b, left, right, value int, values []int) {
	if value >= 0 && left <= a && b <= right || b-a == 1 {
		chosen := value
		if value < 0 {
			chosen = values[a-left]
		}
		t.total[v] = (b - a) * chosen
		t.tag[v] = byte(chosen + 1)
		return
	}
	mid := (a + b) / 2
	if t.tag[v] != 0 {
		old := int(t.tag[v]) - 1
		t.total[2*v], t.total[2*v+1] = (mid-a)*old, (b-mid)*old
		t.tag[2*v], t.tag[2*v+1] = t.tag[v], t.tag[v]
		t.tag[v] = 0
	}
	if left < mid {
		t.replace(2*v, a, mid, left, right, value, values)
	}
	if mid < right {
		t.replace(2*v+1, mid, b, left, right, value, values)
	}
	t.pull(v)
}
func (t *counts) query(v, a, b, left, right int) int {
	if left <= a && b <= right {
		return t.total[v]
	}
	if t.tag[v] != 0 {
		return (int(t.tag[v]) - 1) * (min(b, right) - max(a, left))
	}
	mid, answer := (a+b)/2, 0
	if left < mid {
		answer += t.query(2*v, a, mid, left, right)
	}
	if mid < right {
		answer += t.query(2*v+1, mid, b, left, right)
	}
	return answer
}

type solver struct {
	n, k, oddCap, evenCap int
	chars                 *characters
	sums                  *counts
}

func newSolver(text []byte, k int) *solver {
	odd, even := radii(text, (k+1)/2, k/2)
	for i := range odd {
		odd[i] += even[i]
	}
	return &solver{len(text), k, (k + 1) / 2, k / 2, newCharacters(text), newCounts(odd)}
}
func (s *solver) repair(left, right int) {
	if left > right {
		return
	}
	start, end := max(0, left-s.evenCap), min(s.n, right+s.oddCap)
	odd, even := radii(s.chars.extract(start, end), s.oddCap, s.evenCap)
	values := make([]int, right-left+1)
	for i := range values {
		values[i] = odd[left+i-start] + even[left+i-start]
	}
	s.sums.replace(1, 0, s.n, left, right+1, -1, values)
}
func (s *solver) assign(left, right int, c byte) {
	s.chars.assign(1, 0, s.n, left, right+1, c)
	a, b := max(0, left-s.oddCap+1), min(s.n-1, right+s.evenCap)
	x, y := left+s.evenCap, right-s.oddCap+1
	if x <= y {
		s.sums.replace(1, 0, s.n, x, y+1, s.k, nil)
		s.repair(a, x-1)
		s.repair(y+1, b)
	} else {
		s.repair(a, b)
	}
}
func (s *solver) partial(left, right, first, last int) int {
	odd, even := radii(s.chars.extract(left, right), s.oddCap, s.evenCap)
	answer := 0
	for i := first; i < last; i++ {
		answer += odd[i] + even[i]
	}
	return answer
}
func (s *solver) query(left, right int) int {
	length := right - left + 1
	if length < s.k {
		return s.partial(left, right+1, 0, length)
	}
	answer := s.sums.query(1, 0, s.n, left+s.evenCap, right-s.oddCap+2)
	if s.evenCap > 0 {
		answer += s.partial(left, left+s.k-1, 0, s.evenCap)
	}
	if s.oddCap > 1 {
		answer += s.partial(right-s.k+2, right+1, s.evenCap, s.k-1)
	}
	return answer
}

type input struct {
	data []byte
	at   int
}

func (in *input) word() []byte {
	for in.at < len(in.data) && in.data[in.at] <= ' ' {
		in.at++
	}
	start := in.at
	for in.at < len(in.data) && in.data[in.at] > ' ' {
		in.at++
	}
	return in.data[start:in.at]
}
func (in *input) integer() int {
	value := 0
	for _, c := range in.word() {
		value = 10*value + int(c-'0')
	}
	return value
}
func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	text := in.word()
	k := in.integer()
	model := newSolver(text, k)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for q := in.integer(); q > 0; q-- {
		typeID, left, right := in.integer(), in.integer()-1, in.integer()-1
		if typeID == 1 {
			model.assign(left, right, in.word()[0])
		} else {
			fmt.Fprintln(out, model.query(left, right))
		}
	}
}
