package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

// linear independence is tested modulo a large prime: exact, and a set that is
// independent modulo the prime is independent over the rationals
const p = 2147483647

func power(b, e int64) int64 {
	r := int64(1)
	for b %= p; e > 0; e /= 2 {
		if e%2 == 1 {
			r = r * b % p
		}
		b = b * b % p
	}
	return r
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	m, n := next(), next()
	vec := make([][]int64, m)
	for i := range vec {
		vec[i] = make([]int64, n)
		for k := range vec[i] {
			vec[i][k] = (int64(next())%p + p) % p
		}
	}
	cost := make([]int, m)
	for i := range cost {
		cost[i] = next()
	}
	// the greedy algorithm of a matroid: the cheapest vectors first, and among
	// equal prices the smaller numbers first, which gives the smallest list too
	order := make([]int, m)
	for i := range order {
		order[i] = i
	}
	sort.SliceStable(order, func(a, b int) bool { return cost[order[a]] < cost[order[b]] })
	// rows of the basis, each with a pivot coordinate equal to 1 and zero in
	// the pivots of the rows before it
	var rows [][]int64
	var pivots, chosen []int
	for _, i := range order {
		if len(chosen) == n {
			break
		}
		v := append([]int64(nil), vec[i]...)
		for r, row := range rows {
			f := v[pivots[r]]
			if f == 0 {
				continue
			}
			for k := range v {
				v[k] = ((v[k]-f*row[k])%p + p) % p
			}
		}
		piv := 0
		for piv < n && v[piv] == 0 {
			piv++
		}
		if piv == n {
			continue
		}
		inv := power(v[piv], p-2)
		for k := range v {
			v[k] = v[k] * inv % p
		}
		rows = append(rows, v)
		pivots = append(pivots, piv)
		chosen = append(chosen, i)
	}
	if len(chosen) < n {
		fmt.Println(0)
		return
	}
	total := 0
	for _, i := range chosen {
		total += cost[i]
	}
	sort.Ints(chosen)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fprintln(w, total)
	for _, i := range chosen {
		fmt.Fprintln(w, i+1)
	}
}
