package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

type Input struct {
	data []byte
	pos  int
}

func (in *Input) next() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	var value int64
	for in.pos < len(in.data) && in.data[in.pos] >= '0' {
		value = value*10 + int64(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func power(base, exponent, modulus int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent >>= 1
	}
	return result
}

type Group struct {
	prime   int64
	full    int64
	factors []int64
}

func newGroup(prime int64) Group {
	group := Group{prime: prime, full: prime - 1}
	remaining := group.full
	for factor := int64(2); factor*factor <= remaining; factor++ {
		if remaining%factor == 0 {
			group.factors = append(group.factors, factor)
			for remaining%factor == 0 {
				remaining /= factor
			}
		}
	}
	if remaining > 1 {
		group.factors = append(group.factors, remaining)
	}
	return group
}

// The known subgroup has index limit; only its missing factors need testing.
func (group *Group) subgroupOrder(value, limit int64) int64 {
	if value == 1 {
		return group.full / limit
	}
	if value == group.prime-1 {
		return group.full / gcd(limit, group.full/2)
	}
	order := group.full
	for _, factor := range group.factors {
		for limit%factor == 0 {
			candidate := order / factor
			if power(value, candidate, group.prime) != 1 {
				break
			}
			order = candidate
			limit /= factor
		}
	}
	return order
}

type GcdTree struct {
	base int
	full int64
	data []int64
}

func newGcdTree(values []int64, group *Group) GcdTree {
	base := 1
	for base < len(values) {
		base *= 2
	}
	tree := GcdTree{base: base, full: group.full, data: make([]int64, base*2)}
	for i := range tree.data {
		tree.data[i] = group.full
	}
	for i := 1; i < len(values); i++ {
		tree.data[base+i] = group.full / group.subgroupOrder(values[i], group.full)
	}
	for i := base - 1; i > 0; i-- {
		tree.data[i] = gcd(tree.data[i*2], tree.data[i*2+1])
	}
	return tree
}

func (tree *GcdTree) set(position int, value int64) {
	position += tree.base
	if tree.data[position] == value {
		return
	}
	tree.data[position] = value
	for position /= 2; position > 0; position /= 2 {
		value = gcd(tree.data[position*2], tree.data[position*2+1])
		if tree.data[position] == value {
			break
		}
		tree.data[position] = value
	}
}

func (tree *GcdTree) query(left, right int) int64 {
	result := tree.full
	for left, right = left+tree.base, right+tree.base; left < right && result > 1; {
		if left&1 != 0 {
			result = gcd(result, tree.data[left])
			left++
		}
		if right&1 != 0 {
			right--
			result = gcd(result, tree.data[right])
		}
		left /= 2
		right /= 2
	}
	return result
}

type Fenwick struct {
	prime int64
	data  []int64
}

func newFenwick(size int, prime int64) Fenwick {
	tree := Fenwick{prime: prime, data: make([]int64, size+1)}
	for i := range tree.data {
		tree.data[i] = 1
	}
	return tree
}

func (tree *Fenwick) multiply(position int, value int64) {
	for position < len(tree.data) {
		tree.data[position] = tree.data[position] * value % tree.prime
		position += position & -position
	}
}

func (tree *Fenwick) prefix(position int) int64 {
	result := int64(1)
	for position > 0 {
		result = result * tree.data[position] % tree.prime
		position &= position - 1
	}
	return result
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := Input{data: data}
	prime, n, q := in.next(), int(in.next()), int(in.next())
	original := make([]int64, n)
	for i := range original {
		original[i] = in.next()
	}
	group := newGroup(prime)
	prefix := make([]int64, n+1)
	prefix[0] = 1
	for i, value := range original {
		prefix[i+1] = prefix[i] * value % prime
	}
	difference := make([]int64, n)
	difference[0] = 1
	inverse := power(prefix[n], prime-2, prime)
	// Batch inversion forms all adjacent ratios with one modular exponentiation.
	for i := n - 1; i >= 0; i-- {
		inverseValue := inverse * prefix[i] % prime
		if i+1 < n {
			difference[i+1] = original[i+1] * inverseValue % prime
		}
		inverse = inverse * original[i] % prime
	}
	indices := newGcdTree(difference, &group)
	multipliers := newFenwick(n, prime)
	output := make([]byte, 0)
	for query := 0; query < q; query++ {
		kind, left, right := in.next(), int(in.next())-1, int(in.next())
		if kind == 1 {
			value := in.next()
			if value == 1 {
				continue
			}
			multipliers.multiply(left+1, value)
			if left > 0 {
				difference[left] = difference[left] * value % prime
				index := group.full / group.subgroupOrder(difference[left], group.full)
				indices.set(left, index)
			}
			if right < n {
				inverseValue := power(value, prime-2, prime)
				multipliers.multiply(right+1, inverseValue)
				difference[right] = difference[right] * inverseValue % prime
				index := group.full / group.subgroupOrder(difference[right], group.full)
				indices.set(right, index)
			}
		} else {
			index := indices.query(left+1, right)
			answer := group.full
			if index > 1 {
				value := original[left] * multipliers.prefix(left+1) % prime
				answer = group.subgroupOrder(value, index)
			}
			output = strconv.AppendInt(output, answer, 10)
			output = append(output, '\n')
		}
	}
	os.Stdout.Write(output)
}
