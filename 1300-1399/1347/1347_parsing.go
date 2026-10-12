package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	openTag  = "<friend>"
	closeTag = "</friend>"
	endTag   = "</blog>"
)

// the name inside a friend tag, without other tags or spaces
func clean(inside string) string {
	var name strings.Builder
	tag := false
	for i := 0; i < len(inside); i++ {
		switch c := inside[i]; {
		case c == '<':
			tag = true
		case c == '>':
			tag = false
		case !tag:
			name.WriteByte(c)
		}
	}
	return strings.TrimSpace(name.String())
}

func sorted(set map[string]bool) []string {
	var list []string
	for s := range set {
		list = append(list, s)
	}
	sort.Strings(list)
	return list
}

type blog struct {
	name    string
	friends map[string]bool
}

func main() {
	raw, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	lines := strings.Split(string(raw), "\n")
	n, _ := strconv.Atoi(strings.TrimSpace(lines[0]))
	pos := 1
	var blogs []blog
	for b := 0; b < n; b++ {
		for strings.TrimSpace(lines[pos]) == "" {
			pos++
		}
		name := strings.TrimSpace(lines[pos])
		var text strings.Builder
		for pos++; ; pos++ {
			text.WriteString(lines[pos])
			text.WriteByte('\n')
			if strings.Contains(lines[pos], endTag) {
				break
			}
		}
		pos++
		friends := map[string]bool{}
		body := text.String()
		for {
			at := strings.Index(body, openTag)
			if at < 0 {
				break
			}
			body = body[at+len(openTag):]
			stop := strings.Index(body, closeTag)
			if friend := clean(body[:stop]); friend != "" && friend != name {
				friends[friend] = true
			}
			body = body[stop+len(closeTag):]
		}
		blogs = append(blogs, blog{name, friends})
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for b, x := range blogs {
		readers, both := map[string]bool{}, map[string]bool{}
		for _, other := range blogs {
			if other.name != x.name && other.friends[x.name] {
				readers[other.name] = true
				if x.friends[other.name] {
					both[other.name] = true
				}
			}
		}
		if b > 0 {
			out.WriteString("\n")
		}
		out.WriteString(x.name + "\n")
		for g, group := range []map[string]bool{x.friends, readers, both} {
			out.WriteString(strconv.Itoa(g+1) + ": " + strings.Join(sorted(group), ", ") + "\n")
		}
	}
}
