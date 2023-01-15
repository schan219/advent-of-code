
"""Module signal processing."""

START_BUFFER_LENGTH = 4
START_MESSAGE_BUFFER_LENGTH = 14

def get_marker(signal, buffer_length):
    for i in range(0, len(signal)):
        buffer = signal[i:i+buffer_length]
        buffer_set = set(buffer)
        if len(buffer_set) == buffer_length:
            return i+buffer_length

def get_marker_improved(signal, buffer_length):
    buffer_dict = {}
    previous = None
    for i, element in enumerate(signal):
        buffer = signal[i:i+buffer_length]
        if i != 0:
            buffer_dict[previous] -= 1
        buffer_dict = increment_buffer_dict(buffer)
        previous = element
        if check_buffer_dict(buffer_dict, buffer):
            return i+buffer_length
    return 0

def increment_buffer_dict(buffer):
    buffer_dict = {}
    for key in buffer:
        if key in buffer_dict:
            buffer_dict[key] += 1
        else:
            buffer_dict[key] = 1
    return buffer_dict

def check_buffer_dict(buffer_dict, buffer):
    for key in buffer:
        if buffer_dict[key] > 1:
            return False
    return True

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line for line in file]

    print(get_marker_improved(lines[0], START_MESSAGE_BUFFER_LENGTH))
