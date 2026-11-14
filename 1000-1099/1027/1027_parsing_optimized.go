package main

import "syscall"

const blockSize = 512

func valid() bool {
	var block [blockSize]byte
	depth := 0
	open, comment, star := false, false, false
	for {
		count, err := syscall.Read(syscall.Stdin, block[:])
		if err == syscall.EINTR {
			continue
		}
		if err != nil {
			return false
		}
		if count == 0 {
			break
		}
		for _, c := range block[:count] {
			if comment {
				if star && c == ')' {
					comment = false
				}
				star = c == '*'
				continue
			}
			// A pending '(' can start either an expression or a comment.
			if open {
				open = false
				if c == '*' {
					comment, star = true, false
					continue
				}
				depth++
			}
			switch c {
			case '(':
				open = true
			case ')':
				if depth == 0 {
					return false
				}
				depth--
			case '=', '+', '-', '*', '/', '\r', '\n':
			default:
				if depth > 0 && (c < '0' || c > '9') {
					return false
				}
			}
		}
	}
	return depth == 0 && !open && !comment
}

func main() {
	answer := []byte("NO\n")
	if valid() {
		answer = []byte("YES\n")
	}
	for len(answer) > 0 {
		n, err := syscall.Write(syscall.Stdout, answer)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		answer = answer[n:]
	}
}
