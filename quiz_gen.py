import os
import time
from app.utils.helpers import ask_ai
import json


class QuizGenerator:
    def __init__(self, book, chapter):
        self.book = book
        self.chapter = chapter

        with open("data/quiz-template.json") as f:
            self.outline = json.load(f)

    def set_instructions(self):
        with open("./data/prompt_template.txt") as f:
            instructions = f.read()
        instructions = instructions.replace("{book}", self.book)
        instructions = instructions.replace("{chapter}", str(self.chapter))
        with open("./data/prompt.txt", "w+") as f:
            f.write(instructions)

    def generate(self):
        self.set_instructions()
        prompt_path = "./data/prompt.txt"
        data = ask_ai(prompt_path)
        self.write_json(data)

    def write_json(self, data):
        fp = f"data/{self.book}/{self.book.lower()}-{self.chapter}.json"
        if not os.path.exists(f"./data/{self.book}"):
            os.makedirs(f"./data/{self.book}")
        with open(fp, "w+", encoding="utf-8") as f:
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
    generate_book("Deuteronomy", 34)


if __name__ == "__main__":
    main()
