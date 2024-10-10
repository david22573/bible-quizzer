package quiz

type Quiz struct {
	Book          string `json:"book"`
	Chapter       int    `json:"chapter"`
	QuizStructure struct {
		TotalQuestions int `json:"total_questions"`
		Sections       []struct {
			Name          string   `json:"name"`
			Count         int      `json:"count"`
			QuestionTypes []string `json:"question_types"`
			Questions     []struct {
				Question struct {
					Text          string   `json:"text"`
					Options       []string `json:"options"`
					CorrectAnswer int      `json:"correct_answer"`
				} `json:"question"`
			} `json:"questions"`
		} `json:"sections"`
	} `json:"quiz_structure"`
	KeyThemes []string `json:"key_themes"`
	KeyVerses []struct {
		Reference string `json:"reference"`
	} `json:"key_verses"`
	Characters []struct {
		Name string `json:"name"`
		Role string `json:"role"`
	} `json:"characters"`
	Events []struct {
		Description string `json:"description"`
		Location    string `json:"location"`
	} `json:"events"`
	Concepts        []string `json:"concepts"`
	CrossReferences struct {
		OldTestament []struct {
			Reference   string `json:"reference"`
			Description string `json:"description"`
		} `json:"Old Testament"`
		NewTestament []struct {
			Reference   string `json:"reference"`
			Description string `json:"description"`
		} `json:"New Testament"`
	} `json:"cross_references"`
}
