from app.utils.helpers import ask_ai


with open("./data/outline.txt", "r") as f:
    outline = f.read()


def generate_quiz(book, chapter):
    ask_ai(
        "**DO NOT HALLUCINATE**\n"
        + f"Create an quiz for {book} {chapter}"
        + "\n Following this outline:"
        + outline
    )


def main():
    generate_quiz("Genesis", 1)
    pass


if __name__ == "__main__":
    main()
