package quiz

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func GetQuiz(book string, chapter int) string {

	filename := filepath.Join(
		"data", "quizzes", book,
		fmt.Sprintf("%s-%d.json", strings.ToLower(book), chapter),
	)

	file, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	return string(file)
}
