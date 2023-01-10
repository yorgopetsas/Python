
def mysplit(strng):
    p = 0
    list = []
    for x in range(len(strng)):
        word = ''
        if p == len(strng) - 1:
            return list
        while strng[p] == " ":
            if p == len(strng) - 1:
                return list
            p += 1
        while strng[p] != " ":
            word = word + strng[p]
            p += 1
            if p == len(strng) - 1:
                while strng[p] != " ":
                    word = word + strng[p]
                    list.append(word)
                    return list
        list.append(word)

print(mysplit("Ser o no ser, esa es la pregunta "))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit(" "))
print(mysplit("   abc "))
print(mysplit("   "))

