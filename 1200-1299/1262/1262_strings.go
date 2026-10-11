package main

import (
	"bufio"
	"fmt"
	"os"
)

// Roman digits needed for each decimal digit: -, I, II, III, IV, V, VI,
// VII, VIII, IX
var lengths = [10]int{0, 1, 2, 3, 2, 1, 2, 3, 4, 2}

func main() {
	var s string
	fmt.Fscan(bufio.NewReader(os.Stdin), &s)
	total := 0
	for i := 0; i < len(s); i++ {
		total += lengths[s[i]-'0']
	}
	fmt.Println(total)
}
