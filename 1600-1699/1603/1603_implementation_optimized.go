package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const side = 4
const cells = side * side
const letters = 26
const colorCount = 2
const stateBits = cells - 1
const byteBits = 8
const memoBytes = cells * (1 << stateBits) / byteBits

var positions [letters]uint32
var colors [colorCount]uint32
var near, allowed [cells]uint32
var capacity [colorCount][letters]int
var failed [memoBytes]byte
var word []byte

func walk(cell int, used uint32, index int) bool {
	if index+1 == len(word) {
		return true
	}
	compressed := (used & ((uint32(1) << uint(cell)) - 1)) | ((used >> uint(cell+1)) << uint(cell))
	key := (uint32(cell) << stateBits) | compressed
	flag := byte(1 << (key % byteBits))
	slot := key / byteBits
	if failed[slot]&flag != 0 {
		return false
	}
	options := near[cell] & allowed[index+1] &^ used
	for options != 0 {
		bit := options & -options
		if walk(bits.TrailingZeros32(bit), used|bit, index+1) {
			return true
		}
		options -= bit
	}
	failed[slot] |= flag
	return false
}

func found(original string) bool {
	word = []byte(original)
	length := len(word)
	if bits.OnesCount32(positions[word[0]-'a']) > bits.OnesCount32(positions[word[length-1]-'a']) {
		for left, right := 0, length-1; left < right; left, right = left+1, right-1 {
			word[left], word[right] = word[right], word[left]
		}
	}
	var needed [colorCount][letters]int
	for i, ch := range word {
		needed[i%colorCount][ch-'a']++
	}
	var starts uint32
	for color := 0; color < colorCount; color++ {
		possible := true
		for letter := 0; letter < letters; letter++ {
			if needed[0][letter] > capacity[color][letter] || needed[1][letter] > capacity[color^1][letter] {
				possible = false
			}
		}
		if possible {
			starts |= colors[color]
		}
	}
	if starts == 0 {
		return false
	}
	allowed[length-1] = positions[word[length-1]-'a']
	for i := length - 2; i >= 0; i-- {
		allowed[i] = 0
		options := positions[word[i]-'a']
		for options != 0 {
			bit := options & -options
			cell := bits.TrailingZeros32(bit)
			if near[cell]&allowed[i+1] != 0 {
				allowed[i] |= bit
			}
			options -= bit
		}
	}
	starts &= allowed[0]
	if starts == 0 {
		return false
	}
	for i := range failed {
		failed[i] = 0
	}
	for starts != 0 {
		bit := starts & -starts
		if walk(bits.TrailingZeros32(bit), bit, 0) {
			return true
		}
		starts -= bit
	}
	return false
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var grid []byte
	for row := 0; row < side; row++ {
		in.Scan()
		grid = append(grid, in.Bytes()...)
	}
	for cell, ch := range grid {
		bit := uint32(1) << uint(cell)
		positions[ch-'a'] |= bit
		row, column := cell/side, cell%side
		colors[(row+column)%colorCount] |= bit
		if row > 0 {
			near[cell] |= uint32(1) << uint(cell-side)
		}
		if row+1 < side {
			near[cell] |= uint32(1) << uint(cell+side)
		}
		if column > 0 {
			near[cell] |= uint32(1) << uint(cell-1)
		}
		if column+1 < side {
			near[cell] |= uint32(1) << uint(cell+1)
		}
	}
	for color := 0; color < colorCount; color++ {
		for letter := 0; letter < letters; letter++ {
			capacity[color][letter] = bits.OnesCount32(positions[letter] & colors[color])
		}
	}
	in.Scan()
	n, _ := strconv.Atoi(in.Text())
	cache := make(map[string]bool, n)
	for i := 0; i < n; i++ {
		in.Scan()
		original := in.Text()
		answer, ok := cache[original]
		if !ok {
			answer = found(original)
			cache[original] = answer
		}
		out.WriteString(original)
		if answer {
			out.WriteString(": YES\n")
		} else {
			out.WriteString(": NO\n")
		}
	}
}
