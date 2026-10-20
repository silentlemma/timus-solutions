package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const modulus int64 = 998244353
const cyclePeriod = 4
const branchDegree = 3

type reader struct {
	data []byte
	pos  int
}

func (r *reader) integer() int {
	for r.pos < len(r.data) && r.data[r.pos] <= ' ' {
		r.pos++
	}
	value := 0
	for r.pos < len(r.data) && r.data[r.pos] >= '0' && r.data[r.pos] <= '9' {
		value = value*10 + int(r.data[r.pos]-'0')
		r.pos++
	}
	return value
}

func power(base, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent >>= 1
	}
	return result
}

func determinant(matrix [][]int64, size int) int64 {
	result := int64(1)
	for column := 0; column < size; column++ {
		pivot := column
		for pivot < size && matrix[pivot][column] == 0 {
			pivot++
		}
		if pivot == size {
			return 0
		}
		if pivot != column {
			matrix[pivot], matrix[column] = matrix[column], matrix[pivot]
			result = modulus - result
		}
		value := matrix[column][column]
		result = result * value % modulus
		inverse := power(value, modulus-2)
		for row := column + 1; row < size; row++ {
			if matrix[row][column] == 0 {
				continue
			}
			factor := matrix[row][column] * inverse % modulus
			for next := column + 1; next < size; next++ {
				value = matrix[row][next] - factor*matrix[column][next]%modulus
				if value < 0 {
					value += modulus
				}
				matrix[row][next] = value
			}
		}
	}
	return result
}

func addEdge(matrix [][]int64, from, to int, weight int64) {
	matrix[from][to] = (matrix[from][to] + weight) % modulus
	matrix[to][from] = (matrix[to][from] + weight) % modulus
}

func solve(r *reader) int64 {
	n, m := r.integer(), r.integer()
	head := make([]int, n)
	degree := make([]int, n)
	alive := make([]bool, n)
	for vertex := range head {
		head[vertex] = -1
		alive[vertex] = true
	}
	to := make([]int, 2*m)
	next := make([]int, 2*m)
	for edge := 0; edge < m; edge++ {
		u, v := r.integer()-1, r.integer()-1
		first := 2 * edge
		to[first], next[first], head[u] = v, head[u], first
		to[first+1], next[first+1], head[v] = u, head[v], first+1
		degree[u]++
		degree[v]++
	}
	queue := make([]int, 0, n)
	for vertex, value := range degree {
		if value == 0 {
			return 0
		}
		if value == 1 {
			queue = append(queue, vertex)
		}
	}
	answer := int64(1)
	// A leaf and its neighbor form an invertible block of determinant -1.
	for front := 0; front < len(queue); front++ {
		u := queue[front]
		if !alive[u] {
			continue
		}
		v := -1
		for edge := head[u]; edge != -1; edge = next[edge] {
			if alive[to[edge]] {
				v = to[edge]
				break
			}
		}
		if v == -1 {
			return 0
		}
		alive[u], alive[v] = false, false
		answer = modulus - answer
		for edge := head[v]; edge != -1; edge = next[edge] {
			w := to[edge]
			if !alive[w] {
				continue
			}
			degree[w]--
			if degree[w] == 0 {
				return 0
			}
			if degree[w] == 1 {
				queue = append(queue, w)
			}
		}
	}
	ids := make([]int, n)
	branches := 0
	for vertex := range ids {
		ids[vertex] = -1
		if alive[vertex] && degree[vertex] >= branchDegree {
			ids[vertex] = branches
			branches++
		}
	}
	capacity := 2 * branches
	matrix := make([][]int64, capacity)
	for row := range matrix {
		matrix[row] = make([]int64, capacity)
	}
	seen := make([]bool, n)
	size := branches
	for u := 0; u < n; u++ {
		if ids[u] == -1 {
			continue
		}
		for edge := head[u]; edge != -1; edge = next[edge] {
			v := to[edge]
			if !alive[v] {
				continue
			}
			if ids[v] != -1 {
				if u < v {
					addEdge(matrix, ids[u], ids[v], 1)
				}
				continue
			}
			if seen[v] {
				continue
			}
			previous, length := u, 0
			for ids[v] == -1 {
				seen[v] = true
				length++
				w := -1
				for current := head[v]; current != -1; current = next[current] {
					if alive[to[current]] && to[current] != previous {
						w = to[current]
						break
					}
				}
				previous, v = v, w
			}
			weight := int64(1)
			if (length/2)&1 != 0 {
				weight = modulus - 1
				answer = modulus - answer
			}
			// Eliminate pairs on the path; an odd path retains one vertex.
			if length&1 == 0 {
				addEdge(matrix, ids[u], ids[v], weight)
			} else {
				if size == capacity {
					return 0
				}
				addEdge(matrix, ids[u], size, weight)
				addEdge(matrix, ids[v], size, 1)
				size++
			}
		}
	}
	for start := 0; start < n; start++ {
		if !alive[start] || ids[start] != -1 || seen[start] {
			continue
		}
		previous, vertex, length := -1, start, 0
		for !seen[vertex] {
			seen[vertex] = true
			length++
			w := -1
			for edge := head[vertex]; edge != -1; edge = next[edge] {
				if alive[to[edge]] && to[edge] != previous {
					w = to[edge]
					break
				}
			}
			previous, vertex = vertex, w
		}
		if length&1 != 0 {
			answer = answer * 2 % modulus
		} else if length%cyclePeriod == 0 {
			return 0
		} else {
			answer = answer * (modulus - cyclePeriod) % modulus
		}
	}
	return answer * determinant(matrix, size) % modulus
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	r := reader{data: data}
	fmt.Println(solve(&r))
}
