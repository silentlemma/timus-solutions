package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// node is OR, AND, NOT, a constant or a register, with up to two children
type node struct {
	kind        string
	left, right *node
	value       bool
	name        byte
}

type parser struct {
	tokens []string
	pos    int
}

func (p *parser) peek() string {
	if p.pos < len(p.tokens) {
		return p.tokens[p.pos]
	}
	return ""
}

// disjunction is the top of a recursive descent: NOT binds tightest, OR loosest
func (p *parser) disjunction() *node {
	n := p.conjunction()
	for p.peek() == "OR" {
		p.pos++
		n = &node{kind: "OR", left: n, right: p.conjunction()}
	}
	return n
}

func (p *parser) conjunction() *node {
	n := p.negation()
	for p.peek() == "AND" {
		p.pos++
		n = &node{kind: "AND", left: n, right: p.negation()}
	}
	return n
}

func (p *parser) negation() *node {
	word := p.tokens[p.pos]
	p.pos++
	switch word {
	case "NOT":
		return &node{kind: "NOT", left: p.negation()}
	case "(":
		n := p.disjunction()
		p.pos++
		return n
	case "TRUE", "FALSE":
		return &node{kind: "CONST", value: word == "TRUE"}
	}
	return &node{kind: "REG", name: word[0]}
}

func value(n *node, reg map[byte]bool) bool {
	switch n.kind {
	case "OR":
		return value(n.left, reg) || value(n.right, reg)
	case "AND":
		return value(n.left, reg) && value(n.right, reg)
	case "NOT":
		return !value(n.left, reg)
	case "CONST":
		return n.value
	}
	return reg[n.name]
}

func isLetter(c byte) bool { return c >= 'A' && c <= 'Z' }

func main() {
	in := bufio.NewReader(os.Stdin)
	expr, _ := in.ReadString('\n')
	var tokens []string
	for i := 0; i < len(expr); {
		if isLetter(expr[i]) {
			j := i
			for j < len(expr) && isLetter(expr[j]) {
				j++
			}
			tokens = append(tokens, expr[i:j])
			i = j
			continue
		}
		if expr[i] == '(' || expr[i] == ')' {
			tokens = append(tokens, expr[i:i+1])
		}
		i++
	}
	root := (&parser{tokens: tokens}).disjunction()
	var n, m, k int
	fmt.Fscan(in, &n, &m, &k)
	type point struct{ x, y int }
	forks := map[point]bool{}
	for i := 0; i < m; i++ {
		var x, y int
		fmt.Fscan(in, &x, &y)
		forks[point{x, y}] = true
	}
	switches := map[point]byte{}
	for i := 0; i < k; i++ {
		var x, y int
		var name string
		fmt.Fscan(in, &x, &y, &name)
		switches[point{x, y}] = name[0]
	}
	reg := map[byte]bool{}
	x, y, dx, dy := 0, 0, 1, 0
	var out strings.Builder
	for -n <= x && x <= n && -n <= y && y <= n {
		fmt.Fprintf(&out, "%d %d\n", x, y)
		if name, ok := switches[point{x, y}]; ok {
			reg[name] = !reg[name]
		}
		if forks[point{x, y}] {
			// TRUE turns right, FALSE turns left
			if value(root, reg) {
				dx, dy = dy, -dx
			} else {
				dx, dy = -dy, dx
			}
		}
		x, y = x+dx, y+dy
	}
	fmt.Print(out.String())
}
