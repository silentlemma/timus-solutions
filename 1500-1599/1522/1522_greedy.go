package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	// int has 64 bits on the judge, enough for the total time
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n := next()
	a, b, c := make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		a[i], b[i], c[i] = next(), next(), next()
	}
	// machine B never holds the line, so the line behaves like two machines
	// with times a + b and b + c, where Johnson's rule is optimal: toys
	// faster on the first come first, by its time, the rest by the second
	var early, late []int
	for i := 0; i < n; i++ {
		if a[i]+b[i] < b[i]+c[i] {
			early = append(early, i)
		} else {
			late = append(late, i)
		}
	}
	sort.Slice(early, func(x, y int) bool { return a[early[x]]+b[early[x]] < a[early[y]]+b[early[y]] })
	sort.Slice(late, func(x, y int) bool { return b[late[x]]+c[late[x]] > b[late[y]]+c[late[y]] })
	order := append(early, late...)
	var doneA, doneB, doneC int
	for _, i := range order {
		doneA += a[i]
		if doneA > doneB {
			doneB = doneA
		}
		doneB += b[i]
		if doneB > doneC {
			doneC = doneB
		}
		doneC += c[i]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.Itoa(doneC) + "\n")
	for k, i := range order {
		out.WriteString(strconv.Itoa(i + 1))
		if k+1 < n {
			out.WriteByte(' ')
		}
	}
	out.WriteByte('\n')
}
