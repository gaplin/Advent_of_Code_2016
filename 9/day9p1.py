def read_nums(text: str, i: int) -> tuple:
    nums = [0, 0]
    idx = 0
    while text[i] != ')':
        if text[i] == 'x':
            idx += 1
        else:
            nums[idx] = nums[idx] * 10 + ord(text[i]) - ord('0')
        i += 1
    i += 1
    return (nums[0], nums[1], i)

def process_text(text: str) -> list:
    result = []
    n = len(text)
    i = 0
    repeating_sequence = []
    repeating_length = 0
    repeating_count = 0
    repeating = False
    while i < n:
        if text[i] == '(' and repeating == False:
            repeating_length, repeating_count, new_i = read_nums(text, i + 1)
            i = new_i
            repeating = True
            continue
        if repeating == True:
            repeating_sequence.append(text[i])
            if len(repeating_sequence) == repeating_length:
                result += repeating_sequence * repeating_count
                repeating = False
                repeating_sequence = []
        else:
            result += text[i]
        i += 1
    return result

text = open('input2.txt').read().strip()
processed_text = process_text(text)
print(len(processed_text))