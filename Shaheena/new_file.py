#Exercise 7:
#Draw a hollow square with * using a length as an input


area = int(input("Enter the area"))
for i in range(area):
    for j in range(area):
        if i==0 or i == (area - 1):
            print(" * ", end="")
        else:
            if j==0 or j == (area - 1):
                print(" * ", end="")
            else:
                print("   ", end="")

    print()