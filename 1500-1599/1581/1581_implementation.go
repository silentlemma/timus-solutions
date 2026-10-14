package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	numbers := make([]int, n)
	for i := range numbers {
		fmt.Fscan(in, &numbers[i])
	}
	// each run of equal numbers is said as its length and then the number
	var out []string
	for i := 0; i < n; {
		j := i
		for j < n && numbers[j] == numbers[i] {
			j++
		}
		out = append(out, strconv.Itoa(j-i), strconv.Itoa(numbers[i]))
		i = j
	}
	fmt.Println(strings.Join(out, " "))
}
