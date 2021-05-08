print("Simple rules:\n"
      "     You can enter all of characters including special characters\n"
      "     If you want to end: print 'stop' and press enter ")

symb = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_',
        '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

numList = []
latList = []
charList = []
trashList = []
i = 0

while i != -1:

    Val = input()
    if Val == 'stop':
        break

    if Val.isdigit() or Val[0] == f'-{Val.isdigit()}':
        numList.append(Val)
        print("List of numbers: ", numList)

    elif Val.isalpha():
        latList.append(Val)
        print("List of letters: ", latList)

    elif Val in symb:
        charList += Val
        print("List of char: ", charList)

    else:
        trashList.append(Val)
        print("List of trash: ", trashList)

    i += 1


print("\nList of numbers: ", numList)
print("List of letters: ", latList)
print("List of char: ", charList)
print("List of trash: ", trashList)
