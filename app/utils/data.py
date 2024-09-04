import os
import json


OLD_TESTAMENT = [
    # Old Testament
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "1 Samuel",
    "2 Samuel",
    "1 Kings",
    "2 Kings",
    "1 Chronicles",
    "2 Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "Song of Solomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi",
]

NEW_TESTAMENT = [
    # New Testament
    "Matthew",
    "Mark",
    "Luke",
    "John",
    "Acts",
    "Romans",
    "1 Corinthians",
    "2 Corinthians",
    "Galatians",
    "Ephesians",
    "Philippians",
    "Colossians",
    "1 Thessalonians",
    "2 Thessalonians",
    "1 Timothy",
    "2 Timothy",
    "Titus",
    "Philemon",
    "Hebrews",
    "James",
    "1 Peter",
    "2 Peter",
    "1 John",
    "2 John",
    "3 John",
    "Jude",
    "Revelation",
]

COLLECTION = OLD_TESTAMENT + NEW_TESTAMENT


def get_books():
    books = {}
    _, dirs, _ = next(os.walk("./data"))
    for book in COLLECTION:
        if book in dirs:
            books[book] = os.listdir(f"./data/{book}")
    return books


def get_quiz(book, chapter):
    try:
        with open(f"./data/{book.lower()}-{chapter}.json") as jf:
            return json.load(jf)
    except FileNotFoundError:
        print(f"File not found: {book.lower()}-{chapter}.json")
        return None
    except json.decoder.JSONDecodeError:
        print(f"JSON error: {book.lower()}-{chapter}.json")
        return None


if __name__ == "__main__":
    print(get_books())
