package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type debt struct {
	creditor, debtor int
	amount           int64
}

// mostResponsible is a maximum matching of banks to debts of their own
// country: a bank keeps a debt it already holds or buys one it can afford
func mostResponsible(banks []int, debts []debt, money []int64) int {
	sort.SliceStable(debts, func(a, b int) bool { return debts[a].amount < debts[b].amount })
	nd := len(debts)
	own := map[int][]int{}
	for _, b := range banks {
		own[b] = nil
	}
	for j, d := range debts {
		if _, ok := own[d.creditor]; ok {
			own[d.creditor] = append(own[d.creditor], j)
		}
	}
	reach := map[int]int{} // the affordable prefix
	for _, b := range banks {
		reach[b] = sort.Search(nd, func(j int) bool { return debts[j].amount > money[b] })
	}
	holder, seen, skip := make([]int, nd), make([]bool, nd), make([]int, nd+1)
	reset := func() {
		for j := range seen {
			seen[j] = false
		}
		for j := range skip {
			skip[j] = j
		}
	}
	for j := range holder {
		holder[j] = -1
	}
	reset()
	unseen := func(j int) int {
		root := j
		for skip[root] != root {
			root = skip[root]
		}
		for skip[j] != root {
			skip[j], j = root, skip[j]
		}
		return root
	}
	var augment func(b int) bool
	try := func(j, b int) bool {
		seen[j], skip[j] = true, j+1
		if holder[j] < 0 || augment(holder[j]) {
			holder[j] = b
			return true
		}
		return false
	}
	augment = func(b int) bool {
		for _, j := range own[b] {
			if !seen[j] && try(j, b) {
				return true
			}
		}
		for j := unseen(0); j < reach[b]; j = unseen(j + 1) {
			if debts[j].debtor != b && try(j, b) { // a bank cannot hold its own debt
				return true
			}
		}
		return false
	}
	order := append([]int(nil), banks...)
	// banks that hold a debt already go first, then the poorer ones
	sort.SliceStable(order, func(x, y int) bool {
		a, b := order[x], order[y]
		if (len(own[a]) > 0) != (len(own[b]) > 0) {
			return len(own[a]) > 0
		}
		return reach[a] < reach[b]
	})
	count := 0
	for _, b := range order {
		// marks are cleared only after a success: when a search fails the
		// matching stays as it was, so the debts it saw still lead nowhere
		if augment(b) {
			count++
			reset()
		}
	}
	return count
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	country, money := make([]int, n), make([]int64, n)
	banks := map[int][]int{}
	for b := 0; b < n; b++ {
		fmt.Fscan(in, &country[b], &money[b])
		banks[country[b]] = append(banks[country[b]], b)
	}
	var m int
	fmt.Fscan(in, &m)
	byCountry := map[int][]debt{}
	for i := 0; i < m; i++ {
		var d debt
		fmt.Fscan(in, &d.creditor, &d.debtor, &d.amount)
		d.creditor--
		d.debtor--
		byCountry[country[d.debtor]] = append(byCountry[country[d.debtor]], d)
	}
	total := 0
	for c, group := range banks {
		total += mostResponsible(group, byCountry[c], money)
	}
	fmt.Println(total)
}
