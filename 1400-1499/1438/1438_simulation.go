package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	limit   = 10000000
	bufSize = 1 << 16
	bits    = 64
)

const (
	opSet = iota
	opNot
	opCalc
	opEnd
	opPrint
	opGoto
	opIf
)

// the operations and comparisons in the order of their codes
const (
	calcAdd = iota
	calcSub
	calcMul
	calcDiv
	calcMod
	calcOr
	calcAnd
	calcXor
)

const (
	testEq = iota
	testNe
	testGe
	testGt
	testLe
	testLt
)

var calcs = []string{"+", "-", "*", "/", "%", "or", "and", "xor"}
var tests = []string{"==", "!=", ">=", ">", "<=", "<"}

// operands are slots in one value table: variables and constants
type op struct{ kind, dst, a, b, target, code int }

func codeOf(list []string, s string) int {
	for i, x := range list {
		if x == s {
			return i
		}
	}
	return -1
}

func calc(code int, a, b int64) int64 {
	switch code {
	case calcAdd:
		return a + b
	case calcSub:
		return a - b
	case calcMul:
		return a * b
	case calcDiv:
		return a / b // rounds towards zero
	case calcMod:
		m := b
		if m < 0 {
			m = -m
		}
		return (a%b + m) % m // never negative
	case calcOr:
		return a | b
	case calcAnd:
		return a & b
	}
	return a ^ b
}

func test(code int, a, b int64) bool {
	switch code {
	case testEq:
		return a == b
	case testNe:
		return a != b
	case testGe:
		return a >= b
	case testGt:
		return a > b
	case testLe:
		return a <= b
	}
	return a < b
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, bufSize)
	// a line is "label:", "label: command" or "command"; lines with only a label are no commands
	labels := map[string]int{}
	var commands [][]string
	for {
		line, err := reader.ReadString('\n')
		t := strings.Fields(line)
		if len(t) > 0 && strings.HasSuffix(t[0], ":") {
			labels[strings.ToLower(strings.TrimSuffix(t[0], ":"))] = len(commands)
			t = t[1:]
		}
		if len(t) > 0 {
			commands = append(commands, t)
		}
		if err != nil {
			break
		}
	}
	names := map[string]int{}
	var values []int64
	operand := func(tok string) int {
		if v, err := strconv.ParseInt(tok, 10, bits); err == nil {
			values = append(values, v)
			return len(values) - 1
		}
		if k, ok := names[tok]; ok {
			return k
		}
		values = append(values, 0)
		names[tok] = len(values) - 1
		return len(values) - 1
	}
	ops := make([]op, len(commands))
	for pc, t := range commands {
		o := &ops[pc]
		head := strings.ToLower(t[0])
		switch {
		case len(t) > 1 && t[1] == "=":
			o.dst = operand(t[0])
			// a value, "not" and a value, or a value, an operation and a value
			rest := t[2:]
			switch len(rest) {
			case 1:
				o.kind, o.a = opSet, operand(rest[0])
			case 2:
				o.kind, o.a = opNot, operand(rest[1])
			default:
				o.kind, o.a, o.b = opCalc, operand(rest[0]), operand(rest[2])
				o.code = codeOf(calcs, strings.ToLower(rest[1]))
			}
		case head == "end":
			o.kind = opEnd
		case head == "print":
			o.kind, o.a = opPrint, operand(t[1])
		case head == "goto":
			o.kind, o.target = opGoto, labels[strings.ToLower(t[1])]
		default: // a conditional jump: two values around a comparison, then a label
			rest := t[1:]
			o.kind, o.a, o.b = opIf, operand(rest[0]), operand(rest[2])
			o.code = codeOf(tests, rest[1])
			o.target = labels[strings.ToLower(rest[len(rest)-1])]
		}
	}
	assigned := make([]bool, len(values))
	var out strings.Builder
	pc, size, executed, ended := 0, len(ops), 0, false
	for pc < size && executed < limit {
		o := &ops[pc]
		pc++
		executed++
		switch o.kind {
		case opSet:
			values[o.dst] = values[o.a]
			assigned[o.dst] = true
		case opNot:
			values[o.dst] = ^values[o.a]
			assigned[o.dst] = true
		case opCalc:
			values[o.dst] = calc(o.code, values[o.a], values[o.b])
			assigned[o.dst] = true
		case opEnd:
			ended, pc = true, size
		case opPrint:
			out.WriteString(strconv.FormatInt(values[o.a], 10) + "\n")
		case opGoto:
			pc = o.target
		case opIf:
			if test(o.code, values[o.a], values[o.b]) {
				pc = o.target
			}
		}
	}
	if !ended && executed == limit {
		// ten million commands done and the program still runs
		out.WriteString("Program terminated. Variables state:\n")
		var list []string
		for name := range names {
			list = append(list, name)
		}
		sort.Strings(list)
		for _, name := range list {
			if k := names[name]; assigned[k] {
				out.WriteString(name + ": " + strconv.FormatInt(values[k], 10) + "\n")
			}
		}
	}
	os.Stdout.WriteString(out.String())
}
