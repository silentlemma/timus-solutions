package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var text, name string
	fmt.Fscan(in, &text, &name)
	n, m := len(text), len(name)
	// the name can be written from position j on when each of its letters
	// lands on that letter or on a "?"
	fits := make([]bool, n-m+1)
	for j := range fits {
		fits[j] = true
		for i := 0; i < m && fits[j]; i++ {
			if text[j+i] != '?' && text[j+i] != name[i] {
				fits[j] = false
			}
		}
	}
	// two copies d < m apart agree exactly when d is a period of the name:
	// copies far apart never meet, and a set of copies agrees as soon as
	// each copy agrees with the next one, which covers what lies between
	border := make([]int, m)
	for i, k := 1, 0; i < m; i++ {
		for k > 0 && name[k] != name[i] {
			k = border[k-1]
		}
		if name[k] == name[i] {
			k++
		}
		border[i] = k
	}
	var periods []int
	for k := border[m-1]; k > 0; k = border[k-1] {
		periods = append(periods, m-k)
	}
	// best[j]: the most copies with the last one at j; before[j]: the most
	// with the last one before j
	best, before := make([]int, n-m+1), make([]int, n-m+2)
	for j := 0; j+m <= n; j++ {
		if fits[j] {
			previous := 0
			if j >= m {
				previous = before[j-m+1]
			}
			for _, d := range periods {
				if d <= j && best[j-d] > previous {
					previous = best[j-d]
				}
			}
			best[j] = previous + 1
		}
		before[j+1] = before[j]
		if best[j] > before[j+1] {
			before[j+1] = best[j]
		}
	}
	fmt.Println(before[n-m+1])
}
