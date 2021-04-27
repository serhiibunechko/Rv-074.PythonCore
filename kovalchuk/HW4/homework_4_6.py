n = int(input("Number of a place: "))
if n in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]:
    print("Your place in the bottom of compartment")
elif n in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]:
    print("Your place in the top of compartment")
elif n in [37,39,41,43,45,47,49,51,53]:
    print("Your place in the bottom of side")
elif n in [38,40,42,44,46,48,50,52,54,56]:
    print("Your place in the top of side")
else:
    print("Incorrect number")