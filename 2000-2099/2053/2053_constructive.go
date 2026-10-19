package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const grid = 4
const vertices = grid * grid
const outerScale = 900
const dimension = 2
const roundingOffset = 0.5

type graphType [vertices][vertices]int
type pointsType [vertices][dimension]int

func connect(graph *graphType, a, b int) { graph[a][b] = 1; graph[b][a] = 1 }

func solve() (pointsType, graphType) {
	var graph graphType
	for row := 0; row < grid; row++ {
		for column := 0; column < grid; column++ {
			vertex := row*grid + column
			if column+1 < grid {
				connect(&graph, vertex, vertex+1)
			}
			if row+1 < grid {
				connect(&graph, vertex, vertex+grid)
			}
			if row+1 < grid && column+1 < grid {
				connect(&graph, vertex, vertex+grid+1)
			}
		}
	}
	corners := [grid]int{0, grid - 1, vertices - 1, vertices - grid}
	for side, a := range corners {
		d := corners[(side+1)%grid]
		step := (d - a) / (grid - 1)
		connect(&graph, a, d)
		connect(&graph, a, d-step)
	}
	connect(&graph, corners[1], corners[grid-1])
	var points pointsType
	var fixed [vertices]bool
	points[corners[0]] = [dimension]int{-outerScale, -outerScale}
	points[corners[1]] = [dimension]int{outerScale, -outerScale}
	points[corners[grid-1]] = [dimension]int{0, outerScale}
	fixed[corners[0]], fixed[corners[1]], fixed[corners[grid-1]] = true, true, true
	var index [vertices]int
	var inside []int
	for vertex := 0; vertex < vertices; vertex++ {
		if !fixed[vertex] {
			index[vertex] = len(inside)
			inside = append(inside, vertex)
		}
	}
	size := len(inside)
	matrix := make([][]float64, size)
	for i := range matrix {
		matrix[i] = make([]float64, size+dimension)
	}
	for _, vertex := range inside {
		row := matrix[index[vertex]]
		for neighbour := 0; neighbour < vertices; neighbour++ {
			if graph[vertex][neighbour] != 0 {
				row[index[vertex]]++
				if !fixed[neighbour] {
					row[index[neighbour]]--
				} else {
					for axis := 0; axis < dimension; axis++ {
						row[size+axis] += float64(points[neighbour][axis])
					}
				}
			}
		}
	}
	for column := 0; column < size; column++ {
		pivot := column
		for row := column + 1; row < size; row++ {
			if math.Abs(matrix[row][column]) > math.Abs(matrix[pivot][column]) {
				pivot = row
			}
		}
		matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
		divisor := matrix[column][column]
		for entry := range matrix[column] {
			matrix[column][entry] /= divisor
		}
		for row := 0; row < size; row++ {
			if row != column {
				factor := matrix[row][column]
				for entry := range matrix[row] {
					matrix[row][entry] -= factor * matrix[column][entry]
				}
			}
		}
	}
	for _, vertex := range inside {
		for axis := 0; axis < dimension; axis++ {
			points[vertex][axis] = int(math.Floor(matrix[index[vertex]][size+axis] + roundingOffset))
		}
	}
	return points, graph
}

func main() {
	points, graph := solve()
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, point := range points {
		fmt.Fprintln(out, point[0], point[1])
	}
	for _, row := range graph {
		for _, bit := range row {
			fmt.Fprint(out, bit)
		}
		fmt.Fprintln(out)
	}
}
