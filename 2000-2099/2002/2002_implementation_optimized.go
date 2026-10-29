package main

import (
	"bufio"
	"os"
)

const maxTokenLength = 30

type account struct {
	password string
	online   bool
}

const bufferSize = 1024

// the requests are parsed by hand from a 1 KB buffered reader and answered
// at once through a buffered writer, with no list of commands
type input struct {
	reader *bufio.Reader
}

func (in input) nextInt() int64 {
	ch, err := in.reader.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = in.reader.ReadByte()
	}
	var value int64
	for err == nil && ch >= '0' && ch <= '9' {
		value = value*10 + int64(ch-'0')
		ch, err = in.reader.ReadByte()
	}
	return value
}

func (in input) nextToken() string {
	var token [maxTokenLength]byte
	length := 0
	ch, err := in.reader.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = in.reader.ReadByte()
	}
	for err == nil && ch > ' ' {
		token[length] = ch
		length++
		ch, err = in.reader.ReadByte()
	}
	return string(token[:length])
}

func main() {
	in := input{bufio.NewReaderSize(os.Stdin, bufferSize)}
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer out.Flush()
	count := in.nextInt()
	accounts := make(map[string]account)
	for i := int64(0); i < count; i++ {
		action, name := in.nextToken(), in.nextToken()
		password := ""
		if action != "logout" {
			password = in.nextToken()
		}
		entry, exists := accounts[name]
		var reply string
		if action == "register" {
			if exists {
				reply = "fail: user already exists"
			} else {
				accounts[name] = account{password: password}
				reply = "success: new user added"
			}
		} else if action == "login" {
			if !exists {
				reply = "fail: no such user"
			} else if entry.password != password {
				reply = "fail: incorrect password"
			} else if entry.online {
				reply = "fail: already logged in"
			} else {
				entry.online = true
				accounts[name] = entry
				reply = "success: user logged in"
			}
		} else {
			if !exists {
				reply = "fail: no such user"
			} else if !entry.online {
				reply = "fail: already logged out"
			} else {
				entry.online = false
				accounts[name] = entry
				reply = "success: user logged out"
			}
		}
		out.WriteString(reply)
		out.WriteByte('\n')
	}
}
