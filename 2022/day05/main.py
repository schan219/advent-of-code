"""Module crate stacking."""

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(TEST, encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]
