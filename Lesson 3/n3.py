a = input().split()
a = [int(i) for i in a]
high = max(a)+3
for i in range(high):
    if (i==0 or i==high-1):
        print("#"*(len(a)+2))
    else:
        print("#", end="")
        for j in range(len(a)):
            if a[j]-(high-i)+1>=0:
                print("*", end = "")
            else:
                print(" ", end="")
        print("#", end="")
        print()

