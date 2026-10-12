package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	a, b := next(), next()
	f := make([]int, b-a+1)
	for i := range f {
		f[i] = next()
	}
	pieces, n := 0, len(f)
	for i := 0; i < n; {
		// stretch this piece while it stays monotone; its way up or down is
		// fixed by its first step that is not flat
		pieces++
		way, j := 0, i
		for ; j+1 < n; j++ {
			step := 0
			if f[j+1] > f[j] {
				step = 1
			} else if f[j+1] < f[j] {
				step = -1
			}
			if step != 0 && way != 0 && step != way {
				break
			}
			if way == 0 {
				way = step
			}
		}
		i = j + 1
	}
	fmt.Println(pieces)
}
