package main

import (
	"bufio"
	"os"
	"strconv"
)

const lyoshaName = "Efremov"
const vadikName = "Kantorov"
const fullTeam = 3

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	next := func() string { input.Scan(); return input.Text() }
	number := func() int { value, _ := strconv.Atoi(next()); return value }
	n := number()
	full, pairs := map[string]bool{}, map[string]bool{}
	for i := 0; i < n; i++ {
		size := number()
		for j := 0; j < size; j++ {
			name := next()
			if name != lyoshaName && name != vadikName {
				if size == fullTeam {
					full[name] = true
				} else {
					pairs[name] = true
				}
			}
		}
	}
	lyosha, vadik, m := number(), number(), number()
	best, chosen := -1, ""
	for i := 0; i < m; i++ {
		name, rating := next(), number()
		strength := vadik + rating
		if !full[name] {
			strength += lyosha
		} else if pairs[name] {
			continue
		}
		if strength > best {
			best, chosen = strength, name
		}
	}
	if best < 0 {
		os.Stdout.WriteString("Fail\n")
	} else {
		os.Stdout.WriteString("Win\n" + chosen + "\n")
	}
}
