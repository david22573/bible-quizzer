import time
from app.utils.helpers import ask_ai
import json


class QuizGenerator:
    def __init__(self, book, chapter):
        self.book = book
        self.chapter = chapter

        with open("data/quiz-template.json") as f:
            self.outline = json.load(f)

    def get_instructions(self):
        with open("./data/prompt.txt") as f:
            instructions = f.read()
        instructions = instructions.replace("{book}", self.book)
        instructions = instructions.replace("{chapter}", str(self.chapter))
        return instructions

    def generate(self):
        prompt_path = "./data/prompt.txt"
        data = ask_ai(prompt_path)
        file_path = f"data/{self.book}/{self.book.lower()}-{self.chapter}.json"
        self.write_json(file_path, data)

    def write_json(self, path, data):
        with open(path, "w+", encoding="utf-8") as f:
            data = json.loads(data, strict=False)
            json.dump(data, f, indent=4)


def generate_book(book, ch_nums):
    chapters = [i for i in range(1, ch_nums + 1)]
    for chapter in chapters:
        try:
            qzgen = QuizGenerator(book, chapter)
            print(f"Generating {book} chapter {chapter}")
            qzgen.generate()
            if chapter != chapters[-1]:
                time.sleep(60 * 1)
            print(f"Finished {book} chapter {chapter}")
        except Exception as e:
            print(f"Error generating {book} chapter {chapter}")
            print(e)
            pass


def generate_chapter(book, chapter):
    qzgen = QuizGenerator(book, chapter)
    print(f"Generating {book} chapter {chapter}")
    qzgen.generate()
    print(f"Finished {book} chapter {chapter}")


def generate_missing_chapters():
    with open("./data/missing_chapters.txt") as f:
        missing_chapters = f.readlines()

    for chapter in missing_chapters:
        chapter = chapter.strip()[:-5]
        book, chapter = chapter.split("-")
        qzgen = QuizGenerator(book.capitalize(), chapter)
        print(f"Generating {book} chapter {chapter}")
        qzgen.generate()
        print(f"Finished {book} chapter {chapter}")


def main():
    pass


if __name__ == "__main__":
    main()
