package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var notes = []int{10, 50, 100, 500, 1000, 5000}

func main() {
	reader := bufio.NewReader(os.Stdin)
	total, smallest := 0, 0
	for _, note := range notes {
		var count int
		if _, err := fmt.Fscan(reader, &count); err != nil {
			return
		}
		total += count * note
		if count > 0 && smallest == 0 {
			smallest = note
		}
	}
	var price int
	fmt.Fscan(reader, &price)
	// k tickets fit when k * price <= total, and taking away the smallest
	// note must leave too little: total - smallest < k * price
	low, high := (total-smallest)/price+1, total/price
	parts := make([]string, 0, high-low+1)
	for k := low; k <= high; k++ {
		parts = append(parts, strconv.Itoa(k))
	}
	fmt.Println(len(parts))
	fmt.Println(strings.Join(parts, " "))
}
