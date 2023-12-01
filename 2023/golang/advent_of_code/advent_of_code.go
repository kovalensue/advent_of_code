package main

import (
	"fmt"
	"puzzels"
	"regexp"
)

func main() {
	fmt.Println("Advent of Code 2023")
	fmt.Println("===================================================================")
	fmt.Println("Puzzle #1:", puzzels.Puzzle1())
	fmt.Println("Puzzle #1:", puzzels.Puzzle1a())

	// positive lookahead tests
	re := regexp.MustCompile("(?=(seven|nine))")
	numbers := re.FindAllString("sevenine", -1)
	fmt.Println(numbers)
}
