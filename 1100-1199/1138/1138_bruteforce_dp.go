package main

import "fmt"

const percent = 100

func main() {
	var n, start int
	fmt.Scan(&n, &start)
	if start > n {
		fmt.Println(0)
		return
	}
	jobs := make([]int, n+1)
	jobs[start] = 1
	answer := 1
	// Salaries increase, giving a DAG. Integer divisibility checks
	// whole percentages exactly, without floating-point arithmetic.
	for salary := start; salary <= n; salary++ {
		if jobs[salary] == 0 {
			continue
		}
		if jobs[salary] > answer {
			answer = jobs[salary]
		}
		for following := salary + 1; following <= n; following++ {
			if percent*following%salary == 0 && jobs[following] <= jobs[salary] {
				jobs[following] = jobs[salary] + 1
			}
		}
	}
	fmt.Println(answer)
}
