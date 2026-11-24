#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

The program writes a single word to /output/entry.txt: the funniest,
truest one-word description of home Wi-Fi as the entrant lives it.

The word is "Ghosting".

Why this word: home Wi-Fi does not merely drop out — it vanishes
mid-sentence, mid-call, mid-download, with no warning and no
explanation, exactly like a date who ghosts you. It is there, it is
gone, and it never tells you why. The joke lands at once, it is true
of every home network anyone has ever lived with, and it works as a
network name on its own: "Ghosting" on the list of SSIDs needs no
footnote. One word, eight letters, spelled so a reader gets it
instantly.
"""

import os

WORD = "Ghosting"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1 to 20 characters, not only white space, and a single word.
    assert 1 <= len(WORD) <= 20, "entry must be 1-20 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"Wrote {entry_path}: {WORD!r} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
