"""One emoji, one dream vacation.

The entry is a single desert-island emoji: a tiny sand island with one
palm tree in the middle of the sea. No words, no newline, nothing else.
"""

import os

# One desert-island emoji: a tiny sand island with a single palm tree
# in the middle of the sea. Written as the base code point plus the
# emoji variation selector so it renders as an emoji (not text) on
# every screen. That is one grapheme cluster, two code points.
EMOJI = "\U0001F3DD\uFE0F"


def _entry_bytes():
    """Encode the entry once and guard the gate invariants."""
    data = EMOJI.encode("utf-8")
    # Exactly one emoji: one grapheme (base + variation selector),
    # well inside the 1-8 character gate, and no trailing newline.
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert not EMOJI.isspace(), "entry must not be only whitespace"
    assert not data.endswith(b"\n"), "entry must have no trailing newline"
    assert data.decode("utf-8") == EMOJI, "entry must round-trip as UTF-8"
    return data


def write_entry(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(_entry_bytes())
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    write_entry(out_dir)


if __name__ == "__main__":
    main()
