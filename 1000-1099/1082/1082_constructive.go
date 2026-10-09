package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	// on sorted numbers every partition peels off just the first one
	parts := make([]string, n)
	for i := range parts {
		parts[i] = strconv.Itoa(i + 1)
	}
	fmt.Println(strings.Join(parts, " "))
}
