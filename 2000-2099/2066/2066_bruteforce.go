package main

import "fmt"

func apply(x int, op byte, y int) int {
	switch op {
	case '*':
		return x * y
	case '+':
		return x + y
	}
	return x - y
}

// x op1 y op2 z, multiplication first
func evaluate(x int, op1 byte, y int, op2 byte, z int) int {
	if op2 == '*' && op1 != '*' {
		return apply(x, op1, y*z)
	}
	return apply(apply(x, op1, y), op2, z)
}

const count = 3

func main() {
	var v [count]int
	fmt.Scan(&v[0], &v[1], &v[2])
	ops := "+-*"
	orders := [][count]int{{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}}
	best := v[0] + v[1] + v[2]
	for _, o := range orders {
		for i := 0; i < len(ops); i++ {
			for j := 0; j < len(ops); j++ {
				r := evaluate(v[o[0]], ops[i], v[o[1]], ops[j], v[o[2]])
				if r < best {
					best = r
				}
			}
		}
	}
	fmt.Println(best)
}
