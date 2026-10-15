package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	leaf = iota
	direct
	skew
)

var kinds, lefts, rights, values []int

func newNode(kind, left, right, value int) int {
	kinds = append(kinds, kind)
	lefts = append(lefts, left)
	rights = append(rights, right)
	values = append(values, value)
	return len(kinds) - 1
}

// parts lists the children of the maximal run of nodes of the same kind
// below and including node, in order of position.
func parts(node int) []int {
	var out []int
	todo := []int{node}
	for len(todo) > 0 {
		cur := todo[len(todo)-1]
		todo = todo[:len(todo)-1]
		if kinds[cur] == kinds[node] {
			todo = append(todo, rights[cur], lefts[cur])
		} else {
			out = append(out, cur)
		}
	}
	return out
}

const (
	text = iota
	expr
	seq
)

type item struct {
	what, node int
	char       byte
}

// show writes a direct node as a sequence of its parts and a skew node as
// its parts joined by stars from the smallest values up; no recursion, as
// the tree can be 10^4 levels deep.
func show(root int) string {
	var out strings.Builder
	work := []item{{expr, root, 0}}
	for len(work) > 0 {
		it := work[len(work)-1]
		work = work[:len(work)-1]
		switch {
		case it.what == text:
			out.WriteByte(it.char)
		case kinds[it.node] == leaf:
			number := strconv.Itoa(values[it.node])
			if it.what == expr {
				out.WriteString(number)
			} else {
				out.WriteString("(" + number + ")")
			}
		case kinds[it.node] == skew:
			// pushed in reverse: the largest values come out first as text
			for i, child := range parts(it.node) {
				if i > 0 {
					work = append(work, item{text, 0, '*'})
				}
				work = append(work, item{seq, child, 0})
			}
		default:
			children := parts(it.node)
			work = append(work, item{text, 0, ')'})
			for i := len(children) - 1; i >= 0; i-- {
				work = append(work, item{expr, children[i], 0})
				if i > 0 {
					work = append(work, item{text, 0, ','})
				} else {
					work = append(work, item{text, 0, '('})
				}
			}
		}
	}
	// a lone number at the top must still be a sequence
	if kinds[root] == leaf {
		return "(" + out.String() + ")"
	}
	return out.String()
}

type block struct{ lo, hi, node int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// blocks of consecutive positions holding consecutive values; two
	// neighbours whose value ranges touch join into one block
	var stack []block
	for i := 0; i < n; i++ {
		var v int
		fmt.Fscan(in, &v)
		cur := block{v, v, newNode(leaf, -1, -1, v)}
		for len(stack) > 0 {
			prev := stack[len(stack)-1]
			if prev.hi+1 == cur.lo {
				cur.node = newNode(direct, prev.node, cur.node, 0)
			} else if cur.hi+1 == prev.lo {
				cur.node = newNode(skew, prev.node, cur.node, 0)
			} else {
				break
			}
			stack = stack[:len(stack)-1]
			if prev.lo < cur.lo {
				cur.lo = prev.lo
			}
			if prev.hi > cur.hi {
				cur.hi = prev.hi
			}
		}
		stack = append(stack, cur)
	}
	if len(stack) == 1 {
		fmt.Println(show(stack[0].node))
	} else {
		fmt.Println("IMPOSSIBLE")
	}
}
