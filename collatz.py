def collatz(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1

def collatz_sequence(n: int):
    sequence = [n]
    while n != 1:
        n = collatz(n)
        sequence.append(n)
    return sequence


def main():
    print("Enter a positive integer or 'q' to quit")
    while True:
        n = input("> ")
        if n == "q":
            break
        try:
            n = int(n)
            if n < 1:
                print(f"'{n}' is not a positive integer")
                continue
            print(" ".join(map(str, collatz_sequence(n))))
        except ValueError:
            print(f"'{n}' is not an integer")


if __name__ == "__main__":
    main()
