package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 4096

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	size, _ := strconv.Atoi(input.Text())
	previous := make([]byte, size)
	left, right, up, down := true, true, true, true
	for y := 0; y < size && input.Scan(); y++ {
		row := input.Bytes()
		for x, color := range row {
			if x > 0 && row[x-1] != color {
				left, right = left && color == '0', right && color == '1'
			}
			if y > 0 && previous[x] != color {
				up, down = up && color == '0', down && color == '1'
			}
		}
		if !(left || right || up || down) {
			os.Stdout.WriteString("No\n")
			return
		}
		copy(previous, row)
	}
	os.Stdout.WriteString("Yes\n")
}
