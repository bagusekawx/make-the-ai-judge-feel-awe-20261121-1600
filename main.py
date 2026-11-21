import os

TEXT = (
    "The last streetlight ends and the road becomes a field. "
    "The grass is still warm from the day. "
    "Crickets hold their sound like a cup holds steam, loosely, letting it rise. "
    "Your steps shorten. "
    "Standing still feels ordinary. "
    "And the sky, which waited all day, gets to be big."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
