package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var k int64
	fmt.Scan(&k)
	// from the BELL&RET cell upwards: "CALL i + 1" at cell i doubles the
	// bells made from the next cell, a call of the last cell adds one more,
	// so the binary digits of K give the cells
	var doubles []bool
	bits := strconv.FormatInt(k, 2)
	for _, bit := range bits[1:] {
		doubles = append(doubles, true)
		if bit == '1' {
			doubles = append(doubles, false)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	last := len(doubles)
	for cell := 0; cell < last; cell++ {
		target := last
		if doubles[last-1-cell] {
			target = cell + 1
		}
		fmt.Fprintf(out, "CALL %d\n", target)
	}
	fmt.Fprintln(out, "BELL&RET")
}
