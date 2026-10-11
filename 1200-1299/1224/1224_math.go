package main

import "fmt"

func main() {
	var n, m int64
	fmt.Scan(&n, &m)
	// every full lap turns four times and peels two rows and two columns; the
	// spiral ends in the middle of the shorter side, so only that side counts
	if n <= m {
		fmt.Println(2 * (n - 1))
	} else {
		fmt.Println(2*m - 1)
	}
}
