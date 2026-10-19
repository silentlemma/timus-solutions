package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

type fastInput struct {
	data  []byte
	index int
}

func (input *fastInput) nextInt() int {
	for input.index < len(input.data) && input.data[input.index] <= ' ' {
		input.index++
	}
	value := 0
	for input.index < len(input.data) {
		digit := input.data[input.index]
		if digit < '0' || digit > '9' {
			break
		}
		value = value*10 + int(digit-'0')
		input.index++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := fastInput{data: data}
	rows, columns := input.nextInt(), input.nextInt()
	stride := columns + 1
	rowPrefix := make([]int64, rows*stride)
	diagonalPrefix := make([]int64, (rows+1)*stride)
	total := int64(0)
	for row := 0; row < rows; row++ {
		for column := 0; column < columns; column++ {
			value := int64(input.nextInt())
			rowPrefix[row*stride+column+1] = rowPrefix[row*stride+column] + value
			diagonalPrefix[(row+1)*stride+column] =
				diagonalPrefix[row*stride+column+1] + value
			total += value
		}
	}

	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	queries := input.nextInt()
	maximumDistance := rows + columns - 2
	for query := 0; query < queries; query++ {
		wind := input.nextInt()
		if wind >= maximumDistance {
			fmt.Fprintln(output, total, 1, 1)
			continue
		}

		below := make([]int64, columns)
		best := int64(-1)
		bestRow, bestColumn := rows, columns
		for row := rows - 1; row >= 0; row-- {
			lastRow := row + wind + 1
			if lastRow >= rows {
				lastRow = rows - 1
			}
			for column := 0; column < columns; column++ {
				right := column + wind + 1
				if right > columns {
					right = columns
				}
				sum := below[column] + rowPrefix[row*stride+right] - rowPrefix[row*stride+column]

				// Moving up adds one row and removes the farthest anti-diagonal.
				diagonal := row + column + wind + 1
				firstRow := row + 1
				if diagonal-columns+1 > firstRow {
					firstRow = diagonal - columns + 1
				}
				if firstRow <= lastRow {
					sum -= diagonalPrefix[(lastRow+1)*stride+diagonal-lastRow] -
						diagonalPrefix[firstRow*stride+diagonal-firstRow+1]
				}
				below[column] = sum
				if sum > best || (sum == best &&
					(row < bestRow || (row == bestRow && column < bestColumn))) {
					best, bestRow, bestColumn = sum, row, column
				}
			}
		}
		fmt.Fprintln(output, best, bestRow+1, bestColumn+1)
	}
}
