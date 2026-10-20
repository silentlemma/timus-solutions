package main

import (
	"fmt"
	"math"
	"sort"
)

const minSumFactor int64 = 3
const quadraticFactor int64 = 4
const areaMultiple int64 = 6

func main() {
	var area int64
	fmt.Scan(&area)
	if area%areaMultiple != 0 {
		fmt.Println(0)
		return
	}
	divisors := []int64{1}
	remaining := area
	for prime := int64(2); prime*prime <= remaining; {
		exponent := 0
		for remaining%prime == 0 {
			remaining /= prime
			exponent += 2
		}
		size := len(divisors)
		power := int64(1)
		for step := 0; step < exponent; step++ {
			power *= prime
			for i := 0; i < size; i++ {
				divisors = append(divisors, divisors[i]*power)
			}
		}
		if prime == 2 {
			prime++
		} else {
			prime += 2
		}
	}
	if remaining > 1 {
		size := len(divisors)
		for i := 0; i < size; i++ {
			divisors = append(divisors, divisors[i]*remaining, divisors[i]*remaining*remaining)
		}
	}
	sort.Slice(divisors, func(i, j int) bool { return divisors[i] < divisors[j] })
	square := area * area
	answer := int64(0)
	// Heron's variables satisfy x <= y <= z and xyz(x + y + z) = area squared.
	for i, x := range divisors {
		if x > square/x/x/x/minSumFactor {
			break
		}
		remaining = square / x
		left, right := i, len(divisors)
		for left < right {
			middle := (left + right) / 2
			y := divisors[middle]
			if y <= remaining/y/(x+2*y) {
				left = middle + 1
			} else {
				right = middle
			}
		}
		for _, y := range divisors[i:left] {
			if remaining%y != 0 {
				continue
			}
			total := x + y
			discriminant := total*total + quadraticFactor*(remaining/y)
			root := int64(math.Sqrt(float64(discriminant)))
			for root*root > discriminant {
				root--
			}
			for (root+1)*(root+1) <= discriminant {
				root++
			}
			if root*root == discriminant && (root-total)%2 == 0 {
				answer++
			}
		}
	}
	fmt.Println(answer)
}
