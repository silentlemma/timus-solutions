package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	n      int
	xs, ys []int64
)

// segment returns the segment of f that holds x, or the one to its right
func segment(x int64) int {
	j := sort.Search(n, func(i int) bool { return xs[i] > x }) - 1
	if j > n-2 {
		j = n - 2
	}
	return j
}

func value(x int64) float64 {
	j := segment(x)
	return float64(ys[j]) + float64(ys[j+1]-ys[j])*float64(x-xs[j])/float64(xs[j+1]-xs[j])
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fscan(reader, &n)
	xs, ys = make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &xs[i], &ys[i])
	}

	// f(x) = E(x) + O(x) with E(x) = (f(x) + f(-x)) / 2 and
	// O(x) = (f(x) - f(-x)) / 2; both are linear between the points of f
	// and their mirror images
	seen := map[int64]bool{}
	var points []int64
	for _, x := range xs {
		for _, p := range []int64{x, -x} {
			if !seen[p] {
				seen[p] = true
				points = append(points, p)
			}
		}
	}
	sort.Slice(points, func(a, b int) bool { return points[a] < points[b] })

	fmt.Fprintln(writer, "Yes")
	for _, sign := range []int64{1, -1} { // the even part, then the odd one
		// the slope of a part between neighbouring points: (a/b -+ c/d) / 2 with
		// the slopes a/b of f at x and c/d of f at -x, all below 2 * 10^9
		num := make([]int64, len(points)-1)
		den := make([]int64, len(points)-1)
		for k := 0; k+1 < len(points); k++ {
			j, i := segment(points[k]), segment(-points[k+1])
			a, b := ys[j+1]-ys[j], xs[j+1]-xs[j]
			c, d := ys[i+1]-ys[i], xs[i+1]-xs[i]
			num[k], den[k] = a*d-sign*c*b, 2*b*d
		}
		for k, x := range points {
			bend := k == 0 || k+1 == len(points) || num[k-1]*den[k] != num[k]*den[k-1]
			if bend { // only real bends stay
				fmt.Fprintf(writer, "%.6f %.6f\n", float64(x), (value(x)+float64(sign)*value(-x))/2)
			}
		}
	}
}
