package main

import (
	"bufio"
	"fmt"
	"os"
)

// many caps the counts: two ways already make the answer ambiguous
const many = 2

// fits tells whether digit c of the paper may be bit b
func fits(c byte, b int) bool {
	return c == '?' || int(c-'0') == b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var k, x string
	if _, err := fmt.Fscan(reader, &k, &x); err != nil {
		return
	}
	n := len(k)
	// the Gray code of k has digit x(i) = k(i) xor k(i - 1), with a 0
	// before the first digit; ways[b][i] counts the readings of the first
	// i + 1 digits that end with k(i) = b
	ways := [2][]int{make([]int, n), make([]int, n)}
	w := [2]int{1, 0}
	for i := 0; i < n; i++ {
		var next [2]int
		for cur := 0; cur < 2; cur++ {
			if !fits(k[i], cur) {
				continue
			}
			for prev := 0; prev < 2; prev++ {
				if fits(x[i], prev^cur) {
					next[cur] += w[prev]
					if next[cur] > many {
						next[cur] = many
					}
				}
			}
		}
		w = next
		ways[0][i], ways[1][i] = w[0], w[1]
	}
	if w[0]+w[1] == 0 {
		fmt.Println("Impossible")
		return
	}
	if w[0]+w[1] > 1 {
		fmt.Println("Ambiguity")
		return
	}
	// walk back along the single reading: exactly one earlier digit of k
	// with a reading of its own leads on to the next one
	bits := make([]byte, n)
	code := make([]byte, n)
	cur := 0
	if w[1] > 0 {
		cur = 1
	}
	bits[n-1] = byte('0' + cur)
	for i := n - 1; i > 0; i-- {
		for prev := 0; prev < 2; prev++ {
			if ways[prev][i-1] > 0 && fits(x[i], prev^cur) {
				bits[i-1] = byte('0' + prev)
				code[i] = byte('0' + (prev ^ cur))
			}
		}
		cur = int(bits[i-1] - '0')
	}
	code[0] = bits[0]
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	writer.Write(bits)
	writer.WriteByte('\n')
	writer.Write(code)
	writer.WriteByte('\n')
}
