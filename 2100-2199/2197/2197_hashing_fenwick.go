package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math/bits"
	"os"
)

const (
	mod        int64 = 1000000007
	otherMod   int64 = 1000000009
	base       int64 = 911382323
	wordBits         = 64
	cacheLimit       = 1024
)

type hash struct{ a, b int64 }

func (x hash) add(y hash) hash { return hash{(x.a + y.a) % mod, (x.b + y.b) % otherMod} }
func (x hash) sub(y hash) hash {
	return hash{(x.a - y.a + mod) % mod, (x.b - y.b + otherMod) % otherMod}
}
func (x hash) mul(y hash) hash { return hash{x.a * y.a % mod, x.b * y.b % otherMod} }

type positions struct {
	low, middle []uint64
	top         uint64
}

func below(bit int) uint64 {
	if bit == 0 {
		return 0
	}
	return ^uint64(0) >> uint(wordBits-bit)
}

func (p *positions) insert(position int) {
	block := position / wordBits
	group := block / wordBits
	p.low[block] |= uint64(1) << uint(position%wordBits)
	p.middle[group] |= uint64(1) << uint(block%wordBits)
	p.top |= uint64(1) << uint(group)
}

func (p *positions) erase(position int) {
	block := position / wordBits
	group := block / wordBits
	p.low[block] &^= uint64(1) << uint(position%wordBits)
	if p.low[block] == 0 {
		p.middle[group] &^= uint64(1) << uint(block%wordBits)
		if p.middle[group] == 0 {
			p.top &^= uint64(1) << uint(group)
		}
	}
}

func (p *positions) predecessor(position int) int {
	block := position / wordBits
	lower := p.low[block] & (^uint64(0) >> uint(wordBits-1-position%wordBits))
	if lower == 0 {
		group := block / wordBits
		groups := p.middle[group] & below(block%wordBits)
		if groups == 0 {
			group = bits.Len64(p.top&below(group)) - 1
			groups = p.middle[group]
		}
		block = group*wordBits + bits.Len64(groups) - 1
		lower = p.low[block]
	}
	return block*wordBits + bits.Len64(lower) - 1
}

type solver struct {
	n                              int
	hashes, power, values, fenwick []hash
	following, sources, primes     []int
	positions                      positions
	whole                          hash
	multipliers                    map[int]hash
	cache                          map[hash]int64
}

func newSolver(n int, text []byte) *solver {
	s := &solver{
		n: n, hashes: make([]hash, len(text)+1), power: make([]hash, n+1),
		values: make([]hash, n+1), fenwick: make([]hash, n+1),
		following: make([]int, n+1), sources: make([]int, n+1),
		multipliers: make(map[int]hash), cache: make(map[hash]int64),
	}
	s.positions.low = make([]uint64, n/wordBits+1)
	s.positions.middle = make([]uint64, len(s.positions.low)/wordBits+1)
	s.positions.insert(0)
	for i := range s.following {
		s.following[i] = n
	}
	s.power[0] = hash{1, 1}
	for i := 0; i < n; i++ {
		s.power[i+1] = s.power[i].mul(hash{base, base})
	}
	for i, char := range text {
		s.hashes[i+1] = s.hashes[i].mul(hash{base, base}).add(hash{int64(char), int64(char)})
	}
	s.whole = s.hashes[n]
	s.values[0] = s.whole
	for i := 1; i <= n; i *= 2 {
		s.fenwick[i] = s.whole
	}
	remaining := n
	for divisor := 2; divisor*divisor <= remaining; divisor++ {
		if remaining%divisor == 0 {
			s.primes = append(s.primes, divisor)
			for remaining%divisor == 0 {
				remaining /= divisor
			}
		}
	}
	if remaining > 1 {
		s.primes = append(s.primes, remaining)
	}
	return s
}

// Static slices are weighted by their positions in the current string.
func (s *solver) fingerprint(source, left, right int) hash {
	length := right - left
	return s.hashes[source+length].sub(s.hashes[source].mul(s.power[length])).mul(s.power[s.n-right])
}

