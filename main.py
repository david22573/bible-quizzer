from app.utils.helpers import ask_ai
import json


with open("data/quiz-template.json") as f:
    outline = json.load(f)

    print(outline)


def generate_quiz(book, chapter):
    instruction = (
        f"Generate JSON(VALID AND COMPLETE) for {book} chapter {chapter} from the Bible"
        + " following this template. Please fill in the fields with"
        + " relevant data based on the chapter content, including the quiz structure,"
        + " questions, and options. Do not add anything else but the json please. The JSON should be as follows:"
    )
    return ask_ai(f"{instruction}\n{outline}?")


def read_json(path):
    with open(path) as f:
        return json.loads(f.read())


def write_json(path, data):
    with open(path, "w+") as f:
        data = json.loads(data)
        json.dump(data, f, indent=4)


def main():
    book, chapter = "Genesis", 3
    data = generate_quiz(book, chapter)
    write_json(f"data/{book.lower()}-{chapter}.json", data)


if __name__ == "__main__":
    main()
