from typing import Dict, Any
import os
import json


def validate_quiz_structure(quiz_structure: Dict[str, Any]) -> bool:
    if (
        not isinstance(quiz_structure, dict)
        or "total_questions" not in quiz_structure
        or "sections" not in quiz_structure
    ):
        return False

    if not isinstance(quiz_structure["total_questions"], int) or not isinstance(
        quiz_structure["sections"], list
    ):
        return False

    section_names = {
        "Factual Recall",
        "Comprehension and Analysis",
        "Application",
        "Reflection",
    }
    for section in quiz_structure["sections"]:
        if (
            not isinstance(section, dict)
            or "name" not in section
            or section["name"] not in section_names
        ):
            return False
        if (
            "count" not in section
            or "question_types" not in section
            or "questions" not in section
        ):
            return False
        if (
            not isinstance(section["count"], int)
            or not isinstance(section["question_types"], list)
            or not isinstance(section["questions"], list)
        ):
            return False

    return True


def validate_key_themes(key_themes: Any) -> bool:
    return isinstance(key_themes, list) and len(key_themes) > 0


def validate_key_verses(key_verses: Any) -> bool:
    if not isinstance(key_verses, list) or len(key_verses) < 1:
        return False
    for verse in key_verses:
        if not isinstance(verse, dict) or "reference" not in verse:
            return False
    return True


def validate_characters(characters: Any) -> bool:
    if not isinstance(characters, list) or len(characters) < 1:
        return False
    for character in characters:
        if (
            not isinstance(character, dict)
            or "name" not in character
            or "role" not in character
        ):
            return False
    return True


def validate_events(events: Any) -> bool:
    if not isinstance(events, list) or len(events) < 1:
        return False
    for event in events:
        if (
            not isinstance(event, dict)
            or "description" not in event
            or "location" not in event
        ):
            return False
    return True


def validate_concepts(concepts: Any) -> bool:
    return isinstance(concepts, list) and len(concepts) > 0


def validate_cross_references(cross_references: Any) -> bool:
    if (
        not isinstance(cross_references, dict)
        or "Old Testament" not in cross_references
        or "New Testament" not in cross_references
    ):
        return False
    for testament in ["Old Testament", "New Testament"]:
        if not isinstance(cross_references[testament], list):
            return False
        for reference in cross_references[testament]:
            if (
                not isinstance(reference, dict)
                or "reference" not in reference
                or "description" not in reference
            ):
                return False
    return True


def validate_json_structure(data: Dict[str, Any]) -> bool:
    required_keys = {
        "book",
        "chapter",
        "quiz_structure",
        "key_themes",
        "key_verses",
        "characters",
        "events",
        "concepts",
        "cross_references",
    }
    if not all(key in data for key in required_keys):
        return False

    if not validate_quiz_structure(data["quiz_structure"]):
        return False

    if not validate_key_themes(data["key_themes"]):
        return False

    if not validate_key_verses(data["key_verses"]):
        return False

    if not validate_characters(data["characters"]):
        return False

    if not validate_events(data["events"]):
        return False

    if not validate_concepts(data["concepts"]):
        return False

    if not validate_cross_references(data["cross_references"]):
        return False

    return True


def write_missing_chapters(missing_chapters):
    with open("./missing_chapters.txt", "w+") as f:
        f.write("\n".join(missing_chapters))


def main():
    book = "Exodus"
    files = os.listdir(book)
    missing_chapters = []
    for file in files:
        # file_path = f"./Genesis/{file}"
        if file.endswith(".json"):
            try:
                with open(f"./{book}/{file}", "r") as f:
                    j = json.load(f)
                is_valid = validate_json_structure(j)
                if not is_valid:
                    missing_chapters.append(file)
                    print(f"{file} is not valid")
                else:
                    print(f"{file} is ok!")
            except Exception:
                missing_chapters.append(file)
                print(f"{file} is not valid with an error")
                continue

    write_missing_chapters(missing_chapters)


if __name__ == "__main__":
    main()
