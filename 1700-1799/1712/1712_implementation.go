package main

import "fmt"

const size = 4

func main() {
	var grille, square [size]string
	for r := range grille {
		fmt.Scan(&grille[r])
	}
	for r := range square {
		fmt.Scan(&square[r])
	}
	var password []byte
	// read the windows row by row, then turn the grille clockwise:
	// the cell (r, c) of the turned grille is (size-1-c, r) of the old one
	for turn := 0; turn < size; turn++ {
		for r := 0; r < size; r++ {
			for c := 0; c < size; c++ {
				if grille[r][c] == 'X' {
					password = append(password, square[r][c])
				}
			}
		}
		var turned [size]string
		for r := 0; r < size; r++ {
			row := make([]byte, size)
			for c := 0; c < size; c++ {
				row[c] = grille[size-1-c][r]
			}
			turned[r] = string(row)
		}
		grille = turned
	}
	fmt.Println(string(password))
}
