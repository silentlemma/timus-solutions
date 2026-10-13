package main

import "fmt"

const fields = 3 // a given cell: its column, its row and its number

// pi and sigma of one number
type slot struct{ x, y []int }

var n int
var slots, chosen []slot
var found [][]slot
var used [][]map[[2]int]bool

func permutations(k int) [][]int {
	if k == 0 {
		return [][]int{{}}
	}
	var all [][]int
	for _, p := range permutations(k - 1) {
		for pos := 0; pos <= len(p); pos++ {
			q := append(append(append([]int{}, p[:pos]...), k-1), p[pos:]...)
			all = append(all, q)
		}
	}
	return all
}

// The square survives block swaps exactly when each number v sits in row pi_v(J) of
// every block in column J and column sigma_v(I) of every block in row I, and each pair
// (I, J) meets all positions (pi_v(J), sigma_v(I)) once; such sets are searched.
func grow(start int) {
	if len(chosen) == n*n {
		found = append(found, append([]slot{}, chosen...))
		return
	}
	for k := start; k < len(slots); k++ {
		x, y := slots[k].x, slots[k].y
		free := true
		for i := 0; i < n && free; i++ {
			for j := 0; j < n && free; j++ {
				free = !used[i][j][[2]int{x[j], y[i]}]
			}
		}
		if !free {
			continue
		}
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				used[i][j][[2]int{x[j], y[i]}] = true
			}
		}
		chosen = append(chosen, slots[k])
		grow(k + 1)
		chosen = chosen[:len(chosen)-1]
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				delete(used[i][j], [2]int{x[j], y[i]})
			}
		}
	}
}

func main() {
	var k int
	fmt.Scan(&n, &k)
	given := [][fields]int{{0, 0, 0}} // the corner holds 0
	for i := 0; i < k; i++ {
		var g [fields]int
		fmt.Scan(&g[0], &g[1], &g[2])
		given = append(given, g)
	}
	perms := permutations(n)
	for _, x := range perms {
		for _, y := range perms {
			slots = append(slots, slot{x, y})
		}
	}
	used = make([][]map[[2]int]bool, n)
	for i := range used {
		used[i] = make([]map[[2]int]bool, n)
		for j := range used[i] {
			used[i][j] = map[[2]int]bool{}
		}
	}
	grow(0)
	for _, structure := range found {
		// each given cell pins its number to the one slot that lands there
		slotOf, numberOf := map[int]int{}, map[int]int{}
		fine := true
		for _, g := range given {
			j, c, i, r, v := g[0]/n, g[0]%n, g[1]/n, g[1]%n, g[2]
			s := 0
			for structure[s].x[j] != r || structure[s].y[i] != c {
				s++
			}
			if t, ok := slotOf[v]; ok && t != s {
				fine = false
			}
			if w, ok := numberOf[s]; ok && w != v {
				fine = false
			}
			if !fine {
				break
			}
			slotOf[v], numberOf[s] = s, v
		}
		if fine {
			fmt.Println("YES")
			return
		}
	}
	fmt.Println("NO")
}
