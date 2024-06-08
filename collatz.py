def collatz(n: int):
    if n <= 0:
        return ValueError("'n' must be a positive integer")
    if n == 1:
        return 1
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_sequence(n: int):
    if n <= 0:
        return ValueError("'n' must be a positive integer")
    if n == 1:
        return 1
    sequence = [n]
    while n != 1:
        n = collatz(n)
        sequence.append(n)

    return sequence


def main():
    print("Enter a positive integer or 'q' to quit")
    while True:
        n = input("> ")
        try:
            if n == "q":
                break
            n = int(n)
            if n < 1:
                print(f"'{n}' is not a positive integer")
                continue
            for x in collatz_sequence(n):
                print(x, end=" ")
            print()
        except ValueError:
            print(f"'{n}' is not an integer")
            continue


if __name__ == "__main__":
    main()
