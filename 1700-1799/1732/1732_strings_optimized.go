package main

import (
	"bytes"
	"io/ioutil"
	"os"
)

func erase(span []byte) {
	for i, letter := range span {
		if letter != ' ' {
			span[i] = '_'
		}
	}
}

func fill(source, target []byte) bool {
	var prefix []uint32
	search, keptUntil := 0, 0
	for len(target) > 0 {
		word := target
		if end := bytes.IndexByte(target, ' '); end >= 0 {
			word, target = target[:end], target[end+1:]
		} else {
			target = nil
		}
		// Reuse the prefix table for the next word.
		if cap(prefix) < len(word) {
			size := 2 * cap(prefix)
			if size < len(word) {
				size = len(word)
			}
			prefix = make([]uint32, size)
		}
		matched := 0
		for i := 1; i < len(word); i++ {
			for matched > 0 && word[i] != word[matched] {
				matched = int(prefix[matched-1])
			}
			if word[i] == word[matched] {
				matched++
			}
			prefix[i] = uint32(matched)
		}

		matched = 0
		for search < len(source) {
			letter := source[search]
			search++
			for matched > 0 && letter != word[matched] {
				matched = int(prefix[matched-1])
			}
			if letter == word[matched] {
				matched++
				if matched == len(word) {
					break
				}
			}
		}
		if matched != len(word) {
			return false
		}
		// Leave a separator between successive kept words.
		erase(source[keptUntil : search-len(word)])
		keptUntil = search
		search++
	}
	erase(source[keptUntil:])
	return true
}

func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	end := bytes.IndexByte(data, '\n')
	if end < 0 {
		return
	}
	source := bytes.TrimSuffix(data[:end], []byte("\r"))
	target := bytes.TrimRight(data[end+1:], "\r\n")
	if !fill(source, target) {
		os.Stdout.WriteString("I HAVE FAILED!!!\n")
		return
	}
	os.Stdout.Write(append(source, '\n'))
}
