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

def get_length(text: str) -> list:
    n = len(text)
    up_scales = [1 for _ in range(n + 1)]
    down_scales = [1 for _ in range(n + 1)]
    i = 0
    while i < n:
        if text[i] == '(':
            repeating_length, repeating_count, new_i = read_nums(text, i + 1)
            up_scales[new_i] *= repeating_count
            down_scales[new_i + repeating_length] *= repeating_count
            i = new_i
            continue
        i += 1

    all_scales = [0 for _ in range(n)]
    all_scales[0] = up_scales[0] // down_scales[0]
    for i in range(1, n):
        all_scales[i] = all_scales[i - 1] * up_scales[i] // down_scales[i]
    i = 0
    bracket = False
    while i < n:
        if text[i] == '(':
            bracket = True
        if bracket == True:
            all_scales[i] = 0
        if text[i] == ')':
            bracket = False
        i += 1

    for i in range(1, n):
        all_scales[i] += all_scales[i - 1]
    
    return all_scales[n - 1]
            
text = open('input2.txt').read().strip()
decompressed_length = get_length(text)
print(decompressed_length)