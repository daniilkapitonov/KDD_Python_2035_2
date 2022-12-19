c1 = 0
c2 = 0
tc = 0

w1 = input("Слово - ")
w2 = input("Слово - ")
while c1<=3 and c2<=3:
    print("Ход игрока",tc%2+1)
    if w2[0]==w1[-1]:
        w1 = w2
        w2 = input("Слово - ")
        tc+=1
    else:
        print("Error")
        if tc%2 == 0:
            c1+=1
        else:
            c2+=1
        w2 = input("Слово - ")
    
if (c1>=3):
    print("Игрок 1 проиграл")
else:
    print("Игрок 2 проиграл")