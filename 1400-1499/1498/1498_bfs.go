package main

import "fmt"

var (
	dxs = []int{1, -1, 0, 0}
	dys = []int{0, 0, 1, -1}
)

func main() {
	var n, m, limit, x1, y1, x2, y2 int
	fmt.Scan(&n, &m, &limit, &x1, &y1, &x2, &y2)
	inside := func(x, y int) bool {
		return x >= 1 && x <= n && y >= 1 && y <= m && !(x == x2 && y == y2)
	}
	// the fewest steps from the knight to every cell, around the demon
	dist := make([][]int, n+1)
	for i := range dist {
		dist[i] = make([]int, m+1)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}
	dist[x1][y1] = 0
	queue := [][2]int{{x1, y1}}
	for h := 0; h < len(queue); h++ {
		x, y := queue[h][0], queue[h][1]
		for d := range dxs {
			nx, ny := x+dxs[d], y+dys[d]
			if inside(nx, ny) && dist[nx][ny] < 0 {
				dist[nx][ny] = dist[x][y] + 1
				queue = append(queue, [2]int{nx, ny})
			}
		}
	}
	// the strike comes from a cell next to the demon after a straight run of
	// k steps; its start must be reachable with the steps that are left
	best := 0
	for a := range dxs {
		ax, ay := x2+dxs[a], y2+dys[a]
		if !inside(ax, ay) {
			continue
		}
		for d := range dxs {
			for k := 0; ; k++ {
				sx, sy := ax-k*dxs[d], ay-k*dys[d]
				if !inside(sx, sy) {
					break
				}
				if dist[sx][sy] >= 0 && dist[sx][sy]+k <= limit && k+1 > best {
					best = k + 1
				}
			}
		}
	}
	fmt.Println(best)
}
