package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

// character classes, ordered: the end, other characters, dot, at, letters
const (
	other    = 1
	dot      = 2
	at       = 3
	letter   = 4
	alphabet = letter + 26
)

// cyclic prefix doubling with counting sort; code ends with a 0
func suffixArray(code []byte) ([]int32, []int32) {
	n := len(code)
	size := n
	if size < alphabet {
		size = alphabet
	}
	count := make([]int32, size)
	order := make([]int32, n)
	cls := make([]int32, n)
	shifted := make([]int32, n)
	fresh := make([]int32, n)
	for _, c := range code {
		count[c]++
	}
	for i := 1; i < alphabet; i++ {
		count[i] += count[i-1]
	}
	for i := n - 1; i >= 0; i-- {
		count[code[i]]--
		order[count[code[i]]] = int32(i)
	}
	classes := int32(1)
	for i := 1; i < n; i++ {
		if code[order[i]] != code[order[i-1]] {
			classes++
		}
		cls[order[i]] = classes - 1
	}
	for shift := 1; shift < n && int(classes) < n; shift *= 2 {
		for i := 0; i < n; i++ {
			p := int(order[i]) - shift
			if p < 0 {
				p += n
			}
			shifted[i] = int32(p)
		}
		for i := int32(0); i < classes; i++ {
			count[i] = 0
		}
		for _, p := range shifted {
			count[cls[p]]++
		}
		for i := int32(1); i < classes; i++ {
			count[i] += count[i-1]
		}
		for i := n - 1; i >= 0; i-- {
			p := shifted[i]
			count[cls[p]]--
			order[count[cls[p]]] = p
		}
		fresh[order[0]] = 0
		classes = 1
		for i := 1; i < n; i++ {
			cur, prev := int(order[i]), int(order[i-1])
			curNext, prevNext := (cur+shift)%n, (prev+shift)%n
			if cls[cur] != cls[prev] || cls[curNext] != cls[prevNext] {
				classes++
			}
			fresh[cur] = classes - 1
		}
		cls, fresh = fresh, cls
	}
	return order, cls
}

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	n := len(text)
	code := make([]byte, n+1)
	letters := make([]int32, n+1)
	for i, ch := range text {
		switch {
		case ch >= 'a' && ch <= 'z':
			code[i] = letter + ch - 'a'
			letters[i+1] = letters[i] + 1
			continue
		case ch == '.':
			code[i] = dot
		case ch == '@':
			code[i] = at
		default:
			code[i] = other
		}
		letters[i+1] = letters[i]
	}
	// around an at sign, users start no earlier than just past the last other
	// character, at or double dot, and domains end no later than just before
	// the next of them
	firstStart := make([]int32, n)
	lastEnd := make([]int32, n)
	nextAt := make([]int32, n)
	barrier, twin := -1, -1
	for i := 0; i < n; i++ {
		if code[i] == at {
			firstStart[i] = int32(max(barrier, twin) + 1)
		}
		if code[i] == dot && i > 0 && code[i-1] == dot {
			twin = i
		}
		if code[i] == other || code[i] == at {
			barrier = i
		}
	}
	barrier, twin = n, n
	upcoming := -1
	for i := n - 1; i >= 0; i-- {
		if code[i] == at {
			lastEnd[i] = int32(min(barrier, twin) - 1)
		}
		if code[i] == other {
			upcoming = -1
		}
		nextAt[i] = int32(upcoming)
		if code[i] == dot && code[i+1] == dot {
			twin = i + 1
		}
		if code[i] == other || code[i] == at {
			barrier = i
		}
		if code[i] == at {
			upcoming = i
		}
	}
	order, rank := suffixArray(code)
	// being an address is a property of the string alone, so every address
	// is counted once, at the first suffix in sorted order that starts with
	// it: only prefixes longer than the common part with the suffix before
	var total int64
	common := 0
	for start := 0; start < n; start++ {
		prev := int(order[rank[start]-1])
		for code[start+common] != 0 && code[start+common] == code[prev+common] {
			common++
		}
		lcp := common
		if common > 0 {
			common--
		}
		if code[start] < letter {
			continue
		}
		a := int(nextAt[start])
		if a < 0 || start < int(firstStart[a]) || code[a-1] < letter {
			continue
		}
		end := int(lastEnd[a])
		if a+1 > end || code[a+1] < letter {
			continue
		}
		lo := max(start+lcp, a+1)
		if lo <= end {
			total += int64(letters[end+1] - letters[lo])
		}
	}
	fmt.Println(total)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
