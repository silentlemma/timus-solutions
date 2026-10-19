package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type meter struct {
	name  string
	foot  int // syllables in a foot
	place int // place of the stressed syllable, from 1
}

var meters = []meter{{"trochee", 2, 1}, {"iamb", 2, 2}, {"dactyl", 3, 1},
	{"amphibrach", 3, 2}, {"anapaest", 3, 3}}

func stresses(line string) []bool {
	out := []bool{}
	for _, word := range strings.Fields(line) {
		for _, syllable := range strings.Split(word, "-") {
			if syllable != "" {
				out = append(out, strings.Contains(syllable, "["))
			}
		}
	}
	return out
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	first, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(first))
	poem := make([][]bool, n)
	for i := range poem {
		line, _ := reader.ReadString('\n')
		poem[i] = stresses(line)
	}
	for _, m := range meters {
		// the last foot may be cut short, so only the place within a foot
		// matters, and every syllable must agree with it
		fits := true
		for _, verse := range poem {
			for i, s := range verse {
				if s != (i%m.foot == m.place-1) {
					fits = false
				}
			}
		}
		if fits {
			fmt.Println(m.name)
			return
		}
	}
	fmt.Println("not a poem")
}
