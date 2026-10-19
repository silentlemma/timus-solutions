package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	nameWidth = 30
	dateWidth = 8
	letters   = "ABCDEFGHIJKLM"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	readLine := func() string {
		in.Scan()
		return strings.TrimRight(in.Text(), "\r ")
	}
	pad := func(s string, width int) string {
		return s + strings.Repeat(" ", width-len(s))
	}
	border := "+" + strings.Repeat("-", nameWidth) + "+" + strings.Repeat("-", dateWidth) +
		"+" + strings.Repeat("-", len(letters)) + "+"
	fmt.Fprintln(out, border)
	fmt.Fprintf(out, "|%s|%s|%s|\n", pad("Contest name", nameWidth), pad("Date", dateWidth), letters)
	fmt.Fprintln(out, border)
	n, _ := strconv.Atoi(readLine())
	for c := 0; c < n; c++ {
		name, date := readLine(), readLine()
		counts := strings.Fields(readLine())
		p, _ := strconv.Atoi(counts[0])
		s, _ := strconv.Atoi(counts[1])
		// '.' for a given problem, 'x' once submitted, 'o' once accepted
		marks := []byte(strings.Repeat(".", p) + strings.Repeat(" ", len(letters)-p))
		for k := 0; k < s; k++ {
			submit := readLine()
			i := submit[0] - 'A'
			if submit[2:] == "Accepted" {
				marks[i] = 'o'
			} else if marks[i] != 'o' {
				marks[i] = 'x'
			}
		}
		fmt.Fprintf(out, "|%s|%s|%s|\n", pad(name, nameWidth), date, marks)
		fmt.Fprintln(out, border)
	}
}
