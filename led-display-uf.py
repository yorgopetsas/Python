zero = ["###", "# #", "# #", "# #", "###"]
one = ["#  ", "#  ", "#  ", "#  ", "#  "]
two = ["###", "  #", "###", "#  ", "###"]
three = ["###", "  #", "###", "  #", "###"]
four = ["# #", "# #", "###", "  #", "  #"]
five = ["###", "  #", "###", "  #", "###"]
six = ["###", "#. ", "###", "# #", "###"]
seven = ["###", "  #", " #", "  #", "  #"]
eight = ["###", "# #", "###", "# #", "###"]
nine = ["###", "# #", "###", "  #", "###"]

digits = [zero, one, two, three, four, five, six, seven, eight, nine]

nbr = input('Introduce a number:')
# intnbr = int(nbr)

for i in range(len(nbr)):
    list = []
    intz = int(nbr[i])
    digit = digits[intz]
    for i in range(len(digit)):
        list = digit[i]
        print(list)
