
def yz_split(strng):
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

print(yz_split("Ser o no ser, esa es la pregunta "))
print(yz_split("Ser o no ser,esa es la pregunta"))
print(yz_split(" "))
print(yz_split("   abc "))
print(yz_split("   "))

