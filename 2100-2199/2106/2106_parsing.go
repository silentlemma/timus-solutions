package main

import (
	"bufio"
	"encoding/hex"
	"io"
	"os"
	"strconv"
	"strings"
)

const (
	integerType = -1
	stringType  = -2
	integerSize = 4
	byteBase    = 256
)

type binaryReader struct {
	data   []byte
	offset int
}

func (reader *binaryReader) integer() uint64 {
	var value uint64
	for i := 0; i < integerSize; i++ {
		value = value*byteBase + uint64(reader.data[reader.offset])
		reader.offset++
	}
	return value
}

func (reader *binaryReader) text() string {
	length := int(reader.integer())
	value := string(reader.data[reader.offset : reader.offset+length])
	reader.offset += length
	return value
}

type frame struct {
	typeID int
	next   int
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Scan()
	header := strings.Fields(input.Text())
	typeCount, _ := strconv.Atoi(header[0])
	lineCount, _ := strconv.Atoi(header[1])
	names := make([]string, 0, typeCount)
	fields := make([][]int, 0, typeCount)
	typeIDs := make(map[string]int)
	for line := 0; line < lineCount; line++ {
		input.Scan()
		parts := strings.Fields(input.Text())
		if parts[0] == "struct" {
			typeIDs[parts[1]] = len(names)
			names = append(names, parts[1])
			fields = append(fields, nil)
			continue
		}
		fieldType := 0
		switch parts[0] {
		case "int":
			fieldType = integerType
		case "string":
			fieldType = stringType
		default:
			fieldType = typeIDs[parts[0]]
		}
		current := len(names) - 1
		fields[current] = append(fields[current], fieldType)
	}
	input.Scan()
	data, _ := hex.DecodeString(strings.TrimSpace(input.Text()))
	reader := binaryReader{data: data}
	var output strings.Builder
	stack := make([]frame, 0, typeCount)
	for reader.offset < len(reader.data) {
		root := int(reader.integer()) - 1
		output.WriteString(names[root])
		output.WriteByte('\n')
		stack = append(stack, frame{typeID: root})
		for len(stack) > 0 {
			top := len(stack) - 1
			current := &stack[top]
			if current.next == len(fields[current.typeID]) {
				stack = stack[:top]
				continue
			}
			fieldType := fields[current.typeID][current.next]
			current.next++
			output.WriteString(strings.Repeat(" ", len(stack)))
			switch fieldType {
			case integerType:
				output.WriteString("int ")
				output.WriteString(strconv.FormatUint(reader.integer(), 10))
			case stringType:
				output.WriteString("string ")
				output.WriteString(reader.text())
			default:
				output.WriteString(names[fieldType])
				stack = append(stack, frame{typeID: fieldType})
			}
			output.WriteByte('\n')
		}
	}
	io.WriteString(os.Stdout, output.String())
}
