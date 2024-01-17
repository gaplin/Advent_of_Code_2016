input = open('input2.txt').read().splitlines()

addresses = []
for line in input:
    address = ([], [])
    line = line.split('[')
    address[0].append(line[0])
    for hypernet in line[1:]:
        values = hypernet.split(']')
        address[1].append(values[0])
        if len(values) == 2:
            address[0].append(values[1])

    addresses.append(address)

def contains_ABBA(text: str) -> bool:
    n = len(text)
    for i in range(3, n):
        if text[i - 3] != text[i - 2] and text[i] == text[i - 3] and text[i - 1] == text[i - 2]:
            return True
    return False

def supports_TLS(address: list) -> bool:
    supernets, hypernets = address
    for hypernet in hypernets:
        if contains_ABBA(hypernet):
            return False
        
    for supernet in supernets:
        if contains_ABBA(supernet):
            return True
    
    return False

result = 0
for address in addresses:
    if supports_TLS(address):
        result += 1
    
print(result)
