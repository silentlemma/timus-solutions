package main

import (
	"bufio"
	"os"
	"strconv"
)

const maximumSalary int32 = 1000000000
const decimalDigits = 10

type employee struct {
	parent, offset, low, high int32
}

func number(in *bufio.Reader) int32 {
	c, err := in.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.ReadByte()
	}
	negative := c == '-'
	if negative {
		c, err = in.ReadByte()
	}
	var value int32
	for err == nil && c >= '0' && c <= '9' {
		value = 10*value + int32(c-'0')
		c, err = in.ReadByte()
	}
	if negative {
		return -value
	}
	return value
}

func find(staff []employee, vertex int32) int32 {
	node := &staff[vertex]
	if node.parent < 0 {
		return vertex
	}
	parent := node.parent
	node.parent = find(staff, parent)
	node.offset += staff[parent].offset
	return node.parent
}

func join(staff []employee, a, b, difference int32) bool {
	left, right := find(staff, a), find(staff, b)
	shift := staff[a].offset - staff[b].offset - difference
	if left == right {
		return shift == 0
	}
	// Roots store negative sizes. Attach the smaller component to the larger one.
	if staff[left].parent > staff[right].parent {
		left, right, shift = right, left, -shift
	}
	root, child := &staff[left], &staff[right]
	// Express the child's permissible salaries in the root's coordinates.
	if low := child.low - shift; root.low < low {
		root.low = low
	}
	if high := child.high - shift; root.high > high {
		root.high = high
	}
	if root.low > root.high {
		return false
	}
	root.parent += child.parent
	child.parent, child.offset = left, shift
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	people, statements := number(in), number(in)
	staff := make([]employee, people)
	for i := range staff {
		staff[i] = employee{parent: -1, high: maximumSalary}
	}
	staff[0].high = 0
	var digits [decimalDigits]byte
	for k := int32(1); k <= statements; k++ {
		a, b, difference := number(in), number(in), number(in)
		if !join(staff, a, b, difference) {
			out.WriteString("Impossible after ")
			out.Write(strconv.AppendInt(digits[:0], int64(k), 10))
			out.WriteString(" statements\n")
			return
		}
	}
	out.WriteString("Possible\n")
	for i := range staff {
		root := find(staff, int32(i))
		salary := staff[root].low + staff[i].offset
		out.Write(strconv.AppendInt(digits[:0], int64(salary), 10))
		out.WriteByte('\n')
	}
}
