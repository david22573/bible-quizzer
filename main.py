from app.utils.helpers import ask_ai


with open("./data/outline.txt", "r") as f:
    outline = f.read()


def generate_quiz(book, chapter):
    return ask_ai(
        f"Generate a quiz for {book} {chapter} that follows this outline: "
        + outline
        + "?"
    )


def main():
    generate_quiz("Genesis", 1)
    pass


if __name__ == "__main__":
    main()
