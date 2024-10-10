package main

import (
	"bible-quizzer/src/quiz"
	"fmt"
)

func main() {
	q := quiz.GetQuiz("Exodus", 1)
	fmt.Println(q)
}
