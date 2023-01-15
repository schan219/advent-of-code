"""Module file system item search"""

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line for line in file]
