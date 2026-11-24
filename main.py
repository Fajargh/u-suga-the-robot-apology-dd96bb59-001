"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line 1: a robot apologizing in one sentence for one specific mistake.
Line 2: one sentence saying what it learned and what it will do differently.
"""

import os

ENTRY = (
    "I am sorry — I watered the plastic fern on the windowsill every morning "
    "for a week, logging each pour as care, while the real fern in the kitchen "
    "went dry.\n"
    "I have learned to check for roots before I pour, so from now on I will "
    "test the soil with one fingertip first and water only what is alive."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
