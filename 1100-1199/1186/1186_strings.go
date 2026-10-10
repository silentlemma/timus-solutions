package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"strconv"
	"strings"
)

// number reads the number starting at s[i] (1 if there is none) and
// returns it with the index after it
func number(s string, i int) (int64, int) {
	j := i
	for j < len(s) && s[j] >= '0' && s[j] <= '9' {
		j++
	}
	if j == i {
		return 1, j
	}
	v, _ := strconv.Atoi(s[i:j])
	return int64(v), j
}

func totals(formula string) map[string]int64 {
	result := map[string]int64{}
	for _, term := range strings.Split(formula, "+") {
		times, i := number(term, 0)
		// one level per open bracket; a closing bracket multiplies its level
		// by the number after it and adds it to the level outside
		stack := []map[string]int64{{}}
		for i < len(term) {
			switch term[i] {
			case '(':
				stack = append(stack, map[string]int64{})
				i++
			case ')':
				inner := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				var k int64
				k, i = number(term, i+1)
				for name, count := range inner {
					stack[len(stack)-1][name] += count * k
				}
			default:
				j := i + 1
				if j < len(term) && term[j] >= 'a' && term[j] <= 'z' {
					j++
				}
				k, end := number(term, j)
				stack[len(stack)-1][term[i:j]] += k
				i = end
			}
		}
		for name, count := range stack[0] {
			result[name] += count * times
		}
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var left string
	var n int
	fmt.Fscan(in, &left, &n)
	want := totals(left)
	for q := 0; q < n; q++ {
		var right string
		fmt.Fscan(in, &right)
		sign := "!="
		if reflect.DeepEqual(totals(right), want) {
			sign = "=="
		}
		fmt.Fprintln(out, left+sign+right)
	}
}
