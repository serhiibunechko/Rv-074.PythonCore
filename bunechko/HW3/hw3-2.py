n = int(input("How bytes: "))
c = input("Bytes into Kb (k) or in Mb (m): ")
if c == 'k':
    print("%d byte = %.2f Kb" % (n, n/1024))
elif c == 'm':
    print("%d byte = %.6f Mb" % (n, n/1024**2))

#n = int(input("How bytes into Kb and Mb: "))
#print(("%d byte = %d Kb" % (n, n/1024)), ("%d byte = %.2fMb" % (n, n/1024**2)))
