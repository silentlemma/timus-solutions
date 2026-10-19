package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
)

const decimalBase = 10

type input struct {
	data []byte
	at   int
}

func (in *input) integer() int {
	for in.data[in.at] <= ' ' {
		in.at++
	}
	value := 0
	for in.at < len(in.data) && in.data[in.at] >= '0' && in.data[in.at] <= '9' {
		value = value*decimalBase + int(in.data[in.at]-'0')
		in.at++
	}
	return value
}
func (in *input) base() bool {
	for in.data[in.at] <= ' ' {
		in.at++
	}
	value := in.data[in.at] == '1'
	in.at++
	return value
}
func ceilDivide(numerator, denominator int) int {
	result := numerator / denominator
	if numerator > 0 && numerator%denominator != 0 {
		result++
	}
	return result
}
func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	height, width := in.integer(), in.integer()
	far := height + width
	distances := make([]int, height*width)
	last := make([]int, width)
	for column := range last {
		last[column] = -far
	}
	for row := 0; row < height; row++ {
		for column := 0; column < width; column++ {
			if in.base() {
				last[column] = row
			}
			distances[row*width+column] = row - last[column]
		}
	}
	following := make([]int, width)
	for column := range following {
		following[column] = height + far
	}
	for row := height - 1; row >= 0; row-- {
		for column := 0; column < width; column++ {
			at := row*width + column
			value := distances[at]
			if value == 0 {
				following[column] = row
			} else if following[column]-row < value {
				distances[at] = following[column] - row
			}
		}
	}
	costs := make([]int, width)
	intercepts := make([]int, width)
	sites := make([]int, width)
	starts := make([]int, width)
	out := bufio.NewWriter(os.Stdout)
	for row := 0; row < height; row++ {
		used := 0
		for q := 0; q < width; q++ {
			vertical := distances[row*width+q]
			if vertical >= far {
				continue
			}
			costs[q] = vertical * vertical
			intercepts[q] = costs[q] + q*q
			first := 0
			for used > 0 {
				p := sites[used-1]
				first = ceilDivide(intercepts[q]-intercepts[p], 2*(q-p))
				if first > starts[used-1] {
					break
				}
				used--
			}
			if used == 0 {
				first = 0
			}
			sites[used] = q
			starts[used] = first
			used++
		}
		current := 0
		for x := 0; x < width; x++ {
			for current+1 < used && starts[current+1] <= x {
				current++
			}
			p := sites[current]
			delta := x - p
			if x != 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(delta*delta + costs[p]))
		}
		out.WriteByte('\n')
	}
	out.Flush()
}
