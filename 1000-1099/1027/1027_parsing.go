package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

// expression: characters allowed inside an arithmetic expression besides the brackets
const expression = "=+-*/0123456789\r\n"

func valid(s string) bool {
	depth := 0
	for i := 0; i < len(s); i++ {
		switch {
		case strings.HasPrefix(s[i:], "(*"):
			// a comment ends at the first *) after its opening pair
			end := strings.Index(s[i+2:], "*)")
			if end < 0 {
				return false
			}
			i += 2 + end + 1
		case s[i] == '(':
			depth++
		case s[i] == ')':
			if depth == 0 {
				return false
			}
			depth--
		case depth > 0 && !strings.ContainsRune(expression, rune(s[i])):
			return false
		}
	}
	return depth == 0
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	if valid(string(data)) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
