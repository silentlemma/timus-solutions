package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

const (
	logPrefixLength = 11
	maxExponent     = 30
	adminName       = "admin"
	commandPrefix   = ": /"
	comparisonJoin  = ">-<"
)

type player struct {
	gl     int64
	hf     int64
	online bool
}

func messageBody(command string) string {
	separator := strings.IndexByte(command, ' ')
	if separator < 0 {
		return ""
	}
	return command[separator+1:]
}

func messageCounts(message string) (int64, int64) {
	var gl, hf int64
	for i := 0; i < len(message); i += 2 {
		if message[i] == 'g' {
			gl++
		} else {
			hf++
		}
	}
	return gl, hf
}

// A^g = B^f exactly when both are powers of one root with matching
// exponents; a base of 1 contributes nothing.
var (
	related   = true
	scaleGood int64
	scaleFun  int64
)

// perfectPower writes value as root^exponent with the largest exponent.
func perfectPower(value int64) (int64, int64) {
	for exponent := int64(maxExponent); exponent > 1; exponent-- {
		guess := int64(math.Round(math.Pow(float64(value), 1/float64(exponent))))
		root := guess - 1
		if root < 2 {
			root = 2
		}
		for ; root <= guess+1; root++ {
			power := int64(1)
			for i := int64(0); i < exponent && power <= value; i++ {
				power *= root
			}
			if power == value {
				return root, exponent
			}
		}
	}
	return value, 1
}

func compare(first, second *player, name string, explicit bool, logA, logB float64) string {
	// The common public-message counts cancel for two online players.
	good, fun := first.gl-second.gl, first.hf-second.hf
	equal := good == 0 && fun == 0
	if related {
		equal = good*scaleGood == fun*scaleFun
	}
	if equal {
		if explicit {
			return "Their luck is equal"
		}
		return name + " is good"
	}
	if float64(good)*logA-float64(fun)*logB > 0 {
		return name + " is a loser"
	}
	return name + " is a lucky guy"
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Scan()
	var count, messageLimit int
	var a, b float64
	fmt.Sscan(input.Text(), &count, &messageLimit, &a, &b)
	logA, logB := math.Log(a), math.Log(b)
	if a > 1 {
		scaleGood = 1
	}
	if b > 1 {
		scaleFun = 1
	}
	if a > 1 && b > 1 {
		goodRoot, goodExponent := perfectPower(int64(a))
		funRoot, funExponent := perfectPower(int64(b))
		related = goodRoot == funRoot
		scaleGood, scaleFun = goodExponent, funExponent
	}
	players := map[string]*player{adminName: {online: true}}
	var globalGL, globalHF int64
	online := 1
	var output strings.Builder

	for commandIndex := 0; commandIndex < count && input.Scan(); commandIndex++ {
		line := input.Text()[logPrefixLength:]
		separator := strings.Index(line, commandPrefix)
		author := line[:separator]
		command := line[separator+len(commandPrefix):]
		var answer string

		switch command[0] {
		case 'j':
			current := players[author]
			if current == nil {
				current = &player{}
				players[author] = current
			}
			if current.online {
				answer = "Failed: " + author + " is already on the server"
			} else {
				current.gl -= globalGL
				current.hf -= globalHF
				current.online = true
				online++
				answer = "Successful"
			}
		case 'q':
			current := players[author]
			current.gl += globalGL
			current.hf += globalHF
			current.online = false
			online--
			answer = "Successful"
		case 'o':
			answer = fmt.Sprintf("There are %d players on the server", online)
		case 's':
			message := messageBody(command)
			gl, hf := messageCounts(message)
			globalGL += gl
			globalHF += hf
			players[author].gl -= gl
			players[author].hf -= hf
			answer = author + ": " + message
		case 'w':
			left := strings.IndexByte(command, '<')
			right := strings.IndexByte(command, '>')
			recipient := command[left+1 : right]
			message := messageBody(command)
			if target := players[recipient]; target != nil && target.online {
				gl, hf := messageCounts(message)
				target.gl += gl
				target.hf += hf
			}
			answer = author + " (to " + recipient + "): " + message
		case 'c':
			if author != adminName {
				answer = "Failed: you have no such rights"
				break
			}
			left := strings.IndexByte(command, '<')
			right := strings.IndexByte(command, '>')
			firstName := command[left+1 : right]
			secondName := firstName
			explicit := right+1 < len(command)
			if explicit {
				secondName = command[right+len(comparisonJoin) : len(command)-1]
			} else {
				firstName = adminName
			}
			first, second := players[firstName], players[secondName]
			if first == nil || !first.online {
				answer = "Failed: " + firstName + " is not on the server"
			} else if second == nil || !second.online {
				answer = "Failed: " + secondName + " is not on the server"
			} else {
				answer = compare(first, second, secondName, explicit, logA, logB)
			}
		}
		output.WriteString(answer)
		output.WriteByte('\n')
	}
	fmt.Print(output.String())
}
