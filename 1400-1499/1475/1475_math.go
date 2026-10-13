package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const speed = 4 // bounces k come at 4 h sin(a) k (k + 1) down the slope

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var t int
	fmt.Fscan(reader, &t)
	one := big.NewInt(1)
	for ; t > 0; t-- {
		var hs, ls string
		var drop int64
		fmt.Fscan(reader, &hs, &ls, &drop)
		height, _ := new(big.Int).SetString(hs, 10)
		run, _ := new(big.Int).SetString(ls, 10)
		// the largest k with speed * drop * height * k (k + 1) <= run^2 + height^2
		x := new(big.Int).Mul(run, run)
		x.Add(x, new(big.Int).Mul(height, height))
		y := new(big.Int).Mul(height, big.NewInt(speed*drop))
		q := x.Quo(x, y)
		q.Lsh(q, 2).Add(q, one) // 4q + 1
		k := q.Sqrt(q)
		k.Sub(k, one).Rsh(k, 1)
		fmt.Fprintln(writer, k.Add(k, one).String())
	}
}
