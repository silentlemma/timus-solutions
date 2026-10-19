package main

import (
	"fmt"
	"io/ioutil"
	"math/big"
	"os"
	"sort"
	"strconv"
	"strings"
)

const percent int64 = 100
const scale int64 = 1000000
const digits = 6
const integerBits = 64

func determinant(matrix [][]*big.Int) *big.Int {
	n := len(matrix)
	if n == 0 {
		return big.NewInt(1)
	}
	a := make([][]*big.Int, n)
	for i := range a {
		a[i] = make([]*big.Int, n)
		for j := range a[i] {
			a[i][j] = new(big.Int).Set(matrix[i][j])
		}
	}
	previous := big.NewInt(1)
	sign := int64(1)
	for k := 0; k < n-1; k++ {
		pivotRow := k
		for pivotRow < n && a[pivotRow][k].Sign() == 0 {
			pivotRow++
		}
		if pivotRow == n {
			return big.NewInt(0)
		}
		if pivotRow != k {
			a[k], a[pivotRow] = a[pivotRow], a[k]
			sign = -sign
		}
		pivot := a[k][k]
		for row := k + 1; row < n; row++ {
			for col := k + 1; col < n; col++ {
				first := new(big.Int).Mul(a[row][col], pivot)
				second := new(big.Int).Mul(a[row][k], a[k][col])
				a[row][col] = new(big.Int).Quo(new(big.Int).Sub(first, second), previous)
			}
			a[row][k] = big.NewInt(0)
		}
		previous = pivot
	}
	return new(big.Int).Mul(a[n-1][n-1], big.NewInt(sign))
}

func solve(input string) string {
	recipes := make(map[string]map[string]int64)
	parts := make(map[string]bool)
	for _, line := range strings.Split(input, "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		sides := strings.SplitN(line, ":", 2)
		name := strings.TrimSpace(sides[0])
		tokens := strings.Fields(sides[1])
		row := make(map[string]int64)
		for i := 0; i < len(tokens); i += 2 {
			value, _ := strconv.ParseInt(tokens[i+1], 10, integerBits)
			row[tokens[i]] = value
			parts[tokens[i]] = true
		}
		recipes[name] = row
	}
	names := make([]string, 0, len(recipes))
	for name := range recipes {
		names = append(names, name)
		delete(parts, name)
	}
	sort.Strings(names)
	bases := make([]string, 0, len(parts))
	for name := range parts {
		bases = append(bases, name)
	}
	sort.Strings(bases)
	n, m := len(names), len(bases)
	a := make([][]*big.Int, n)
	for i := range a {
		a[i] = make([]*big.Int, n)
		for j := range a[i] {
			value := -recipes[names[i]][names[j]]
			if i == j {
				value += percent
			}
			a[i][j] = big.NewInt(value)
		}
	}
	denominator := determinant(a)
	numerators := make([][]*big.Int, n)
	for col := 0; col < n; col++ {
		numerators[col] = make([]*big.Int, m)
		for base := 0; base < m; base++ {
			replaced := make([][]*big.Int, n)
			for row := range replaced {
				replaced[row] = append([]*big.Int(nil), a[row]...)
				replaced[row][col] = big.NewInt(recipes[names[row]][bases[base]])
			}
			numerators[col][base] = determinant(replaced)
		}
	}
	var output strings.Builder
	multiplier := big.NewInt(percent * scale)
	for row, name := range names {
		units := make([]int64, m)
		var total int64
		largest := 0
		for base := 0; base < m; base++ {
			scaled := new(big.Int).Mul(numerators[row][base], multiplier)
			units[base] = new(big.Int).Quo(scaled, denominator).Int64()
			total += units[base]
			if numerators[row][base].Cmp(numerators[row][largest]) > 0 {
				largest = base
			}
		}
		units[largest] += percent*scale - total
		fmt.Fprintf(&output, "%s :", name)
		for base := 0; base < m; base++ {
			fmt.Fprintf(&output, " %s %d.%0*d", bases[base], units[base]/scale, digits, units[base]%scale)
		}
		output.WriteByte('\n')
	}
	return output.String()
}

func main() { input, _ := ioutil.ReadAll(os.Stdin); fmt.Print(solve(string(input))) }
