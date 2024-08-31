import json
import os
from typing import Dict, Any


def validate_json_structure(data: Dict[str, Any]) -> bool:
    # Check top-level keys
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

    # Validate quiz_structure
    quiz_structure = data["quiz_structure"]
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

    # Validate sections
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

    # Validate key_themes
    if not isinstance(data["key_themes"], list) or len(data["key_themes"]) < 1:
        return False

    # Validate key_verses
    if not isinstance(data["key_verses"], list) or len(data["key_verses"]) < 1:
        return False
    for verse in data["key_verses"]:
        if not isinstance(verse, dict) or "reference" not in verse:
            return False

    # Validate characters
    if not isinstance(data["characters"], list) or len(data["characters"]) < 1:
        return False
    for character in data["characters"]:
        if (
            not isinstance(character, dict)
            or "name" not in character
            or "role" not in character
        ):
            return False

    # Validate events
    if not isinstance(data["events"], list) or len(data["events"]) < 1:
        return False
    for event in data["events"]:
        if (
            not isinstance(event, dict)
            or "description" not in event
            or "location" not in event
        ):
            return False

    # Validate concepts
    if not isinstance(data["concepts"], list) or len(data["concepts"]) < 1:
        return False

    # Validate cross_references
    if (
        not isinstance(data["cross_references"], dict)
        or "Old Testament" not in data["cross_references"]
        or "New Testament" not in data["cross_references"]
    ):
        return False
    for testament in ["Old Testament", "New Testament"]:
        if not isinstance(data["cross_references"][testament], list):
            return False
        for reference in data["cross_references"][testament]:
            if (
                not isinstance(reference, dict)
                or "reference" not in reference
                or "description" not in reference
            ):
                return False

    return True


def main():
    jsons = []
    files = os.listdir("./Genesis")
    for file in files:
        if file.endswith(".json"):
            with open(f"./Genesis/{file}", "r") as f:
                jsons.append(json.load(f))
    for f, j in zip(files, jsons):
        file_path = f"./Genesis/{f}"
        is_valid = validate_json_structure(j)
        if not is_valid:
            os.remove(file_path)


if __name__ == "__main__":
    main()
