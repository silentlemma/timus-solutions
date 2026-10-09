package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const width = 80

func main() {
	line, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	line = strings.TrimRight(line, "\r\n")
	screen := []byte(strings.Repeat(" ", width))
	cursor := 0
	for i := 0; i < len(line); i++ {
		switch line[i] {
		case '<':
			cursor--
		case '>':
			cursor++
		default:
			screen[cursor] = line[i]
			cursor++
		}
		// past either edge the cursor jumps to the leftmost position
		if cursor < 0 || cursor >= width {
			cursor = 0
		}
	}
	fmt.Println(string(screen))
}
