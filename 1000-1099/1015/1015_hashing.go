package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	faces = 6
	base  = 7
)

// quarter turns around the vertical and the left-right axes: the new face at
// position i is the old face at position turns[t][i]
var turns = [][faces]int{{3, 5, 2, 1, 4, 0}, {0, 1, 5, 2, 3, 4}}

func rotations() [][faces]int {
	all := make([][faces]int, 1)
	for i := range all[0] {
		all[0][i] = i
	}
	for k := 0; k < len(all); k++ {
		for _, turn := range turns {
			var r [faces]int
			for i := range r {
				r[i] = all[k][turn[i]]
			}
			known := false
			for _, q := range all {
				known = known || q == r
			}
			if !known {
				all = append(all, r)
			}
		}
	}
	return all
}

func main() {
	rots := rotations()
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n := next()
	// the key of a die is the smallest code among its 24 rotations
	group := map[int]int{}
	var members [][]int
	for d := 1; d <= n; d++ {
		var face [faces]int
		for i := range face {
			face[i] = next()
		}
		key := -1
		for _, r := range rots {
			code := 0
			for i := 0; i < faces; i++ {
				code = code*base + face[r[i]]
			}
			if key < 0 || code < key {
				key = code
			}
		}
		if g, ok := group[key]; ok {
			members[g] = append(members[g], d)
		} else {
			group[key] = len(members)
			members = append(members, []int{d})
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.Itoa(len(members)) + "\n")
	for _, m := range members {
		for i, d := range m {
			if i > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(d))
		}
		out.WriteByte('\n')
	}
}
