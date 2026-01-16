def secret_password(input: list[str]):
    """Return the number of times the dial is left pointing at 0 after any rotation in the sequence"""
    i = 50
    count = 0

    for item in input:
        direction, amount_str = item[0], item[1:]
        amount = (
            int(amount_str) % 100
        )  # ignore wrap around (only 100 possible placements)

        if direction == "L":
            i = (i - amount) % 100
        elif direction == "R":
            i = (i + amount) % 100

        if i == 0:
            count += 1

    return count


def read_parse_file(file_path) -> list[str] | None:
    try:
        with open(file_path, "r") as file:
            res = []
            for line in file:
                res.append(line.strip())
            return res
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while reading the file '{file_path}'.")


if __name__ == "__main__":
    file_path = "./input.txt"
    input = read_parse_file(file_path=file_path)
    if not input:
        exit(1)
    s1 = secret_password(input=input)
    print(s1)
