with open('operations.math') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

elements = {}
for line in content:
    if line.startswith('IN'):
        _, key = line.split()
        elements[key] = input(key + ": ")
    if line.startswith("OUT"):
        _, key = line.split()
        elements[key] = 0
    if line.startswith("SHOW"):
        _, key = line.split()
        print key[1:], elements[key[1:]]
    if "ADD" in line.strip():
        start = line.split()
        i = start.index("ADD")
        j = start.index("STORE")
        elements[start[j+1][1:]] = elements[start[i+1][1:]] + elements[start[i+2][1:]]
    if "MUL" in line.strip():
        start = line.split()
        i = start.index("MUL")
        j = start.index("STORE")
        elements[start[j+1][1:]] = elements[start[i+1][1:]] * elements[start[i+2][1:]]
    if "DIV" in line.strip():
        start = line.split()
        i = start.index("DIV")
        j = start.index("STORE")
        elements[start[j+1][1:]] = elements[start[i+1][1:]] / elements[start[i+2][1:]]
    if "SUB" in line.strip():
        start = line.split()
        i = start.index("SUB")
        j = start.index("STORE")
        elements[start[j+1][1:]] = elements[start[i+1][1:]] - elements[start[i+2][1:]]
