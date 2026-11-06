package main

import (
	"bufio"
	"os"
	"strconv"
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	size := nextInt(input)
	menu := make(map[string]int, size)
	for i := 0; i < size; i++ {
		input.Scan()
		if _, exists := menu[string(input.Bytes())]; !exists {
			menu[input.Text()] = len(menu) + 1
		}
	}
	students := nextInt(input)
	safeCount := len(menu)
	excluded := make([]bool, safeCount+1)
	seen := make([]int, safeCount+1)
	risky := make([]int, students+1)
	for student := 0; student <= students; student++ {
		count := nextInt(input)
		for i := 0; i < count; i++ {
			input.Scan()
			item := menu[string(input.Bytes())]
			if item == 0 || excluded[item] || seen[item] == student+1 {
				continue
			}
			seen[item] = student + 1
			if student == 0 {
				excluded[item] = true
				safeCount--
			} else {
				risky[student]++
			}
		}
	}
	meal := nextInt(input)
	output := bufio.NewWriter(os.Stdout)
	for _, risk := range risky[1:] {
		switch {
		case meal == 0 || risk == 0:
			output.WriteString("YES\n")
		case safeCount-risk < meal:
			output.WriteString("NO\n")
		default:
			output.WriteString("MAYBE\n")
		}
	}
	output.Flush()
}
