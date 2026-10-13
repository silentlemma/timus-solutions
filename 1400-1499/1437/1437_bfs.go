package main

import "fmt"

const cans = 3

func main() {
	var cap, sz [cans]int
	for i := range cap {
		fmt.Scan(&cap[i])
		sz[i] = cap[i] + 1
	}
	code := func(v [cans]int) int { return (v[0]*sz[1]+v[1])*sz[2] + v[2] }
	// a state (x, y, z) as one number; every move leaves some can empty or full
	seen := make([]bool, sz[0]*sz[1]*sz[2])
	seen[0] = true
	queue := [][cans]int{{}}
	volumes := map[int]bool{}
	for head := 0; head < len(queue); head++ {
		v := queue[head]
		for mask := 1; mask < 1<<cans; mask++ {
			sum := 0
			for i := 0; i < cans; i++ {
				if mask>>i&1 == 1 {
					sum += v[i]
				}
			}
			volumes[sum] = true
		}
		for i := 0; i < cans; i++ {
			for j := -1; j < cans; j++ {
				w := v
				if j < 0 { // fill can i from the pump up to the brim
					w[i] = cap[i]
				} else if i != j { // pour i into j
					move := v[i]
					if cap[j]-v[j] < move {
						move = cap[j] - v[j]
					}
					w[i] -= move
					w[j] += move
				}
				if k := code(w); !seen[k] {
					seen[k] = true
					queue = append(queue, w)
				}
			}
		}
	}
	delete(volumes, 0)
	fmt.Println(len(volumes))
}
