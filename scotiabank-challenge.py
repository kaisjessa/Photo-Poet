data = []

while True:
    try:
        line = input()
        if line == "": break
        data.append(line.split())
    except:
        break

expanded = []

while data:
    expanded += data.pop(0)
    data = list(map(list, reversed(list(zip(*data)))))

print("".join(expanded))
