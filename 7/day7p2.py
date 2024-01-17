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

def get_ABAs(texts: list) -> set:
    result = set()
    for text in texts:
        n = len(text)
        for i in range(2, n):
            if text[i] == text[i - 2] and text[i - 1] != text[i]:
                result.add(text[i - 2] + text[i - 1] + text[i])
    return result

def supports_TLS(address: list) -> bool:
    supernets, hypernets = address
    
    supernet_abas = get_ABAs(supernets)
    hypernet_abas = get_ABAs(hypernets)

    for aba in supernet_abas:
        bab = aba[1] + aba[0] + aba[1]
        if bab in hypernet_abas:
            return True

    return False

result = 0
for address in addresses:
    if supports_TLS(address):
        result += 1
    
print(result)
