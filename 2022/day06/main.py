
"""Module signal processing."""

START_BUFFER_LENGTH = 4
START_MESSAGE_BUFFER_LENGTH = 14

def get_marker(signal, buffer_length):
    for i in range(0, len(signal)):
        buffer = signal[i:i+buffer_length]
        buffer_set = set(buffer)
        if len(buffer_set) == buffer_length:
            return i+buffer_length

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line for line in file]

    print(get_marker(lines[0], START_MESSAGE_BUFFER_LENGTH))
