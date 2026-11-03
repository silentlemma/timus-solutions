package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const maxWordLength = 50
const keypad = "22233344115566070778889990"

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for in.Scan() {
		phone := in.Text()
		if phone == "-1" {
			break
		}
		in.Scan()
		count, _ := strconv.Atoi(in.Text())
		n := len(phone)
		edges := make([][10]int32, n*maxWordLength+1)
		words := make([]string, len(edges))
		nodes := int32(1)
		// Restrict the trie to phone substrings before reading the dictionary.
		// unrelated words then need neither nodes nor retained strings.
		for start := 0; start < n; start++ {
			node := int32(0)
			for end := start; end < n && end < start+maxWordLength; end++ {
				digit := phone[end] - '0'
				if edges[node][digit] == 0 {
					edges[node][digit] = nodes
					nodes++
				}
				node = edges[node][digit]
			}
		}
		for i := 0; i < count; i++ {
			in.Scan()
			word := in.Bytes()
			node := int32(0)
			for _, letter := range word {
				node = edges[node][keypad[letter-'a']-'0']
				if node == 0 {
					break
				}
			}
			if node != 0 && words[node] == "" {
				words[node] = string(word)
			}
		}
		best, how := make([]int, n+1), make([]int32, n+1)
		for i := 1; i <= n; i++ {
			best[i] = n + 1
		}
		for start := 0; start < n; start++ {
			if best[start] > n {
				continue
			}
			node := int32(0)
			for end := start; end < n && end < start+maxWordLength; end++ {
				node = edges[node][phone[end]-'0']
				if words[node] != "" && best[start]+1 < best[end+1] {
					best[end+1], how[end+1] = best[start]+1, node
				}
			}
		}
		if best[n] > n {
			fmt.Fprintln(out, "No solution.")
			continue
		}
		answer := make([]string, 0, best[n])
		for position := n; position > 0; {
			word := words[how[position]]
			answer = append(answer, word)
			position -= len(word)
		}
		for i, j := 0, len(answer)-1; i < j; i, j = i+1, j-1 {
			answer[i], answer[j] = answer[j], answer[i]
		}
		fmt.Fprintln(out, strings.Join(answer, " "))
	}
}
