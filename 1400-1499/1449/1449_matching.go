package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	// the Hungarian method minimises the cost -A; rows and columns from 1, 0 is a helper
	cost := make([][]int64, n+1)
	cost[0] = make([]int64, n+1)
	for i := 1; i <= n; i++ {
		cost[i] = make([]int64, n+1)
		for j := 1; j <= n; j++ {
			fmt.Fscan(reader, &cost[i][j])
			cost[i][j] = -cost[i][j]
		}
	}
	u, v := make([]int64, n+1), make([]int64, n+1)
	match, way := make([]int, n+1), make([]int, n+1) // match[j]: the row matched to column j
	for i := 1; i <= n; i++ {
		match[0] = i
		j0 := 0
		low := make([]int64, n+1)
		for j := range low {
			low[j] = math.MaxInt64
		}
		used := make([]bool, n+1)
		for match[j0] != 0 {
			used[j0] = true
			i0, j1 := match[j0], 0
			delta := int64(math.MaxInt64)
			for j := 1; j <= n; j++ {
				if !used[j] {
					if cur := cost[i0][j] - u[i0] - v[j]; cur < low[j] {
						low[j], way[j] = cur, j0
					}
					if low[j] < delta {
						delta, j1 = low[j], j
					}
				}
			}
			for j := 0; j <= n; j++ {
				if used[j] {
					u[match[j]] += delta
					v[j] -= delta
				} else {
					low[j] -= delta
				}
			}
			j0 = j1
		}
		for j0 != 0 {
			j1 := way[j0]
			match[j0] = match[j1]
			j0 = j1
		}
	}
	// u + v <= -A, so the bribes -u, -v cover every credit and add up to the
	// heaviest matching; shifting them until a row bribe is 0 keeps all >= 0
	shift := int64(math.MaxInt64)
	for i := 1; i <= n; i++ {
		if -u[i] < shift {
			shift = -u[i]
		}
	}
	rows, cols := make([]string, n), make([]string, n)
	for i := 1; i <= n; i++ {
		rows[i-1] = strconv.FormatInt(-u[i]-shift, 10)
		cols[i-1] = strconv.FormatInt(-v[i]+shift, 10)
	}
	fmt.Println(strings.Join(rows, " "))
	fmt.Println(strings.Join(cols, " "))
}