func (s *solver) setValue(position int, value hash) {
	old := s.values[position]
	// Fenwick nodes store raw sums of normalized fragment fingerprints.
	for i := position + 1; i <= s.n; i += i & -i {
		s.fenwick[i].a += value.a - old.a
		s.fenwick[i].b += value.b - old.b
	}
	s.values[position] = value
}

func (s *solver) replace(begin, end, source int) {
	start := s.positions.predecessor(begin)
	removed := hash{}
	for position := start; position < end; position = s.following[position] {
		left, right := position, s.following[position]
		if left < begin {
			left = begin
		}
		if right > end {
			right = end
		}
		if left == position && right == s.following[position] {
			removed = removed.add(s.values[position])
		} else {
			removed = removed.add(s.fingerprint(s.sources[position]+left-position, left, right))
		}
	}
	replacement := s.fingerprint(source, begin, end)
	delta := replacement.sub(removed)
	if delta == (hash{}) && end <= s.following[start] {
		return
	}
	s.whole = s.whole.add(delta)
	for position := start; position < end; {
		stop, oldSource := s.following[position], s.sources[position]
		if position < begin {
			s.setValue(position, s.fingerprint(oldSource, position, begin))
			s.following[position] = begin
		} else if position != begin {
			s.setValue(position, hash{})
			s.positions.erase(position)
		}
		if end < stop {
			s.sources[end] = oldSource + end - position
			s.following[end] = stop
			s.setValue(end, s.fingerprint(s.sources[end], end, stop))
			s.positions.insert(end)
		}
		position = stop
	}
	s.sources[begin] = source
	s.following[begin] = end
	s.setValue(begin, replacement)
	s.positions.insert(begin)
}

func (s *solver) prefix(length int) hash {
	position := s.positions.predecessor(length - 1)
	value := hash{}
	for i := position; i > 0; i -= i & -i {
		value.a += s.fenwick[i].a
		value.b += s.fenwick[i].b
	}
	value.a %= mod
	value.b %= otherMod
	if s.following[position] == length {
		return value.add(s.values[position])
	}
	return value.add(s.fingerprint(s.sources[position], position, length))
}

func (s *solver) answer() int64 {
	if answer, ok := s.cache[s.whole]; ok {
		return answer
	}
	period := s.n
	repeated := s.power[s.n].sub(hash{1, 1})
	// Remove prime factors while the shorter prefix still generates the string.
	for _, prime := range s.primes {
		for period%prime == 0 {
			candidate := period / prime
			multiplier, ok := s.multipliers[candidate]
			if !ok {
				multiplier = s.power[candidate].sub(hash{1, 1}).mul(s.power[s.n-candidate])
				s.multipliers[candidate] = multiplier
			}
			if s.whole.mul(multiplier) != s.prefix(candidate).mul(repeated) {
				break
			}
			period = candidate
		}
	}
	result := int64(s.n) * int64(period)
	if len(s.cache) == cacheLimit {
		s.cache = make(map[hash]int64)
	}
	s.cache[s.whole] = result
	return result
}

type reader struct {
	data     []byte
	position int
}

func (r *reader) next() []byte {
	for r.position < len(r.data) && r.data[r.position] <= ' ' {
		r.position++
	}
	start := r.position
	for r.position < len(r.data) && r.data[r.position] > ' ' {
		r.position++
	}
	return r.data[start:r.position]
}

func (r *reader) number() int {
	value := 0
	for _, digit := range r.next() {
		value = value*10 + int(digit-'0')
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := reader{data: data}
	n, m, q := input.number(), input.number(), input.number()
	text := append([]byte(nil), input.next()...)
	starts, lengths := make([]int, m+1), make([]int, m+1)
	lengths[0] = n
	for i := 1; i <= m; i++ {
		part := input.next()
		starts[i], lengths[i] = len(text), len(part)
		text = append(text, part...)
	}
	s := newSolver(n, text)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	fmt.Fprintln(output, s.answer())
	for i := 0; i < q; i++ {
		begin, index := input.number()-1, input.number()
		s.replace(begin, begin+lengths[index], starts[index])
		fmt.Fprintln(output, s.answer())
	}
}
