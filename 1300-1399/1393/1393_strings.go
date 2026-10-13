package main

import (
	"bufio"
	"fmt"
	"os"
)

const alphabet = 256

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var text string
	fmt.Fscan(in, &n, &text)
	text = text[:n]
	// the shortest period p of the cyclic string: T is u repeated n / p times
	pi := make([]int32, n)
	for i := 1; i < n; i++ {
		k := pi[i-1]
		for k > 0 && text[i] != text[k] {
			k = pi[k-1]
		}
		if text[i] == text[k] {
			k++
		}
		pi[i] = k
	}
	p := n - int(pi[n-1])
	if n%p != 0 {
		p = n
	}
	pi = nil
	// sort the rotations of u by doubling, all of them distinct
	order, cls := make([]int32, p), make([]int32, p)
	tmp, tmpCls := make([]int32, p), make([]int32, p)
	size := p
	if size < alphabet {
		size = alphabet
	}
	cnt := make([]int32, size)
	for i := 0; i < p; i++ {
		cnt[text[i]]++
	}
	for i := 1; i < alphabet; i++ {
		cnt[i] += cnt[i-1]
	}
	for i := p - 1; i >= 0; i-- {
		cnt[text[i]]--
		order[cnt[text[i]]] = int32(i)
	}
	classes := 1
	for i := 1; i < p; i++ {
		if text[order[i]] != text[order[i-1]] {
			classes++
		}
		cls[order[i]] = int32(classes - 1)
	}
	for length := 1; length < p && classes < p; length *= 2 {
		// sorted by the second half already: shift each start back by length
		for i := 0; i < p; i++ {
			tmp[i] = int32((int(order[i]) - length + p) % p)
		}
		for i := 0; i < classes; i++ {
			cnt[i] = 0
		}
		for i := 0; i < p; i++ {
			cnt[cls[tmp[i]]]++
		}
		for i := 1; i < classes; i++ {
			cnt[i] += cnt[i-1]
		}
		for i := p - 1; i >= 0; i-- {
			cnt[cls[tmp[i]]]--
			order[cnt[cls[tmp[i]]]] = tmp[i]
		}
		tmpCls[order[0]] = 0
		classes = 1
		for i := 1; i < p; i++ {
			a, b := int(order[i]), int(order[i-1])
			if cls[a] != cls[b] || cls[(a+length)%p] != cls[(b+length)%p] {
				classes++
			}
			tmpCls[a] = int32(classes - 1)
		}
		cls, tmpCls = tmpCls, cls
	}
	// Kasai: the common prefix with the previous rotation drops by at most one per step
	total := int64(0)
	h := 0
	for i := 0; i < p; i++ {
		if cls[i] == 0 {
			h = 0
			continue
		}
		j := int(order[cls[i]-1])
		for h < p && text[(i+h)%p] == text[(j+h)%p] {
			h++
		}
		total += int64(h)
		if h > 0 {
			h--
		}
	}
	// each rotation of u appears n / p times in a row, with common prefixes of n
	total += int64(p) * int64(n/p-1) * int64(n)
	fmt.Printf("%.3f\n", float64(total)/float64(n-1))
}
