package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

type folder map[string]folder

func print(f folder, depth int, w *bufio.Writer) {
	names := make([]string, 0, len(f))
	for name := range f {
		names = append(names, name)
	}
	sort.Strings(names)
	for _, name := range names {
		w.WriteString(strings.Repeat(" ", depth))
		w.WriteString(name)
		w.WriteByte('\n')
		print(f[name], depth+1, w)
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var n int
	fmt.Fscan(in, &n)
	root := folder{}
	for i := 0; i < n; i++ {
		var path string
		fmt.Fscan(in, &path)
		cur := root
		for _, name := range strings.Split(path, "\\") {
			next, ok := cur[name]
			if !ok {
				next = folder{}
				cur[name] = next
			}
			cur = next
		}
	}
	// subfolders are sorted by name, not as parts of a full path
	print(root, 0, w)
}
