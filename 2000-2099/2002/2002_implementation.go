package main

import (
	"bufio"
	"fmt"
	"os"
)

type Account struct {
	password string
	online   bool
}

func process(commands [][]string) []string {
	accounts := make(map[string]*Account)
	replies := make([]string, 0, len(commands))
	for _, command := range commands {
		action, name := command[0], command[1]
		account := accounts[name]
		reply := ""
		if action == "register" {
			if account != nil {
				reply = "fail: user already exists"
			} else {
				accounts[name] = &Account{password: command[2]}
				reply = "success: new user added"
			}
		} else if action == "login" {
			if account == nil {
				reply = "fail: no such user"
			} else if account.password != command[2] {
				reply = "fail: incorrect password"
			} else if account.online {
				reply = "fail: already logged in"
			} else {
				account.online = true
				reply = "success: user logged in"
			}
		} else {
			if account == nil {
				reply = "fail: no such user"
			} else if !account.online {
				reply = "fail: already logged out"
			} else {
				account.online = false
				reply = "success: user logged out"
			}
		}
		replies = append(replies, reply)
	}
	return replies
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var count int
	fmt.Fscan(in, &count)
	commands := make([][]string, count)
	for i := range commands {
		var action, name, password string
		fmt.Fscan(in, &action, &name)
		commands[i] = []string{action, name}
		if action != "logout" {
			fmt.Fscan(in, &password)
			commands[i] = append(commands[i], password)
		}
	}
	for _, reply := range process(commands) {
		fmt.Fprintln(out, reply)
	}
}
