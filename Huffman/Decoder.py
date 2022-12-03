data = open("Compressed Stream.txt", "r")
CompressedCode = data.readline()
ShortCode = []
characters = []
with open('Short Code.txt') as p:
    for line in p:
        line = line.strip('\n')
        w = line.split("=")
        characters.append(w[0])
        ShortCode.append(w[1])
# print(encoder)
print()
result = ""
temp = ""
for i in CompressedCode:
    temp += i
    for y in ShortCode:
        if temp == y:
            q = ShortCode.index(y)
            result += characters[q]
            temp = ""

print(result)
