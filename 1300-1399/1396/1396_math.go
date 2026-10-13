package main

import (
	"bufio"
	"os"
	"strconv"
)

const bits = 61   // every n is below 2^60, and a lowered bit leaves at most 60 free ones
const endings = 4 // per first bit: as is, last bit 1, last two 11, last two 01

// step: (a_m, a_m+1) -> (a_2m+bit, a_2m+bit+1)
func step(x, y int64, bit int) (int64, int64) {
	if bit == 0 {
		return x, x + y
	}
	return x + y, y
}

func main() {
	// maps[r]: (p, q) with a = p a_m + q a_m+1 after each candidate suffix of
	// r free bits: alternating bits with the last one or two changed
	maps := make([][][2]int64, bits)
	for r := 0; r < bits; r++ {
		for first := 0; first < 2; first++ {
			for e := 0; e < endings; e++ {
				pattern := make([]int, r)
				for k := range pattern {
					pattern[k] = (first + k) % 2
				}
				if e == 1 && r >= 1 {
					pattern[r-1] = 1
				}
				if e >= 2 && r >= 2 {
					pattern[r-2] = 0
					if e == 2 {
						pattern[r-2] = 1
					}
					pattern[r-1] = 1
				}
				px, py, qx, qy := int64(1), int64(0), int64(0), int64(1)
				for _, b := range pattern {
					px, py = step(px, py, b)
					qx, qy = step(qx, qy, b)
				}
				maps[r] = append(maps[r], [2]int64{px, qx})
			}
		}
	}
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for sc.Scan() {
		v, _ := strconv.Atoi(sc.Text()) // int has 64 bits on the judge
		n := int64(v)
		if n == 0 {
			break
		}
		length := 0
		for length < bits && n>>uint(length) > 0 {
			length++
		}
		best := int64(0)
		x, y := int64(0), int64(1) // (a_0, a_1) for the empty prefix
		for k := length - 1; k >= 0; k-- {
			bit := int(n >> uint(k) & 1)
			if bit == 1 {
				// lower this bit to 0: the k bits below are free
				lx, ly := step(x, y, 0)
				for _, pq := range maps[k] {
					if v := pq[0]*lx + pq[1]*ly; v > best {
						best = v
					}
				}
			}
			x, y = step(x, y, bit)
		}
		if x > best {
			best = x
		}
		out.WriteString(strconv.FormatInt(best, 10) + "\n")
	}
}
