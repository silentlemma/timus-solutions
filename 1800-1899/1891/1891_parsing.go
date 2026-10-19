package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const callPrefix = 3

func words(line string) []string {
	return strings.FieldsFunc(line, func(letter rune) bool {
		return !((letter >= 'a' && letter <= 'z') || (letter >= 'A' && letter <= 'Z'))
	})
}

func signature(name string, arguments []string) string {
	return name + ":" + strings.Join(arguments, ",")
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	in.Scan()
	functionCount, _ := strconv.Atoi(in.Text())
	functions := make(map[string]string)
	for i := 0; i < functionCount; i++ {
		in.Scan()
		tokens := words(in.Text())
		functions[signature(tokens[0], tokens[1:len(tokens)-1])] = tokens[len(tokens)-1]
	}
	in.Scan()
	lineCount, _ := strconv.Atoi(in.Text())
	variables := make(map[string]string)
	var inferred strings.Builder
	for number := 1; number <= lineCount; number++ {
		in.Scan()
		tokens := words(in.Text())
		declared, name, function := tokens[0], tokens[1], tokens[2]
		error := ""
		argumentTypes := make([]string, 0, len(tokens)-callPrefix)
		if _, exists := variables[name]; exists {
			error = "Double declaration"
		} else {
			for _, argument := range tokens[callPrefix:] {
				valueType, exists := variables[argument]
				if !exists {
					error = "Unknown variable"
					break
				}
				argumentTypes = append(argumentTypes, valueType)
			}
		}
		if error == "" {
			result, exists := functions[signature(function, argumentTypes)]
			if !exists {
				error = "No such function"
			} else if declared != "auto" && declared != result {
				error = "Invalid initialization"
			} else {
				variables[name] = result
				if declared == "auto" {
					fmt.Fprintf(&inferred, "%s : %s\n", name, result)
				}
			}
		}
		if error != "" {
			fmt.Fprintf(out, "Error on line %d: %s\n", number, error)
			return
		}
	}
	fmt.Fprint(out, inferred.String())
}
