package main

import (
	"bufio"
	"fmt"
	"os"
)

const padding = 3
const modulus int64 = 1000000007

func main() {
	input := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(input, &n)
	edges := n - 1
	length := 2 * edges
	inverse := make([]int64, length+2)
	choose := make([]int64, length+padding)
	inverse[1] = 1
	choose[0] = 1
	for i := 1; i <= length; i++ {
		value := int64(i)
		if i > 1 {
			inverse[i] = modulus - (modulus/value)*inverse[modulus%value]%modulus
		}
		choose[i] = choose[i-1] * int64(length-i+1) % modulus * inverse[i] % modulus
	}

	// Contour walks are Dyck paths. Sum the counts whose maximum is at least h.
	// Reflection at levels -1 and h gives this second difference, with width h + 1.
	var answer int64
	for width := 2; width <= edges+1; width++ {
		for offset := width; offset <= edges+1; offset += width {
			index := edges + offset
			answer += choose[index-1] - 2*choose[index] + choose[index+1]
		}
	}
	fmt.Println((answer%modulus + modulus) % modulus)
}
