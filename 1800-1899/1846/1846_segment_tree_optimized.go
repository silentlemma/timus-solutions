package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

// digits are parsed by hand instead of fmt.Fscan; the buffered reader refills,
// so no total input-size bound is needed.
var input = bufio.NewReader(os.Stdin)

func number() int {
	c, _ := input.ReadByte()
	for c < '0' || c > '9' {
		c, _ = input.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		next, err := input.ReadByte()
		if err != nil {
			break
		}
		c = next
	}
	return value
}

func gcd(a, b int32) int32 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
func main() {
	q := number()
	// x <= 10^9: signed 32-bit entries hold the operation and its value.
	operations, values := make([]int32, q), make([]int, q)
	for i := range operations {
		sign, _ := input.ReadByte()
		for sign != '+' && sign != '-' {
			sign, _ = input.ReadByte()
		}
		x := number()
		values[i], operations[i] = x, int32(x)
		if sign == '-' {
			operations[i] = -operations[i]
		}
	}
	sort.Ints(values)
	size := 0
	for _, x := range values {
		if size == 0 || values[size-1] != x {
			values[size] = x
			size++
		}
	}
	values = values[:size]
	// one leaf per distinct value; counts are at most q <= 100000.
	counts, tree := make([]int32, size), make([]int32, 2*size)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, operation := range operations {
		x := operation
		if x < 0 {
			x = -x
		}
		id := sort.SearchInts(values, int(x))
		if operation > 0 {
			counts[id]++
		} else {
			counts[id]--
		}
		v, value := size+id, x
		if counts[id] == 0 {
			value = 0
		}
		if tree[v] != value {
			tree[v] = value
			for v /= 2; v > 0; v /= 2 {
				g := gcd(tree[2*v], tree[2*v+1])
				if g == tree[v] {
					break
				}
				tree[v] = g
			}
		}
		answer := tree[1]
		if answer == 0 {
			answer = 1
		}
		out.WriteString(strconv.Itoa(int(answer)))
		out.WriteByte('\n')
	}
}
