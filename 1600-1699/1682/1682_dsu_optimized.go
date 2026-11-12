package main

import (
	"bufio"
	"os"
	"strconv"
)

const cycleMultiple = 3
const decimalBase = 10

func find(parent []int32, v uint32) uint32 {
	root := v
	for parent[root] >= 0 {
		root = uint32(parent[root])
	}
	for v != root {
		next := uint32(parent[v])
		parent[v] = int32(root)
		v = next
	}
	return root
}

func join(parent []int32, a, b uint32) bool {
	a = find(parent, a)
	b = find(parent, b)
	if a == b {
		return false
	}
	if parent[a] > parent[b] {
		a, b = b, a
	}
	parent[a] += parent[b]
	parent[b] = int32(a)
	return true
}

func solve(k int) int {
	square, rootHead := make([]uint32, k), make([]uint32, k)
	rootNext, writtenHead := make([]uint32, k), make([]uint32, k)
	for s := 0; s < k; s++ {
		remainder := uint32(uint64(s) * uint64(s) % uint64(k))
		if remainder != 0 {
			square[s] = uint32(k) - remainder
		}
		rootNext[s] = rootHead[square[s]]
		rootHead[square[s]] = uint32(s + 1)
	}
	parent := []int32{0}
	writtenNext := []uint32{0}
	for a := 1; a <= cycleMultiple*k; a++ {
		parent = append(parent, -1)
		residue := a % k
		connect := func(s uint32) bool {
			for b := writtenHead[s]; b != 0; b = writtenNext[b] {
				if !join(parent, uint32(a), b) {
					return false
				}
			}
			return true
		}
		if !connect(square[residue]) {
			return a
		}
		for node := rootHead[residue]; node != 0; node = rootNext[node-1] {
			s := node - 1
			if s != square[residue] && !connect(s) {
				return a
			}
		}
		writtenNext = append(writtenNext, writtenHead[residue])
		writtenHead[residue] = uint32(a)
	}
	return -1
}

func main() {
	in := bufio.NewReader(os.Stdin)
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	k := 0
	for c >= '0' && c <= '9' {
		k = k*decimalBase + int(c-'0')
		c, _ = in.ReadByte()
	}
	os.Stdout.WriteString(strconv.Itoa(solve(k)) + "\n")
}
