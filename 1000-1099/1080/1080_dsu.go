package main

import "os"

const maxCountries = 98
const bufferSize = 4096

var input [bufferSize]byte
var position, available int
var parent, sizes, parity [maxCountries]byte

func readByte() byte {
	if position == available {
		available, _ = os.Stdin.Read(input[:])
		position = 0
		if available == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func nextInt() int {
	c := readByte()
	for c <= ' ' {
		c = readByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = readByte()
	}
	return value
}

func find(v byte) byte {
	if parent[v] != v {
		old := parent[v]
		parent[v] = find(old)
		parity[v] ^= parity[old]
	}
	return parent[v]
}

func main() {
	n := nextInt()
	// N<=98: indices, component sizes and XOR parities all fit one byte.
	for v := 0; v < n; v++ {
		parent[v] = byte(v)
		sizes[v] = 1
	}
	for a := 0; a < n; a++ {
		for raw := nextInt(); raw != 0; raw = nextInt() {
			x, y := byte(a), byte(raw-1)
			ra, rb := find(x), find(y)
			if ra == rb {
				if parity[x] == parity[y] {
					os.Stdout.WriteString("-1\n")
					return
				}
			} else {
				if sizes[ra] < sizes[rb] {
					ra, rb = rb, ra
				}
				parent[rb] = ra
				// New edge requires opposite colors; the formula is symmetric.
				parity[rb] = parity[x] ^ parity[y] ^ 1
				sizes[ra] += sizes[rb]
			}
		}
	}
	find(0)
	first := parity[0]
	var answer [maxCountries]byte
	for v := 0; v < n; v++ {
		find(byte(v))
		answer[v] = '0' + (parity[v] ^ first)
	}
	os.Stdout.Write(answer[:n])
	os.Stdout.WriteString("\n")
}
