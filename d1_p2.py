def secret_password(input: list[str]):
    """Return the number of times the dial is left pointing at 0 at any point during rotation in the sequence"""
    i = 50
    count = 0

    for item in input:
        direction, amount_str = item[0], item[1:]
        amount = int(amount_str)

        full_rotations = amount // 100
        count += full_rotations
        rem_rotations = amount - full_rotations * 100

        print(count, full_rotations)

        if direction == "L":
            new = i - rem_rotations
            if new <= 0:
                count += 1
            i = new % 100

        elif direction == "R":
            new = i + rem_rotations
            if new >= 100:
                count += 1
            i = new % 100

        # if i == 0:
        #     count += 1

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
    print(s1, len(input))

    # ############################################

    # file_path = "./input2.txt"
    # input = read_parse_file(file_path=file_path)
    # if not input:
    #     exit(1)
    # s1 = secret_password(input=input)
    # print("---")
    # print(s1, len(input))
