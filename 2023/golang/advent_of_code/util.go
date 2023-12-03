package main

import (
	"log"
	"os"
)

func Sum(array []int) int {
	sum := 0
	for _, val := range array {
		sum += val
	}
	return sum
}

func OpenFile(filePath string) *os.File {
	// open file
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}

	return file
}
