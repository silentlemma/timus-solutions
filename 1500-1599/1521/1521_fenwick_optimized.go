package main

import (
	"bufio"
	"os"
	"strconv"
)

// parsing digits directly avoids formatted input and per-token allocations.
func readInt(in *bufio.Reader) int {
	value := 0
	c, err := in.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.ReadByte()
	}
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	n, k := readInt(in), readInt(in)
	// a fenwick tree over the circle: 1 for a soldier still marching
	// initially every interval is full, so its count is lowbit(i) <= n <= 100000.
	tree := make([]int32, n+1)
	for i := 1; i <= n; i++ {
		tree[i] = int32(i & -i)
	}
	top := 1
	for top*2 <= n {
		top *= 2
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// n <= 100000 needs at most six decimal digits; this scratch space is reused.
	const maxDigits = 10
	var digits [maxDigits]byte
	for rank, left := 0, n; left > 0; left-- {
		// the soldier k places ahead, counting among those still marching
		rank = (rank + k - 1) % left
		// descend to the (rank + 1)-th remaining soldier
		pos, need := 0, rank+1
		for step := top; step > 0; step /= 2 {
			next := pos + step
			if next <= n {
				if int(tree[next]) < need {
					need -= int(tree[next])
					pos = next
				} else {
					// this fenwick interval contains the soldier being removed.
					tree[next]--
				}
			}
		}
		out.Write(strconv.AppendInt(digits[:0], int64(pos+1), 10))
		if left > 1 {
			out.WriteByte(' ')
		} else {
			out.WriteByte('\n')
		}
	}
}
