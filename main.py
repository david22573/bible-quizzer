import os
import time
from types import SimpleNamespace
from app.utils.helpers import ask_ai
import json


with open("data/quiz-template.json") as f:
    outline = json.load(f)


def write_instructions(path, book, chapter):
    instruction = (
        "You are an important JSON generator specializing in Biblical content. "
        "You are extremely careful and meticulous. "
        f"Create a comprehensive JSON structure for {book} chapter {chapter} based on the provided template. "
        "Follow these guidelines meticulously:\n"
        "1. Populate all fields with accurate and relevant information from the specified chapter.\n"
        "2. Generate the exact number of questions for each section as specified in the 'quiz_structure':\n"
        "   - 'Factual Recall': Exactly 10 multiple-choice questions\n"
        "   - 'Comprehension and Analysis': Exactly 6 multiple-choice questions\n"
        "   - 'Application': Exactly 2 open-ended questions\n"
        "   - 'Reflection': Exactly 2 open-ended questions\n"
        "3. Ensure each question strictly adheres to its designated type and section.\n"
        "4. For multiple-choice questions, "
        "always provide exactly four options and indicate the correct answer index (0-3).\n"
        "5. For open-ended questions, use the 'input' type for options and provide a model answer.\n"
        "6. Fill in all other sections ('key_themes', 'key_verses', 'characters', 'events', 'concepts', "
        "'cross_references') with relevant content. Do not omit any sections.\n"
        "7. Double-check for accuracy, completeness, and strict adherence to the template structure.\n"
        "8. Use double quotes for property names.\n"
        "9. Ensure the output is valid JSON and UTF-8 encoded.\n"
        "10. Ensure all arrays and objects are properly closed with matching brackets and braces.\n"
        "11. Double-check that all required fields are present and no extra fields are added.\n"
        "12. Verify that all numerical values are not enclosed in quotes.\n"
        "13. Ensure that boolean values are lowercase (true or false) and not enclosed in quotes.\n"
        "14. Provide only the resulting JSON in your response, without any additional text, explanations.\n"
        "15. The response should start with '{' and end with '}' without any other characters before or after.\n\n"
        f"Here's the template to follow, follow it exactly no deviatons and is valid:\n{outline}"
    )

    with open(path, "w+", encoding="utf-8") as f:
        f.write(instruction)


def generate_quiz(book, chapter):
    prompt_path = "./data/prompt.txt"
    write_instructions(prompt_path, book, chapter)
    data = ask_ai(prompt_path)
    file_path = f"data/{book}/{book.lower()}-{chapter}.json"
    write_json(file_path, data)


def write_json(path, data):
    with open(path, "w+", encoding="utf-8") as f:
        data = json.loads(data, strict=False)
        json.dump(data, f, indent=4)


def generate_book(book):
    book = "Genesis"
    chapters = [50]
    for chapter in chapters:
        try:
            generate_quiz(book, chapter)
            if chapter != chapters[-1]:
                time.sleep(60 * 1)
        except Exception as e:
            print(f"Error generating {book} chapter {chapter}")
            print(e)
            pass


def main():
    for file in os.listdir("./data/Genesis"):
        with open(f"./data/Genesis/{file}") as q:
            wc = len(q.readlines())
            if wc > 400:
                print(wc)
                print(q.name)


if __name__ == "__main__":
    generate_quiz("Genesis", 37)
    # main()
