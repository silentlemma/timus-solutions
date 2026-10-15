package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	var n, k, x, y int
	fmt.Scan(&n, &k, &x, &y)
	// the scale shows x times all the bars plus y - x times the platinum
	// ones, so the counts must have pairwise different subset sums; the
	// Conway-Guy sets u_n - u_i do, with the smallest largest count known
	u := []int{0, 1}
	for m := 1; m < n; m++ {
		r := int(math.Round(math.Sqrt(float64(2 * m))))
		u = append(u, 2*u[m]-u[m-r])
	}
	if u[n] > k {
		fmt.Println("NO")
		return
	}
	counts := make([]string, n)
	for i := range counts {
		counts[i] = strconv.Itoa(u[n] - u[i])
	}
	fmt.Println("YES")
	fmt.Println(strings.Join(counts, " "))
}
