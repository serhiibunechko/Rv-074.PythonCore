bytes = float(input("Enter the number of bytes: "))
choise = float(input("Choose data you want to convert it to:\nPrint 1 fot kBytes\nPrint 2 for mBytes\n "))
if bytes < 0:
    print("error")
if choise == 1:
    print(bytes / 1024, "Kb")
if choise == 2:
    print(bytes / 1048576, "Mb")
if choise > 2 or choise < 1:
    print("error")

