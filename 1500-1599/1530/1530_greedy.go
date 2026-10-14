package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var p, q string
	fmt.Fscan(in, &n, &p, &q)
	// A xor B equals A + B exactly when no position holds two ones. With a
	// equal to p, b follows q up to a 0 that becomes 1, then zeros, and that
	// prefix of q must avoid the ones of p, so it ends before the first clash
	clash := 0
	for clash < n && !(p[clash] == '1' && q[clash] == '1') {
		clash++
	}
	for j := clash - 1; j >= 0; j-- {
		if p[j] == '0' && q[j] == '0' {
			fmt.Println(p)
			fmt.Println(q[:j] + "1" + strings.Repeat("0", n-j-1))
			return
		}
	}
	// otherwise the next a after p with b all zeros, or start over
	a := strings.Repeat("0", n)
	if last := strings.LastIndexByte(p, '0'); last >= 0 {
		a = p[:last] + "1" + strings.Repeat("0", n-last-1)
	}
	fmt.Println(a)
	fmt.Println(strings.Repeat("0", n))
}
