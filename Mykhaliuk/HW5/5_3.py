#​Display a multiplication table (1 to 9).
for i in range(0, 9):
    print(f"\nFor {i+1}\n")
    for j in range(0, 9):
        print(f"{i+1}*{j+1} = {(i+1)*(j+1)}")