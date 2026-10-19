package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const roleCount = 3

func transform(sentence string) string {
	opening, closing := "{([", "})]"
	results := make([]string, 0)
	for _, clause := range strings.Split(strings.ToLower(sentence), ",") {
		var phrases [roleCount]string
		prefix := ""
		for i := 0; i < len(clause); {
			role := strings.IndexByte(opening, clause[i])
			if role >= 0 {
				end := i + 1
				for clause[end] != closing[role] {
					end++
				}
				phrases[role] = clause[i+1 : end]
				i = end + 1
			} else if clause[i] >= 'a' && clause[i] <= 'z' {
				begin := i
				for i < len(clause) && clause[i] >= 'a' && clause[i] <= 'z' {
					i++
				}
				prefix = clause[begin:i]
			} else {
				i++
			}
		}
		phrase := strings.Join(phrases[:], " ")
		if prefix != "" {
			phrase = prefix + " " + phrase
		}
		results = append(results, phrase)
	}
	answer := strings.Join(results, ", ")
	return strings.ToUpper(answer[:1]) + answer[1:]
}
func main() {
	input := bufio.NewReader(os.Stdin)
	sentence, _ := input.ReadString('\n')
	fmt.Println(transform(strings.TrimSpace(sentence)))
}
