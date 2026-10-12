package main

import "fmt"

func main() {
	var limit int64
	fmt.Scan(&limit)
	// going back from the last replacement: reach is the longest run that
	// the replacements chosen so far turn into a single space
	var plan []int64
	reach := int64(1)
	for reach < limit {
		step := (reach+1)/2 + 1    // the best length to replace here
		groups := reach + 2 - step // most groups in a run that still fits
		reach = groups*step + step - 2
		plan = append(plan, step)
	}
	fmt.Println(len(plan))
	for i := len(plan) - 1; i >= 0; i-- {
		fmt.Println(plan[i])
	}
}
