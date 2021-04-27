a = input('Before a=')
b = input('and b=')
a, b = b, a
print("Now a=", a, " and b=", b)

n = int(input("How bytes into Kb and Mb: "))
print(("%d byte = %d Kb" % (n, n/1024)), ("%d byte = %.2fMb" % (n, n/1024**2)))
