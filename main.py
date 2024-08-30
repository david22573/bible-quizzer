from app.utils.helpers import ask_ai
import json


with open("data/quiz-template.json") as f:
    outline = json.load(f)

    print(outline)


def generate_quiz(book, chapter):
    instruction = (
        f"Generate JSON(prettier formatted, completely) for {book} chapter {chapter} from the Bible"
        + " following this template. Please fill in the fields with"
        + " relevant data based on the chapter content, including the quiz structure,"
        + " questions, and options. The JSON should be as follows:"
    )
    ask_ai(f"{instruction}\n{outline}?")


def main():
    generate_quiz("Genesis", 2)
    pass


if __name__ == "__main__":
    main()
