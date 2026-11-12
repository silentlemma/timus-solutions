package main

import "syscall"

const (
	width          = 10
	rows           = 4
	columns        = 3
	maxWords       = 5
	lineSize       = columns*(width+1) + 2
	inputCapacity  = 1024 // At most 820 bytes for 12 courses with CRLF.
	readSize       = 128
	outputCapacity = lineSize * (rows*maxWords + rows + 1)
)

func readInput(input []byte) []byte {
	var block [readSize]byte
	for {
		count, err := syscall.Read(syscall.Stdin, block[:])
		if count > 0 {
			input = append(input, block[:count]...)
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return input
		}
	}
}

func writeOutput(output []byte) {
	for len(output) > 0 {
		count, err := syscall.Write(syscall.Stdout, output)
		if count > 0 {
			output = output[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
	}
}

func main() {
	var inputBuffer [inputCapacity]byte
	input := readInput(inputBuffer[:0])
	at := 0
	nextLine := func() []byte {
		start := at
		for at < len(input) && input[at] != '\n' {
			at++
		}
		end := at
		if at < len(input) {
			at++
		}
		if end > start && input[end-1] == '\r' {
			end--
		}
		return input[start:end]
	}
	count := 0
	for _, c := range nextLine() {
		if c >= '0' && c <= '9' {
			count = count*10 + int(c-'0')
		}
	}
	var grid [rows][columns][maxWords][width]byte
	var heights [rows]int
	for row := range grid {
		heights[row] = 1
		for col := range grid[row] {
			for level := range grid[row][col] {
				for i := range grid[row][col][level] {
					grid[row][col][level][i] = ' '
				}
			}
		}
	}
	for course := 0; course < count; course++ {
		name, day := nextLine(), nextLine()
		last := len(day) - 1
		for last >= 0 && day[last] <= ' ' {
			last--
		}
		lesson := int(day[last] - '1')
		column := 0
		if day[0] == 'S' {
			column = 2
		} else if day[1] != 'u' {
			column = 1
		}
		level, used := 0, 0
		for start := 0; start < len(name); {
			if name[start] == ' ' {
				start++
				continue
			}
			end := start
			for end < len(name) && name[end] != ' ' {
				end++
			}
			length := end - start
			if used > 0 && used+1+length > width {
				level++
				used = 0
			}
			if used > 0 {
				used++
			}
			// Fixed padded cells avoid per-line strings; the five-word bound is sufficient.
			copy(grid[lesson][column][level][used:], name[start:end])
			used += length
			start = end
		}
		if level+1 > heights[lesson] {
			heights[lesson] = level + 1
		}
	}
	var border, line [lineSize]byte
	for i := 0; i < lineSize-1; i++ {
		border[i] = '-'
		if i%(width+1) == 0 {
			border[i] = '+'
		}
	}
	border[lineSize-1] = '\n'
	var buffer [outputCapacity]byte
	output := append(buffer[:0], border[:]...)
	for row := 0; row < rows; row++ {
		for level := 0; level < heights[row]; level++ {
			line[0] = '|'
			for col := 0; col < columns; col++ {
				copy(line[1+col*(width+1):], grid[row][col][level][:])
				line[(col+1)*(width+1)] = '|'
			}
			line[lineSize-1] = '\n'
			output = append(output, line[:]...)
		}
		output = append(output, border[:]...)
	}
	writeOutput(output)
}
