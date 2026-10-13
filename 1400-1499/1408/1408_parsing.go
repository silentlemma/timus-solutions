package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"unicode"
)

const letters = 26

type powers [letters]int

// number: the number of digits starting at pos and the position after it.
func number(s string, pos int) (int64, int) {
	value := int64(0)
	for pos < len(s) && s[pos] >= '0' && s[pos] <= '9' {
		value = value*10 + int64(s[pos]-'0')
		pos++
	}
	return value, pos
}

// parse: a polynomial as a map from the powers of a .. z to coefficients.
func parse(line string) map[powers]int64 {
	s := strings.Map(func(r rune) rune {
		if unicode.IsSpace(r) {
			return -1 // spaces may stand anywhere
		}
		return r
	}, line)
	poly := map[powers]int64{}
	pos, sign := 0, int64(1)
	for pos < len(s) {
		if s[pos] == '+' || s[pos] == '-' {
			sign = 1
			if s[pos] == '-' {
				sign = -1
			}
			pos++
		}
		coef := int64(1)
		var p powers
		for {
			if s[pos] >= '0' && s[pos] <= '9' {
				var value int64
				value, pos = number(s, pos)
				coef *= value
			} else {
				v := int(s[pos] - 'a')
				pos++
				e := int64(1)
				if pos < len(s) && s[pos] == '^' {
					e, pos = number(s, pos+1)
				}
				p[v] += int(e)
			}
			if pos < len(s) && s[pos] == '*' {
				pos++
			} else {
				break
			}
		}
		poly[p] += sign * coef
	}
	return poly
}

func main() {
	in := bufio.NewReader(os.Stdin)
	a, _ := in.ReadString('\n')
	b, _ := in.ReadString('\n')
	first, second := parse(a), parse(b)
	product := map[powers]int64{}
	for p, x := range first {
		for q, y := range second {
			var r powers
			for v := 0; v < letters; v++ {
				r[v] = p[v] + q[v]
			}
			product[r] += x * y
		}
	}
	type term struct {
		p    powers
		coef int64
	}
	var terms []term
	for p, c := range product {
		if c != 0 {
			terms = append(terms, term{p, c})
		}
	}
	// by total degree, then by the powers of a, b, ... from the largest
	sort.Slice(terms, func(i, j int) bool {
		si, sj := 0, 0
		for v := 0; v < letters; v++ {
			si += terms[i].p[v]
			sj += terms[j].p[v]
		}
		if si != sj {
			return si > sj
		}
		for v := 0; v < letters; v++ {
			if terms[i].p[v] != terms[j].p[v] {
				return terms[i].p[v] > terms[j].p[v]
			}
		}
		return false
	})
	var out strings.Builder
	for k, t := range terms {
		var factors []string
		for v, e := range t.p {
			if e == 1 {
				factors = append(factors, string(rune('a'+v)))
			} else if e > 1 {
				factors = append(factors, string(rune('a'+v))+"^"+strconv.Itoa(e))
			}
		}
		size := t.coef
		if size < 0 {
			size = -size
		}
		if size != 1 || len(factors) == 0 {
			factors = append([]string{strconv.FormatInt(size, 10)}, factors...)
		}
		body := strings.Join(factors, "*")
		switch {
		case k == 0 && t.coef < 0:
			out.WriteString("-" + body)
		case k == 0:
			out.WriteString(body)
		case t.coef < 0:
			out.WriteString(" - " + body)
		default:
			out.WriteString(" + " + body)
		}
	}
	if out.Len() == 0 {
		out.WriteString("0")
	}
	fmt.Println(out.String())
}
