package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const indexDigits = 5

type city struct {
	joy, arm         int32
	degree, neighbor uint16
	weight, child    uint16
}

func number(input *bufio.Reader) int {
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value
}

func (c *city) add(neighbor, weight uint16) {
	c.degree++
	c.neighbor ^= neighbor
	c.weight ^= weight
}

func main() {
	input := bufio.NewReader(os.Stdin)
	n, flights := number(input), number(input)
	cities := make([]city, n+1)
	var center uint16 = 1
	for i := 1; i <= n; i++ {
		cities[i].joy = int32(number(input))
		if cities[i].joy > cities[center].joy {
			center = uint16(i)
		}
	}
	for i := 0; i < flights; i++ {
		a, b, weight := uint16(number(input)), uint16(number(input)), uint16(number(input))
		cities[a].add(b, weight)
		cities[b].add(a, weight)
	}
	leaves := make([]uint16, 0, n)
	for i := 1; i <= n; i++ {
		if cities[i].degree == 1 {
			leaves = append(leaves, uint16(i))
		}
	}
	best := cities[center].joy
	var left, right uint16
	for i := 0; i < len(leaves); i++ {
		v := leaves[i]
		leaf := cities[v]
		if leaf.degree == 0 {
			continue
		}
		// A leaf has exactly one remaining neighbor and weight in its XOR fields.
		parent := &cities[leaf.neighbor]
		parent.degree--
		parent.neighbor ^= v
		parent.weight ^= leaf.weight
		if parent.degree == 1 {
			leaves = append(leaves, leaf.neighbor)
		}
		branch := leaf.joy + leaf.arm + int32(leaf.weight)
		if total := parent.joy + parent.arm + branch; total > best {
			best = total
			center, left, right = leaf.neighbor, v, parent.child
		}
		if branch > parent.arm {
			parent.arm, parent.child = branch, v
		}
	}
	route := leaves[:0]
	for v := left; v != 0; v = cities[v].child {
		route = append(route, v)
	}
	for i, j := 0, len(route)-1; i < j; i, j = i+1, j-1 {
		route[i], route[j] = route[j], route[i]
	}
	route = append(route, center)
	for v := right; v != 0; v = cities[v].child {
		route = append(route, v)
	}
	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(output, best)
	fmt.Fprintln(output, len(route))
	var digits [indexDigits]byte
	for i, v := range route {
		if i != 0 {
			output.WriteByte(' ')
		}
		output.Write(strconv.AppendInt(digits[:0], int64(v), 10))
	}
	output.WriteByte('\n')
	output.Flush()
}
