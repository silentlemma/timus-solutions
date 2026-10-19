package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

type reader struct {
	data     []byte
	position int
}

func (r *reader) token() []byte {
	for r.position < len(r.data) && r.data[r.position] <= ' ' {
		r.position++
	}
	begin := r.position
	for r.position < len(r.data) && r.data[r.position] > ' ' {
		r.position++
	}
	return r.data[begin:r.position]
}
func (r *reader) number() int {
	value := 0
	for _, digit := range r.token() {
		value = 10*value + int(digit-'0')
	}
	return value
}
func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := reader{data: data}
	count := input.number()
	input.number()
	value, previous := make([]int32, count+2), make([]int32, count+2)
	learned, redo := make([]int32, count+2), make([]int32, count+2)
	used, entities := int32(0), 1
	output := make([]byte, 0)
	for step := 0; step < count; step++ {
		command := input.token()
		entity := input.number()
		switch string(command) {
		case "learn":
			used++
			value[used] = int32(input.number())
			previous[used] = learned[entity]
			learned[entity] = used
			redo[entity] = 0
		case "rollback":
			head := learned[entity]
			used++
			value[used] = value[head]
			previous[used] = redo[entity]
			learned[entity] = previous[head]
			redo[entity] = used
		case "relearn":
			head := redo[entity]
			used++
			value[used] = value[head]
			previous[used] = learned[entity]
			redo[entity] = previous[head]
			learned[entity] = used
		case "clone":
			entities++
			learned[entities] = learned[entity]
			redo[entities] = redo[entity]
		default:
			head := learned[entity]
			if head == 0 {
				output = append(output, "basic\n"...)
			} else {
				output = strconv.AppendInt(output, int64(value[head]), 10)
				output = append(output, '\n')
			}
		}
	}
	os.Stdout.Write(output)
}
