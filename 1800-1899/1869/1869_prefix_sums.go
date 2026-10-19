package main

import (
	"bufio"
	"fmt"
	"os"
)

const seats = 36

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	// change[k] is how many people get on at station k minus how many get
	// off there; the eastbound and westbound trains are counted apart
	east, west := make([]int64, n+1), make([]int64, n+1)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			var a int64
			fmt.Fscan(reader, &a)
			if i < j {
				east[i] += a
				east[j] -= a
			} else if i > j {
				west[j] += a
				west[i] -= a
			}
		}
	}
	var best, loadE, loadW int64
	for k := 0; k < n; k++ {
		loadE += east[k]
		loadW += west[k]
		if loadE > best {
			best = loadE
		}
		if loadW > best {
			best = loadW
		}
	}
	fmt.Println((best + seats - 1) / seats)
}
