package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strings"
)

const (
	width = 6
	full  = 100
	none  = -1
	code  = 3
)

type question struct {
	code, line string
	answers    []byte
	lines      []string
}

// shares gives percents of total that round each value down or up and add
// up to 100: round all down, then raise the ones with the largest remainders
func shares(values []int, total int) []int {
	out := make([]int, len(values))
	if total == 0 {
		for k := range out {
			out[k] = none
		}
		return out
	}
	rest := make([]int, len(values))
	order := make([]int, len(values))
	sum := 0
	for k, v := range values {
		out[k], rest[k], order[k] = full*v/total, full*v%total, k
		sum += out[k]
	}
	sort.SliceStable(order, func(a, b int) bool { return rest[order[a]] > rest[order[b]] })
	for k := 0; k < full-sum; k++ {
		out[order[k]]++
	}
	return out
}

func cell(s string) string {
	return strings.Repeat(" ", width-len(s)) + s
}

func percent(p int) string {
	if p == none {
		return cell("-")
	}
	return cell(fmt.Sprintf("%d%%", p))
}

func index(list []byte, c byte) int {
	for k, x := range list {
		if x == c {
			return k
		}
	}
	return -1
}

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	lines := strings.Split(strings.ReplaceAll(string(data), "\r", ""), "\n")
	survey, at := lines[0], 1
	var questions []question
	place := map[string]int{}
	for ; lines[at] != "#"; at++ {
		if lines[at][0] == ' ' {
			q := &questions[len(questions)-1]
			q.answers = append(q.answers, lines[at][1])
			q.lines = append(q.lines, lines[at])
		} else {
			place[lines[at][:code]] = len(questions)
			questions = append(questions, question{code: lines[at][:code], line: lines[at]})
		}
	}
	var results []string
	for at++; lines[at] != "#"; at++ {
		results = append(results, lines[at])
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	started := false
	for at++; at < len(lines) && lines[at] != "#"; at++ {
		p1, p2 := place[lines[at][:code]], place[lines[at][code+1:2*code+1]]
		first, second := questions[p1], questions[p2]
		rows, cols := len(first.answers), len(second.answers)
		// the table with its totals as one more column and one more row
		table := make([][]int, rows+1)
		for i := range table {
			table[i] = make([]int, cols+1)
		}
		for _, line := range results {
			r, c := index(first.answers, line[p1]), index(second.answers, line[p2])
			for _, i := range []int{r, rows} {
				for _, j := range []int{c, cols} {
					table[i][j]++
				}
			}
		}
		byRow, byCol := make([][]int, rows+1), make([][]int, rows+1)
		for i := 0; i <= rows; i++ {
			byRow[i] = shares(table[i][:cols], table[i][cols])
			if table[i][cols] > 0 {
				byRow[i] = append(byRow[i], full)
			} else {
				byRow[i] = append(byRow[i], none)
			}
			byCol[i] = make([]int, cols+1)
		}
		for j := 0; j <= cols; j++ {
			part := make([]int, rows)
			for i := range part {
				part[i] = table[i][j]
			}
			got := shares(part, table[rows][j])
			for i := range part {
				byCol[i][j] = got[i]
			}
			byCol[rows][j] = none
			if table[rows][j] > 0 {
				byCol[rows][j] = full
			}
		}
		if started {
			fmt.Fprintln(out)
		}
		started = true
		fmt.Fprintf(out, "%s - %s\n", survey, lines[at][2*code+2:])
		for _, q := range []question{first, second} {
			fmt.Fprintln(out, q.line)
			for _, line := range q.lines {
				fmt.Fprintln(out, line)
			}
		}
		fmt.Fprint(out, "\n", strings.Repeat(" ", width))
		for _, c := range second.answers {
			fmt.Fprint(out, cell(second.code+":"+string(c)))
		}
		fmt.Fprintln(out, cell("TOTAL"))
		for i := 0; i <= rows; i++ {
			label := "TOTAL"
			if i < rows {
				label = first.code + ":" + string(first.answers[i])
			}
			fmt.Fprint(out, cell(label))
			for _, v := range table[i] {
				fmt.Fprint(out, cell(fmt.Sprint(v)))
			}
			for _, ps := range [][]int{byRow[i], byCol[i]} {
				fmt.Fprint(out, "\n", strings.Repeat(" ", width))
				for _, p := range ps {
					fmt.Fprint(out, percent(p))
				}
			}
			fmt.Fprintln(out)
		}
	}
}
