fuelCap = float(input("Input fuel capacity: "))
fuelAm = float(input("Input how much fuel is in your tank: "))
sens = "green"
if fuelAm < fuelCap * 0.1:
    sens = "Red"
print(sens)