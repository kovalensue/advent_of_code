package main

import (
	"fmt"
)

func main() {
	fmt.Println("Advent of Code 2023")
	fmt.Println("===================================================================")
	fmt.Println("Puzzle #1:", Puzzle1("puzzle_1.txt"))

	validGamesSum, powersSum := Puzzle2("puzzle_2.txt")
	fmt.Println("Puzzle #2:", validGamesSum, "Puzzle #2a:", powersSum)

	fmt.Println("Puzzle #1a:", Puzzle1a("puzzle_1.txt"))
	fmt.Println("Puzzle #3:", Puzzle3("puzzle_3.txt"))
	fmt.Println("Puzzle #4:", Puzzle4("puzzle_4.txt"))
}
