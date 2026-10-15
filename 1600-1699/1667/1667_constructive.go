package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	rootLimit = 316227766 // the largest integer whose square is at most 10^17
	legs      = 40        // Pythagorean pairs from m^2 - n^2 and 2mn with n < m < legs

	starts   = 30 // first terms of the arithmetic sequences
	steps    = 6  // their differences
	offsets  = 30 // where the runs of consecutive primes start
	primeCnt = 80
	half     = 32 // a reduced fraction x / y is stored as x << half | y
)

type list struct {
	nums   []int64
	ratios []int64 // sorted reduced fractions x / y < 1
	top    int64
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// fromUs: for u_1..u_k with S = sum of u^2, the numbers 2u_1, ..., 2u_k
// and S - 1 have squares adding up to (S + 1)^2; nil if they repeat.
func fromUs(us []int64) []int64 {
	total := int64(0)
	var nums []int64
	seen := map[int64]bool{}
	for _, u := range us {
		total += u * u
		nums = append(nums, 2*u)
		seen[2*u] = true
	}
	if seen[total-1] || len(seen) != len(us) {
		return nil
	}
	return append(nums, total-1)
}

func makeList(nums []int64) list {
	l := list{nums: nums}
	for _, x := range nums {
		if x > l.top {
			l.top = x
		}
		for _, y := range nums {
			if x < y {
				g := gcd(x, y)
				l.ratios = append(l.ratios, (x/g)<<half|(y/g))
			}
		}
	}
	sort.Slice(l.ratios, func(i, j int) bool { return l.ratios[i] < l.ratios[j] })
	return l
}

// lists gives lists of distinct positive integers whose squares add up to
// a square, smallest maximum first.
func lists(size int, primes []int64) []list {
	var found [][]int64
	switch size {
	case 1:
		found = append(found, []int64{1})
	case 2:
		for m := int64(2); m < legs; m++ {
			for n := int64(1); n < m; n++ {
				if gcd(m, n) == 1 && (m-n)%2 == 1 {
					found = append(found, []int64{m*m - n*n, 2 * m * n})
				}
			}
		}
	default:
		k := size - 1
		for s := int64(1); s < starts; s++ {
			for d := int64(1); d <= steps; d++ {
				us := make([]int64, k)
				for i := range us {
					us[i] = s + d*int64(i)
				}
				found = append(found, fromUs(us))
			}
		}
		for off := 0; off < offsets; off++ {
			found = append(found, fromUs(primes[off:off+k]))
		}
	}
	var out []list
	for _, nums := range found {
		if nums != nil {
			out = append(out, makeList(nums))
		}
	}
	sort.SliceStable(out, func(i, j int) bool { return out[i].top < out[j].top })
	return out
}

func disjoint(x, y []int64) bool {
	i, j := 0, 0
	for i < len(x) && j < len(y) {
		if x[i] == y[j] {
			return false
		}
		if x[i] < y[j] {
			i++
		} else {
			j++
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var primes []int64
	for n := int64(2); len(primes) < primeCnt; n++ {
		prime := true
		for _, p := range primes {
			if p*p > n {
				break
			}
			if n%p == 0 {
				prime = false
				break
			}
		}
		if prime {
			primes = append(primes, n)
		}
	}
	var t int
	fmt.Fscan(in, &t)
	pool := map[int][]list{}
	for k := 0; k < t; k++ {
		var rows, cols int
		fmt.Fscan(in, &rows, &cols)
		for _, size := range []int{rows, cols} {
			if _, ok := pool[size]; !ok {
				pool[size] = lists(size, primes)
			}
		}
		// entry (i, j) is (a_i b_j)^2; two products a_i b_j and a_k b_l are
		// equal exactly when a_i / a_k = b_l / b_j, so no ratio may be shared
		var found, other *list
		smallest := pool[cols][0].top
		for i := range pool[rows] {
			a := &pool[rows][i]
			if a.top*smallest > rootLimit || found != nil {
				break
			}
			for j := range pool[cols] {
				b := &pool[cols][j]
				if a.top*b.top > rootLimit {
					break
				}
				if disjoint(a.ratios, b.ratios) {
					found, other = a, b
					break
				}
			}
		}
		if k > 0 {
			out.WriteString("\n")
		}
		if found == nil {
			out.WriteString("-1\n")
			continue
		}
		for _, x := range found.nums {
			words := make([]string, len(other.nums))
			for j, y := range other.nums {
				words[j] = strconv.FormatInt(x*y*x*y, 10)
			}
			out.WriteString(strings.Join(words, " ") + "\n")
		}
	}
}
