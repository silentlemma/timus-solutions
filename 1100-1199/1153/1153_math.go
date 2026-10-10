package main

import (
	"fmt"
	"math/big"
)

// eight: 8 S + 1 = (2 N + 1)^2 for S = N (N + 1) / 2
const eight = 8

func main() {
	var text string
	fmt.Scan(&text)
	total, _ := new(big.Int).SetString(text, 10)
	d := new(big.Int).Mul(total, big.NewInt(eight))
	d.Add(d, big.NewInt(1))
	root := new(big.Int).Sqrt(d)
	root.Sub(root, big.NewInt(1))
	root.Rsh(root, 1)
	fmt.Println(root.String())
}
