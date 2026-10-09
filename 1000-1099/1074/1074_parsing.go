package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

// exponents beyond this either give zero or an answer longer than allowed
const expLimit = 1000
const fail = "Not a floating point number"

func isDigit(c byte) bool { return c >= '0' && c <= '9' }

func run(s string, pos int) (string, int) {
	start := pos
	for pos < len(s) && isDigit(s[pos]) {
		pos++
	}
	return s[start:pos], pos
}

func convert(s string, n int) string {
	pos := 0
	negative := false
	if pos < len(s) && (s[pos] == '+' || s[pos] == '-') {
		negative = s[pos] == '-'
		pos++
	}
	whole, pos := run(s, pos)
	frac := ""
	if pos < len(s) && s[pos] == '.' {
		frac, pos = run(s, pos+1)
		if frac == "" {
			return fail
		}
	} else if whole == "" {
		return fail
	}
	exp := 0
	if pos < len(s) && (s[pos] == 'e' || s[pos] == 'E') {
		pos++
		sign := 1
		if pos < len(s) && (s[pos] == '+' || s[pos] == '-') {
			if s[pos] == '-' {
				sign = -1
			}
			pos++
		}
		var power string
		power, pos = run(s, pos)
		if power == "" {
			return fail
		}
		for i := 0; i < len(power); i++ {
			exp = exp*10 + int(power[i]-'0')
			if exp > expLimit {
				exp = expLimit
			}
		}
		exp *= sign
	}
	if pos != len(s) {
		return fail
	}
	// the digits of the number with the decimal point after `point` of them
	mantissa := whole + frac
	point := len(whole) + exp
	if strings.Trim(mantissa, "0") == "" {
		point = 0
	}
	digit := func(i int) byte {
		if i >= 0 && i < len(mantissa) {
			return mantissa[i]
		}
		return '0'
	}
	var head, tail []byte
	for i := 0; i < point; i++ {
		if len(head) > 0 || digit(i) != '0' {
			head = append(head, digit(i))
		}
	}
	if len(head) == 0 {
		head = []byte{'0'}
	}
	for i := point; i < point+n; i++ {
		tail = append(tail, digit(i))
	}
	out := string(head)
	if n > 0 {
		out += "." + string(tail)
	}
	if negative && strings.Trim(string(head)+string(tail), "0") != "" {
		out = "-" + out
	}
	return out
}

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	lines := strings.Split(string(data), "\n")
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for i := 0; i+1 < len(lines); i += 2 {
		s := strings.TrimSuffix(lines[i], "\r")
		if s == "#" {
			break
		}
		n, _ := strconv.Atoi(strings.TrimSpace(lines[i+1]))
		w.WriteString(convert(s, n))
		w.WriteByte('\n')
	}
}
