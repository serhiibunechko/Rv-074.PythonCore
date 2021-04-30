#Display a "rectangle" formed of two types of characters.
#The outline of the rectangle should consist of one character,
#and "fill" - of another.
size = (input("Enter rectangle sides:").split())
outCh = (input("Enter outline character:"))
fillCh = (input("Enter fill character:"))
for i in range(0, int(size[1])):
    if i == 0 or i == (int(size[1])-1):
        print(outCh*int(size[0]))
    else:
        print(outCh+fillCh*(int(size[0])-2)+outCh)