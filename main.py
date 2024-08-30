from app.utils.helpers import ask_ai
import json


with open("data/quiz-template.json") as f:
    outline = json.load(f)


def write_instructions(path, book, chapter):
    instruction = (
        f"Generate a complete and valid JSON for {book} chapter {chapter} from the Bible. "
        "Follow the provided template exactly, ensuring all fields are filled with correct and relevant information. "
        "Important requirements:"
        "\n1. The quiz MUST have exactly 20 questions in total, distributed as specified."
        "\n2. Include all sections from the template:"
        " key_themes, key_verses, characters, events, concepts, and cross_references."
        "\n3. Provide detailed descriptions for events, including specific locations mentioned."
        "\n4. Include at least 5 key concepts relevant to the chapter."
        "\n5. Provide at least 4 cross-references, including both Old and New Testament connections where applicable."
        "\n6. Give detailed descriptions of characters, including their roles and significance."
        "\n7. Ensure the JSON is complete, valid, and uses double quotes for strings."
        "\n8. Aim to keep the total output within approximately 6000 tokens to allow for more comprehensive coverage."
        "\n9. IMPORTANT: Provide ONLY the JSON data in your response."
        "Do not include any explanatory text before or after the JSON."
        "\nHere's the template to follow:\n" + str(outline)
    )

    data = f"{instruction}\n{outline}?"

    with open(path, "w+", encoding="utf-8") as f:
        f.write(data)


def generate_quiz(book, chapter):
    prompt_path = "./data/prompt.txt"
    write_instructions(prompt_path, book, chapter)
    return ask_ai(prompt_path)


def write_json(path, data):
    with open(path, "w+", encoding="utf-8") as f:
        data = json.loads(data)
        json.dump(data, f, indent=4)


def main():
    book, chapter = "Genesis", 18
    data = generate_quiz(book, chapter)
    write_json(f"data/{book}/{book.lower()}-{chapter}.json", data)


if __name__ == "__main__":
    main()
