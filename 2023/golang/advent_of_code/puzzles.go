package main

import (
	"bufio"
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func Puzzle1(inputFile string) int {

	file := OpenFile("/home/kovalikt/git/personal/advent_of_code/2023/golang/resources/" + inputFile)

	// initialize new Scanner and split file to lines
	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var calibrationNumber []int

	// loop through scanner and print each token
	for fileScanner.Scan() {
		re := regexp.MustCompile("[0-9]{1}")
		numbers := re.FindAllString(fileScanner.Text(), -1)

		extractedNumber, err := strconv.Atoi(numbers[0] + numbers[len(numbers)-1])
		if err != nil {
			log.Fatal(err, fmt.Sprintf("no number found in - %s", numbers))
		}

		calibrationNumber = append(calibrationNumber, extractedNumber)
	}

	// close file
	file.Close()

	return Sum(calibrationNumber)
}

func Puzzle1a(inputFile string) int {

	file := OpenFile("/home/kovalikt/git/personal/advent_of_code/2023/golang/resources/" + inputFile)

	// initialize new Scanner and split file to lines
	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var result []int
	digitMap := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	// loop through scanner and print each token
	for fileScanner.Scan() {
		var numbers []string

		re := regexp.MustCompile("[0-9]{1}|(one|two|three|four|five|six|seven|eight|nine){1}")
		line := fileScanner.Text()
		loc := re.FindStringIndex(line)
		for loc != nil {
			//fmt.Println(loc, line)
			numbers = append(numbers, line[loc[0]:loc[1]])
			if loc[1] > 1 {
				line = line[loc[1]-1:] // if end of match is bigger than one whe go back one more index to cover text number overlaps
			} else {
				line = line[loc[1]:]
			}
			//fmt.Println("new line:", line)
			loc = re.FindStringIndex(line)
		}

		firstDigit, ok := digitMap[numbers[0]]
		if !ok {
			firstDigit = numbers[0]
		}
		secondDigit, ok := digitMap[numbers[len(numbers)-1]]
		if !ok {
			secondDigit = numbers[len(numbers)-1]
		}

		extractedNumber, err := strconv.Atoi(firstDigit + secondDigit)
		//fmt.Println("extracted number: ", extractedNumber, "string: ", fileScanner.Text())
		if err != nil {
			log.Fatal(err, fmt.Sprintf("no number found in - %s", numbers))
		}

		result = append(result, extractedNumber)
	}

	// close file
	file.Close()

	return Sum(result)
}

func Puzzle2(inputFile string) int {

	CubesCount := map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}

	file := OpenFile("/home/kovalikt/git/personal/advent_of_code/2023/golang/resources/" + inputFile)

	// initialize new Scanner and split file to lines
	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var validGames []int

	for fileScanner.Scan() {
		line := fileScanner.Text()
		splitedLine := strings.Split(line, ":")
		gameId, err := strconv.Atoi(strings.Split(splitedLine[0], " ")[1])
		gameIsPossible := true

		if err != nil {
			log.Fatal(err)
		}

		for _, hand := range strings.Split(splitedLine[1], ";") {
			//fmt.Println(hand)
			for _, cube := range strings.Split(hand, ",") {
				//fmt.Println(cube)
				cubeNum := strings.Trim(strings.Split(cube, " ")[1], " ")
				//fmt.Println("cube num:", cubeNum)
				cubeColor := strings.Trim(strings.Split(cube, " ")[2], " ")
				//fmt.Println("cube color:", cubeColor)
				cubeNumInt, err := strconv.Atoi(cubeNum)

				if err != nil {
					log.Fatal(err)
				}

				if cubeNumInt > CubesCount[cubeColor] {
					gameIsPossible = false
					break
				}
				//fmt.Println(cubeNumInt, CubesCount[cubeColor])
			}

			if !gameIsPossible {
				break
			}
		}

		if gameIsPossible {
			validGames = append(validGames, gameId)
		}
	}
	return Sum(validGames)
}
