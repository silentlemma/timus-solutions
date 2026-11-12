package main

import (
	"bufio"
	"os"
	"strconv"
)

const registerCount = 26
const expressionLimit = 250
const fork = 1
const switchOffset = 2
const outputSize = 8192
const pointReserve = 12
const decimalBase = 10

const (
	trueCode byte = registerCount + iota
	falseCode
	notCode
	andCode
	orCode
	openParen
	closeParen
	endToken
)

type parser struct {
	expression string
	pos        int
	token      byte
	code       [expressionLimit]byte
	size       int
	relevant   uint32
}

func (p *parser) next() {
	for p.pos < len(p.expression) && p.expression[p.pos] <= ' ' {
		p.pos++
	}
	if p.pos == len(p.expression) {
		p.token = endToken
		return
	}
	c := p.expression[p.pos]
	if c == '(' || c == ')' {
		p.pos++
		if c == '(' {
			p.token = openParen
		} else {
			p.token = closeParen
		}
		return
	}
	start := p.pos
	for p.pos < len(p.expression) && p.expression[p.pos] >= 'A' && p.expression[p.pos] <= 'Z' {
		p.pos++
	}
	switch p.expression[start:p.pos] {
	case "TRUE":
		p.token = trueCode
	case "FALSE":
		p.token = falseCode
	case "NOT":
		p.token = notCode
	case "AND":
		p.token = andCode
	case "OR":
		p.token = orCode
	default:
		p.token = c - 'A'
	}
}

func (p *parser) emit(op byte) { p.code[p.size] = op; p.size++ }

func (p *parser) disjunction() {
	p.conjunction()
	for p.token == orCode {
		p.next()
		p.conjunction()
		p.emit(orCode)
	}
}

func (p *parser) conjunction() {
	p.unary()
	for p.token == andCode {
		p.next()
		p.unary()
		p.emit(andCode)
	}
}

func (p *parser) unary() {
	if p.token == notCode {
		p.next()
		p.unary()
		p.emit(notCode)
	} else if p.token == openParen {
		p.next()
		p.disjunction()
		p.next()
	} else {
		p.emit(p.token)
		if p.token < registerCount {
			p.relevant |= uint32(1) << p.token
		}
		p.next()
	}
}

func (p *parser) value(registers uint32) bool {
	var stack [expressionLimit]bool
	top := 0
	for _, op := range p.code[:p.size] {
		if op < registerCount {
			stack[top] = registers>>op&1 != 0
			top++
		} else {
			switch op {
			case trueCode, falseCode:
				stack[top] = op == trueCode
				top++
			case notCode:
				stack[top-1] = !stack[top-1]
			case andCode:
				top--
				stack[top-1] = stack[top-1] && stack[top]
			case orCode:
				top--
				stack[top-1] = stack[top-1] || stack[top]
			}
		}
	}
	return stack[0]
}

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	negative := c == '-'
	if negative {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c, _ = in.ReadByte()
	}
	if negative {
		return -value
	}
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	expression, _ := in.ReadString('\n')
	p := parser{expression: expression}
	p.next()
	p.disjunction()
	n, m, k := number(in), number(in), number(in)
	width := 2*n + 1
	field := make([]byte, width*width)
	for i := 0; i < m; i++ {
		x, y := number(in), number(in)
		field[(x+n)*width+y+n] = fork
	}
	for i := 0; i < k; i++ {
		x, y := number(in), number(in)
		c, _ := in.ReadByte()
		for c <= ' ' {
			c, _ = in.ReadByte()
		}
		field[(x+n)*width+y+n] = c - 'A' + switchOffset
	}
	var storage [outputSize]byte
	output := storage[:0]
	x, y, dx, dy := 0, 0, 1, 0
	registers, cachedMask := uint32(0), uint32(0)
	cached, known := false, false
	for x >= -n && x <= n && y >= -n && y <= n {
		if len(output)+pointReserve > cap(output) {
			os.Stdout.Write(output)
			output = storage[:0]
		}
		output = strconv.AppendInt(output, int64(x), decimalBase)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(y), decimalBase)
		output = append(output, '\n')
		object := field[(x+n)*width+y+n]
		if object >= switchOffset {
			registers ^= uint32(1) << (object - switchOffset)
		} else if object == fork {
			mask := registers & p.relevant
			if !known || mask != cachedMask {
				cached = p.value(mask)
				cachedMask = mask
				known = true
			}
			if cached {
				dx, dy = dy, -dx
			} else {
				dx, dy = -dy, dx
			}
		}
		x += dx
		y += dy
	}
	os.Stdout.Write(output)
}
