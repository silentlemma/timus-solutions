package main

import (
	"bufio"
	"fmt"
	"os"
)

const small = 2

// freeLanguage is english, or else the first name of one or two letters that
// no team speaks: at most 100 teams cannot take all 702 of them.
func freeLanguage(spoken map[string]bool) string {
	if !spoken["english"] {
		return "english"
	}
	var names []string
	for a := 'a'; a <= 'z'; a++ {
		names = append(names, string(a))
	}
	for a := 'a'; a <= 'z'; a++ {
		for b := 'a'; b <= 'z'; b++ {
			names = append(names, string(a)+string(b))
		}
	}
	for _, name := range names {
		if !spoken[name] {
			return name
		}
	}
	return ""
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	langs := make([]string, n)
	distinct := map[string]bool{}
	for i := range langs {
		fmt.Fscan(in, &langs[i])
		distinct[langs[i]] = true
	}
	switch {
	case len(distinct) < n:
		// a third team would overhear two teams of one language
		if n == small {
			fmt.Fprintln(out, 0)
		} else {
			fmt.Fprintln(out, "Impossible")
		}
	case n == 1:
		fmt.Fprintln(out, 0)
	case n == small:
		fmt.Fprintln(out, 1)
		fmt.Fprintf(out, "%s-%s\n", langs[0], langs[1])
	default:
		// a talk through another team's language is overheard, so every talk
		// goes through a language no team speaks
		hub := freeLanguage(distinct)
		fmt.Fprintln(out, n)
		for _, lang := range langs {
			fmt.Fprintf(out, "%s-%s\n", lang, hub)
		}
	}
}
