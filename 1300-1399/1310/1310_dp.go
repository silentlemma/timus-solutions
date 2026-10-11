package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var length, top, k int
	var code string
	fmt.Fscan(in, &length, &top, &k, &code)
	n, _ := new(big.Int).SetString(code, 10)
	// ways[i][r]: how many ways i registers can hold values 1..M with a sum
	// that leaves remainder r modulo K
	ways := make([][]*big.Int, length+1)
	for i := range ways {
		ways[i] = make([]*big.Int, k)
		for r := range ways[i] {
			ways[i][r] = new(big.Int)
		}
	}
	ways[0][0].SetInt64(1)
	for i := 1; i <= length; i++ {
		for v := 1; v <= top; v++ {
			for r := 0; r < k; r++ {
				t := ways[i][(r+v)%k]
				t.Add(t, ways[i-1][r])
			}
		}
	}
	out := make([]string, 0, length)
	total := 0
	for pos := 0; pos < length; pos++ {
		left := length - pos - 1
		// try the values in increasing order and skip whole blocks of states
		for v := 1; v <= top; v++ {
			block := ways[left][((-(total+v))%k+k)%k]
			if n.Cmp(block) < 0 {
				out = append(out, strconv.Itoa(v))
				total += v
				break
			}
			n.Sub(n, block)
		}
	}
	fmt.Println(strings.Join(out, " "))
}
