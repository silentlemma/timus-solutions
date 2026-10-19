package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	teamCount    = 4
	winPoints    = 3
	outcomeCount = 3
	orderCount   = 24
)

type game struct{ a, b, c, d int }
type row struct {
	coefficients []int64
	bound        int64
}

func gcd(a, b int64) int64 {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func simplify(rows []row) ([]row, bool) {
	unique := make([]row, 0, len(rows))
	for _, r := range rows {
		var divisor int64
		for _, value := range r.coefficients {
			divisor = gcd(divisor, value)
		}
		if divisor == 0 {
			if r.bound < 0 {
				return nil, false
			}
			continue
		}
		a := make([]int64, len(r.coefficients))
		for i, value := range r.coefficients {
			a[i] = value / divisor
		}
		bound := r.bound / divisor
		if r.bound%divisor < 0 {
			bound--
		}
		found := -1
		for i, u := range unique {
			equal := true
			for j, value := range a {
				if value != u.coefficients[j] {
					equal = false
					break
				}
			}
			if equal {
				found = i
				break
			}
		}
		if found < 0 {
			unique = append(unique, row{a, bound})
		} else if bound < unique[found].bound {
			unique[found].bound = bound
		}
	}
	return unique, true
}

func integerFeasible(rows []row) bool {
	rows, okay := simplify(rows)
	if !okay {
		return false
	}
	for len(rows) > 0 {
		dimension := len(rows[0].coefficients)
		column := -1
		bestCost := len(rows)*len(rows) + 1
		for i := 0; i < dimension; i++ {
			positive, negative := 0, 0
			unitUpper, unitLower := true, true
			for _, r := range rows {
				value := r.coefficients[i]
				if value > 0 {
					positive++
					unitUpper = unitUpper && value == 1
				}
				if value < 0 {
					negative++
					unitLower = unitLower && value == -1
				}
			}
			if (unitUpper || unitLower) && positive*negative < bestCost {
				column = i
				bestCost = positive * negative
			}
		}
		projected := make([]row, 0)
		for _, r := range rows {
			if r.coefficients[column] == 0 {
				a := make([]int64, 0, dimension-1)
				for i, value := range r.coefficients {
					if i != column {
						a = append(a, value)
					}
				}
				projected = append(projected, row{a, r.bound})
			}
		}
		for _, lower := range rows {
			if lower.coefficients[column] < 0 {
				for _, upper := range rows {
					if upper.coefficients[column] > 0 {
						a := make([]int64, 0, dimension-1)
						for i := 0; i < dimension; i++ {
							if i != column {
								value := upper.coefficients[column]*lower.coefficients[i] -
									lower.coefficients[column]*upper.coefficients[i]
								a = append(a, value)
							}
						}
						bound := upper.coefficients[column]*lower.bound - lower.coefficients[column]*upper.bound
						projected = append(projected, row{a, bound})
					}
				}
			}
		}
		rows, okay = simplify(projected)
		if !okay {
			return false
		}
	}
	return true
}

func nextOrder(order *[teamCount]int) bool {
	i := teamCount - 2
	for i >= 0 && order[i] >= order[i+1] {
		i--
	}
	if i < 0 {
		return false
	}
	j := teamCount - 1
	for order[j] <= order[i] {
		j--
	}
	order[i], order[j] = order[j], order[i]
	for a, b := i+1, teamCount-1; a < b; a, b = a+1, b-1 {
		order[a], order[b] = order[b], order[a]
	}
	return true
}

func possibleOrders(matches []game) [][teamCount]int {
	var initialPoints [teamCount]int
	var initialDifference [teamCount]int64
	var played [teamCount][teamCount]bool
	for _, m := range matches {
		played[m.a][m.b] = true
		initialDifference[m.a] += int64(m.c - m.d)
		initialDifference[m.b] += int64(m.d - m.c)
		if m.c == m.d {
			initialPoints[m.a]++
			initialPoints[m.b]++
		} else if m.c > m.d {
			initialPoints[m.a] += winPoints
		} else {
			initialPoints[m.b] += winPoints
		}
	}
	remaining := make([][2]int, 0)
	for a := 0; a < teamCount; a++ {
		for b := a + 1; b < teamCount; b++ {
			if !played[a][b] {
				remaining = append(remaining, [2]int{a, b})
			}
		}
	}
	orders := make([][teamCount]int, 0, orderCount)
	var order [teamCount]int
	for i := range order {
		order[i] = i
	}
	for {
		orders = append(orders, order)
		if !nextOrder(&order) {
			break
		}
	}
	var found [orderCount]bool
	foundCount, patternCount := 0, 1
	for range remaining {
		patternCount *= outcomeCount
	}
	for pattern := 0; pattern < patternCount && foundCount < orderCount; pattern++ {
		code := pattern
		points, difference := initialPoints, initialDifference
		edges := make([][2]int, 0)
		for _, pair := range remaining {
			outcome := code % outcomeCount
			code /= outcomeCount
			if outcome == 0 {
				points[pair[0]]++
				points[pair[1]]++
			} else {
				winner, loser := pair[0], pair[1]
				if outcome != 1 {
					winner, loser = loser, winner
				}
				points[winner] += winPoints
				difference[winner]++
				difference[loser]--
				edges = append(edges, [2]int{winner, loser})
			}
		}
		for index, o := range orders {
			if found[index] {
				continue
			}
			compatible := true
			for i := 0; i+1 < teamCount; i++ {
				if points[o[i]] < points[o[i+1]] {
					compatible = false
				}
			}
			if !compatible {
				continue
			}
			rows := make([]row, 0)
			for column := range edges {
				a := make([]int64, len(edges))
				a[column] = -1
				rows = append(rows, row{a, 0})
			}
			for i := 0; i+1 < teamCount; i++ {
				a, b := o[i], o[i+1]
				if points[a] != points[b] {
					continue
				}
				coefficients := make([]int64, len(edges))
				for j, edge := range edges {
					if edge[0] == b {
						coefficients[j]++
					}
					if edge[1] == b {
						coefficients[j]--
					}
					if edge[0] == a {
						coefficients[j]--
					}
					if edge[1] == a {
						coefficients[j]++
					}
				}
				rows = append(rows, row{coefficients, difference[a] - difference[b]})
			}
			if integerFeasible(rows) {
				found[index] = true
				foundCount++
			}
		}
	}
	result := make([][teamCount]int, 0, foundCount)
	for i, o := range orders {
		if found[i] {
			result = append(result, o)
		}
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	matches := make([]game, n)
	for i := range matches {
		m := &matches[i]
		fmt.Fscan(in, &m.a, &m.b, &m.c, &m.d)
		m.a--
		m.b--
	}
	orders := possibleOrders(matches)
	fmt.Fprintln(out, len(orders))
	for _, o := range orders {
		for i, v := range o {
			if i > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, v+1)
		}
		fmt.Fprintln(out)
	}
}
