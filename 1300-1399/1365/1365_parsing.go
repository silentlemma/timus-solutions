package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const (
	none = -1 // no term starts here
	bits = 64
)

type parser struct {
	s   string
	pos int
}

func (p *parser) accept(c byte) bool {
	if p.pos < len(p.s) && p.s[p.pos] == c {
		p.pos++
		return true
	}
	return false
}

func isDigit(c byte) bool { return c >= '0' && c <= '9' }

// term reads a number, an operation with its arguments or a bracket
func (p *parser) term() int64 {
	if p.pos < len(p.s) && isDigit(p.s[p.pos]) {
		start := p.pos
		for p.pos < len(p.s) && isDigit(p.s[p.pos]) {
			p.pos++
		}
		v, _ := strconv.ParseInt(p.s[start:p.pos], 10, bits)
		return v
	}
	for _, sign := range []byte("+*/") {
		if p.accept(sign) {
			return p.fold(sign)
		}
	}
	if p.accept('(') {
		x := p.glue(false)
		p.accept(')')
		return x
	}
	return none
}

// fold applies an operation to its arguments: glued terms split by ';'
func (p *parser) fold(sign byte) int64 {
	a := p.glue(true)
	for p.accept(';') {
		b := p.glue(true)
		switch {
		case sign == '+':
			a += b
		case sign == '*':
			a *= b
		case b == 0:
			a = 0
		default:
			a /= b
		}
	}
	return a
}

// glue joins terms written one after another as decimal strings. Inside an
// operation ';' ends the argument; elsewhere it glues the whole rest, and a
// missing term counts as 1
func (p *parser) glue(inside bool) int64 {
	var parts []int64
	for x := p.term(); x != none || len(parts) == 0; x = p.term() {
		parts = append(parts, x)
		if p.pos < len(p.s) && p.s[p.pos] == ';' {
			if inside {
				break
			}
			p.pos++
			parts = append(parts, p.glue(false))
		}
	}
	var text strings.Builder
	for _, x := range parts {
		if x < 0 {
			x = -x
		}
		text.WriteString(strconv.FormatInt(x, 10))
	}
	v, err := strconv.ParseInt(text.String(), 10, bits)
	if err != nil {
		v = math.MaxInt64 // a glued number that does not fit is cut
	}
	return v
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 1; in.Scan(); i++ {
		p := parser{s: in.Text()}
		fmt.Fprintf(out, "Expression %d evaluates to: %d\n", i, p.glue(false))
	}
}
