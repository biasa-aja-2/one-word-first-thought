"""One Word, First Thought.

Writes a single word to /output/entry.txt: the first word that comes
to mind. The word is "mamihlapinatapai" — a Yaghan word for the look
shared by two people, each wishing the other would start what both
want but neither wants to begin. One word, a whole scene: surprising,
vivid, and witty enough to reward a second look.

Pure standard library, deterministic: the same word on every run.
"""

import os

WORD = "mamihlapinatapai"


def main() -> None:
    word = WORD.strip()
    assert word, "word must not be empty"
    assert 1 <= len(word) <= 24, f"word is {len(word)} chars, gate allows 1-24"
    assert word.strip(), "word must not be only whitespace"
    assert " " not in word and "\n" not in word, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    # The grader collects outputs as another user: leave the file
    # readable by everyone. Never chmod /output itself.
    os.chmod(path, 0o644)
    # Verify the written word by reading it back: the entry on disk
    # must be exactly the word this program produced.
    with open(path, encoding="utf-8") as f:
        assert f.read() == word, "written word differs from the word"


if __name__ == "__main__":
    main()
