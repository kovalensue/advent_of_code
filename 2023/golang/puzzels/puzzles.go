package puzzels

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func sum(array []int) int {
	sum := 0
	for _, val := range array {
		sum += val
	}
	return sum
}

func openFile(filePath string) *os.File {
	// open file
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}

	return file
}

func Puzzle1() int {

	file := openFile("/home/kovalikt/git/personal/advent_of_code/2023/golang/resources/puzzle_1.txt")

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

	return sum(calibrationNumber)
}

func Puzzle1a() int {

	file := openFile("/home/kovalikt/git/personal/advent_of_code/2023/golang/resources/puzzle_1a.txt")

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
		re := regexp.MustCompile("[0-9]{1}|(one|two|three|four|five|six|seven|eight|nine)")
		numbers := re.FindAllString(fileScanner.Text(), -1)

		firstDigit, ok := digitMap[numbers[0]]
		if !ok {
			firstDigit = numbers[0]
		}
		secondDigit, ok := digitMap[numbers[len(numbers)-1]]
		if !ok {
			secondDigit = numbers[len(numbers)-1]
		}

		extractedNumber, err := strconv.Atoi(firstDigit + secondDigit)
		fmt.Println("extracted number: ", extractedNumber, "string: ", fileScanner.Text())
		if err != nil {
			log.Fatal(err, fmt.Sprintf("no number found in - %s", numbers))
		}

		result = append(result, extractedNumber)
	}

	// close file
	file.Close()

	return sum(result)

}
