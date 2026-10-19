package main

import (
	"bufio"
	"fmt"
	"os"
)

const smallOddLimit = 5
const firstOddPrime = 3
const column = 2

type builder struct {
	grid  [][]int
	value int
}

func (b *builder) visit(row, col int) { b.value++; b.grid[row][col] = b.value }

func construct(n int) [][]int {
	b := builder{grid: make([][]int, n)}
	for i := range b.grid {
		b.grid[i] = make([]int, n)
	}
	if n%2 == 1 && n < smallOddLimit {
		for row := 0; row < n; row++ {
			for step := 0; step < n; step++ {
				col := step
				if row%2 == 1 {
					col = n - 1 - step
				}
				b.visit(row, col)
			}
		}
		return b.grid
	}
	limit := n * n
	prime := make([]bool, limit+1)
	for p := 2; p <= limit; p++ {
		prime[p] = true
	}
	for p := 2; p*p <= limit; p++ {
		if prime[p] {
			for multiple := p * p; multiple <= limit; multiple += p {
				prime[multiple] = false
			}
		}
	}
	following := make([]int, limit+1)
	widths := make([]int, n)
	largest := 0
	for p := limit; p >= 0; p-- {
		following[p] = largest
		if prime[p] {
			largest = p
		}
	}
	if n%2 == 0 {
		b.visit(0, 1)
		b.visit(0, 0)
		b.visit(1, 0)
		for row := 1; row < n-2; row += 2 {
			width := (following[b.value] - b.value - 2) / 2
			widths[row] = width
			for col := 1; col <= width; col++ {
				b.visit(row, col)
			}
			b.visit(row+1, width)
			for col := width - 1; col >= 0; col-- {
				b.visit(row+1, col)
			}
			b.visit(row+2, 0)
		}
		for col := 1; col < n; col++ {
			b.visit(n-1, col)
		}
		for row := n - 2; row > 1; row -= 2 {
			width := widths[row-1]
			for col := n - 1; col > width; col-- {
				b.visit(row, col)
			}
			for col := width + 1; col < n; col++ {
				b.visit(row-1, col)
			}
		}
		for col := n - 1; col > 1; col-- {
			b.visit(0, col)
		}
		return b.grid
	}
	rightWidth := n - column - 1
	initial := -1
	for candidate := 0; candidate <= rightWidth; candidate++ {
		if candidate == rightWidth-1 {
			continue
		}
		first := firstOddPrime + 2*candidate
		current := first + 2*n
		if !prime[first] || !prime[current] {
			continue
		}
		valid := true
		for row := n - 1; row > column+1; row -= 2 {
			nextPrime := following[current]
			width := (nextPrime - current - 2) / 2
			if width < 0 || width >= rightWidth {
				valid = false
				break
			}
			widths[row] = width
			current = nextPrime
		}
		if valid {
			initial = candidate
			break
		}
	}
	if initial < 0 {
		panic("No admissible prime prefix")
	}
	b.visit(1, 1)
	b.visit(1, column)
	for col := column + 1; col <= column+initial; col++ {
		b.visit(1, col)
	}
	for col := column + initial; col >= column; col-- {
		b.visit(0, col)
	}
	b.visit(0, 1)
	b.visit(0, 0)
	b.visit(1, 0)
	b.visit(2, 0)
	b.visit(2, 1)
	for row := column + 1; row < n; row += 2 {
		b.visit(row, 1)
		b.visit(row, 0)
		b.visit(row+1, 0)
		b.visit(row+1, 1)
	}
	b.visit(n-1, column)
	for row := n - 1; row > column+1; row -= 2 {
		width := widths[row]
		for col := column + 1; col <= column+width; col++ {
			b.visit(row, col)
		}
		b.visit(row-1, column+width)
		for col := column + width - 1; col >= column; col-- {
			b.visit(row-1, col)
		}
		b.visit(row-2, column)
	}
	left := column + initial + 1
	if left == n {
		for col := column + 1; col < n; col++ {
			b.visit(2, col)
		}
	} else {
		for col := column + 1; col <= left; col++ {
			b.visit(2, col)
		}
		b.visit(1, left)
		for col := left; col < n; col++ {
			b.visit(0, col)
		}
		for col := n - 1; col > left; col-- {
			b.visit(1, col)
		}
		for col := left + 1; col < n; col++ {
			b.visit(2, col)
		}
	}
	for row := column + 1; row < n; row += 2 {
		width := widths[row+1]
		for col := n - 1; col > column+width; col-- {
			b.visit(row, col)
		}
		for col := column + width + 1; col < n; col++ {
			b.visit(row+1, col)
		}
	}
	return b.grid
}

func main() {
	var n int
	fmt.Fscan(bufio.NewReader(os.Stdin), &n)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, row := range construct(n) {
		for col, value := range row {
			if col > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, value)
		}
		fmt.Fprintln(out)
	}
}
