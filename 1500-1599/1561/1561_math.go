package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var days = []string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

const week = 7

func dayOf(word string) int {
	for i, d := range days {
		if d == word {
			return i
		}
	}
	return -1
}

func inverse(x int) int {
	for y := 1; y < week; y++ {
		if x*y%week == 1 {
			return y
		}
	}
	return 0
}

func mod(x int) int {
	return (x%week + week) % week
}

// row is a row of an echelon basis over the residues modulo 7, with a 1 at
// its first non-zero place
type row struct {
	pivot        int
	coefficients []int
	right        int
}

func main() {
	in := bufio.NewScanner(bufio.NewReader(os.Stdin))
	in.Split(bufio.ScanWords)
	word := func() string {
		in.Scan()
		return in.Text()
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	n, _ := strconv.Atoi(word())
	sorts := 0
	var basis []row
	crazy := false
	// subtract basis rows until no pivot of the basis stays non-zero
	reduce := func(v []int, value int) int {
		for _, r := range basis {
			c := v[r.pivot]
			if c == 0 {
				continue
			}
			// the row is shorter if sorts appeared after it
			for i := r.pivot; i < len(r.coefficients); i++ {
				v[i] = mod(v[i] - c*r.coefficients[i])
			}
			value = mod(value - c*r.right)
		}
		return value
	}
	for q := 0; q < n; q++ {
		kind := word()
		if kind == "Add" {
			sorts++
			continue
		}
		// the numbers of the query up to its first weekday
		var v []int
		w := word()
		for dayOf(w) < 0 {
			a, _ := strconv.Atoi(w)
			v = append(v, a%week)
			w = word()
		}
		for len(v) < sorts {
			v = append(v, 0)
		}
		start := dayOf(w)
		if kind == "Learn" {
			finish := dayOf(word())
			if crazy {
				continue
			}
			value := reduce(v, mod(finish-start))
			pivot := 0
			for pivot < len(v) && v[pivot] == 0 {
				pivot++
			}
			if pivot == len(v) {
				crazy = value != 0
				continue
			}
			scale := inverse(v[pivot])
			for i := range v {
				v[i] = v[i] * scale % week
			}
			at := sort.Search(len(basis), func(i int) bool { return basis[i].pivot > pivot })
			basis = append(basis, row{})
			copy(basis[at+1:], basis[at:])
			basis[at] = row{pivot, v, value * scale % week}
		} else if crazy {
			fmt.Fprintln(out, "Already crazy")
		} else {
			value := reduce(v, 0)
			known := true
			for _, c := range v {
				if c != 0 {
					known = false
				}
			}
			if known {
				fmt.Fprintln(out, days[mod(start-value)])
			} else {
				fmt.Fprintln(out, "Don't know")
			}
		}
	}
}
