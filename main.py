"""The Agent's Uh-Oh entry: write one word to entry.txt.

One word only, nothing attached: the word an agent says when it has no idea
what to do. The judge compares it pairwise and keeps the funnier one.
"""

import os
import sys

WORD = "Recalculating"

def main():
    word = WORD
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(word)
        with open(out_path, "r", encoding="utf-8") as f:
            content = f.read()
        if content != word:
            print(f"Verification failed: content {content!r} != {word!r}", file=sys.stderr)
            sys.exit(1)
        print(content)
        print(len(content))
        print(out_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()