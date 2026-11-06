package main

import (
	"bufio"
	"os"
	"strconv"
)

const inputSize = 4096

func restore(word []byte, size int) []byte {
	modulus := size + 1
	weight := 0
	for i, ch := range word {
		if ch == '1' {
			weight += i + 1
		}
	}
	residue := weight % modulus
	switch {
	case len(word) == size:
		if residue != 0 {
			word[residue-1] = '0'
		}
	case len(word) < size:
		for i := len(word); i >= 0; i-- {
			if residue == 0 || residue+i+1 == modulus {
				digit := byte('0')
				if residue != 0 {
					digit = '1'
				}
				word = word[:len(word)+1]
				copy(word[i+1:], word[i:])
				word[i] = digit
				return word
			}
			if i > 0 && word[i-1] == '1' {
				residue++
				if residue == modulus {
					residue = 0
				}
			}
		}
	default:
		positionResidue := 0
		for i := len(word) - 1; i >= 0; i-- {
			digit := int(word[i] - '0')
			if residue == digit*positionResidue {
				copy(word[i:], word[i+1:])
				return word[:len(word)-1]
			}
			residue -= digit
			if residue < 0 {
				residue += modulus
			}
			positionResidue = i
		}
	}
	return word
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [inputSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	size, _ := strconv.Atoi(input.Text())
	word := make([]byte, size+1)
	output := bufio.NewWriter(os.Stdout)
	for input.Scan() {
		length := copy(word, input.Bytes())
		output.Write(restore(word[:length], size))
		output.WriteByte('\n')
	}
	output.Flush()
}
