package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

const maxLine = 250

func main() {
	in := bufio.NewReader(os.Stdin)
	readLine := func() string {
		line, _ := in.ReadString('\n')
		return strings.TrimRight(line, "\r\n")
	}
	n, _ := strconv.Atoi(strings.TrimSpace(readLine()))
	known := make(map[string][]uint32, n)
	ids := make(map[string]uint32)
	var names []string
	for i := 0; i < n; i++ {
		line := readLine()
		colon := strings.IndexByte(line, ':')
		list := known[line[:colon]]
		for _, word := range strings.Fields(line[colon+1:]) {
			id, exists := ids[word]
			if !exists {
				id = uint32(len(names))
				ids[word] = id
				names = append(names, word)
			}
			list = append(list, id)
		}
		sort.Slice(list, func(i, j int) bool { return list[i] < list[j] })
		used := 0
		for _, id := range list {
			if used == 0 || list[used-1] != id {
				list[used] = id
				used++
			}
		}
		known[line[:colon]] = list[:used]
	}
	m, _ := strconv.Atoi(strings.TrimSpace(readLine()))
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	common := make([]uint32, 0, maxLine/2)
	result := make([]string, 0, maxLine/2)
	for query := 0; query < m; query++ {
		group := strings.Fields(readLine())
		seed := known[group[0]]
		for _, name := range group {
			if len(known[name]) < len(seed) {
				seed = known[name]
			}
		}
		common = append(common[:0], seed...)
		for _, name := range group {
			if len(common) == 0 {
				break
			}
			other := known[name]
			left, right, used := 0, 0, 0
			for left < len(common) && right < len(other) {
				if common[left] < other[right] {
					left++
				} else if other[right] < common[left] {
					right++
				} else {
					common[used] = common[left]
					used++
					left++
					right++
				}
			}
			common = common[:used]
		}
		if len(common) == 0 {
			out.WriteString("No solution.\n")
			continue
		}
		result = result[:0]
		for _, id := range common {
			result = append(result, names[id])
		}
		sort.Strings(result)
		out.WriteString(strings.Join(result, " "))
		out.WriteByte('\n')
	}
}
