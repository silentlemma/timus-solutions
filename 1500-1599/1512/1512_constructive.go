package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const period = 6 // the simple pattern fails exactly when n mod 6 is 2

// evenRows gives the row of the queen in each column 1 ... n for even n,
// keeping the main diagonal free.
func evenRows(n int) []int {
	half := n / 2
	rows := make([]int, n)
	for i := 1; i <= half; i++ {
		if n%period != 2 {
			// the even rows in the left half, the odd rows in the right half
			rows[i-1] = 2 * i
			rows[half+i-1] = 2*i - 1
		} else {
			shift := (2*(i-1) + half - 1) % n
			rows[i-1] = 1 + shift
			rows[n-i] = n - shift
		}
	}
	return rows
}

func main() {
	var n int
	fmt.Scan(&n)
	// an odd board is an even one plus the free corner (n, n)
	rows := evenRows(n - n%2)
	if n%2 == 1 {
		rows = append(rows, n)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for col := 1; col <= n; col++ {
		out.WriteString(strconv.Itoa(col) + " " + strconv.Itoa(rows[col-1]) + "\n")
	}
}
