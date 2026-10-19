package main

import (
	"bufio"
	"io"
	"os"
)

const (
	ioBufferSize = 65536
	maxQueries   = 100000
	maxChanges   = 100000
	asciiSpace   = ' '
	asciiZero    = '0'
)

type fastInput struct {
	reader   io.Reader
	buffer   [ioBufferSize]byte
	position int
	length   int
}

func (input *fastInput) nextByte() byte {
	if input.position == input.length {
		input.length, _ = input.reader.Read(input.buffer[:])
		input.position = 0
		if input.length == 0 {
			return 0
		}
	}
	character := input.buffer[input.position]
	input.position++
	return character
}

func (input *fastInput) nextInt() int32 {
	character := input.nextByte()
	for character <= asciiSpace {
		character = input.nextByte()
	}
	var value int32
	for character > asciiSpace {
		value = value*10 + int32(character-asciiZero)
		character = input.nextByte()
	}
	return value
}

func writeInt(output *bufio.Writer, value int32) {
	var digits [10]byte
	position := len(digits)
	for {
		position--
		digits[position] = byte(value%10) + asciiZero
		value /= 10
		if value == 0 {
			break
		}
	}
	output.Write(digits[position:])
}

type change struct {
	day   int32
	count int32
	step  int32
	value int32
}

type query struct {
	day  int32
	next int32
}

func main() {
	input := fastInput{reader: os.Stdin}
	days := input.nextInt()
	friends := input.nextInt()
	plan := make([]int32, days)
	for day := range plan {
		plan[day] = input.nextInt()
	}

	firstChild := make([]int32, friends+1)
	nextSibling := make([]int32, friends+1)
	firstQuery := make([]int32, friends+1)
	changeBegin := make([]int32, friends+2)
	answerBegin := make([]int32, friends+2)
	for version := range firstChild {
		firstChild[version] = -1
		nextSibling[version] = -1
		firstQuery[version] = -1
	}
	changes := make([]change, 0, maxChanges)
	queries := make([]query, 0, maxQueries)
	totalAssignments := 0

	for person := int32(1); person <= friends; person++ {
		answerBegin[person] = int32(len(queries))
		questionCount := input.nextInt()
		for question := int32(0); question < questionCount; question++ {
			version := input.nextInt()
			day := input.nextInt() - 1
			queries = append(queries, query{day, firstQuery[version]})
			firstQuery[version] = int32(len(queries)) - 1
		}

		parent := input.nextInt()
		nextSibling[person] = firstChild[parent]
		firstChild[parent] = person
		changeCount := input.nextInt()
		changeBegin[person] = int32(len(changes))
		for index := int32(0); index < changeCount; index++ {
			day := input.nextInt() - 1
			count := input.nextInt()
			step := input.nextInt()
			value := input.nextInt()
			changes = append(changes, change{day, count, step, value})
			totalAssignments += int(count)
		}
	}
	changeBegin[friends+1] = int32(len(changes))
	answerBegin[friends+1] = int32(len(queries))

	answers := make([]int32, len(queries))
	history := make([]int32, totalAssignments)
	historySize := 0
	events := make([]int32, 1, friends+1)
	events[0] = 1

	// Each exit reverses every write, including repeated writes to the same day.
	for len(events) != 0 {
		last := len(events) - 1
		event := events[last]
		events = events[:last]
		if event > 0 {
			version := event - 1
			for index := changeBegin[version]; index < changeBegin[version+1]; index++ {
				current := changes[index]
				day := current.day
				for left := current.count; left != 0; left-- {
					history[historySize] = plan[day]
					historySize++
					plan[day] = current.value
					day += current.step
				}
			}
			for index := firstQuery[version]; index != -1; index = queries[index].next {
				answers[index] = plan[queries[index].day]
			}
			events = append(events, -event)
			for child := firstChild[version]; child != -1; child = nextSibling[child] {
				events = append(events, child+1)
			}
		} else {
			version := -event - 1
			for index := changeBegin[version+1]; index > changeBegin[version]; {
				index--
				current := changes[index]
				day := current.day + (current.count-1)*current.step
				for left := current.count; left != 0; left-- {
					historySize--
					plan[day] = history[historySize]
					day -= current.step
				}
			}
		}
	}

	output := bufio.NewWriterSize(os.Stdout, ioBufferSize)
	for person := int32(1); person <= friends; person++ {
		for index := answerBegin[person]; index < answerBegin[person+1]; index++ {
			if index != answerBegin[person] {
				output.WriteByte(' ')
			}
			writeInt(output, answers[index])
		}
		output.WriteByte('\n')
	}
	output.Flush()
}
