def conv_a(stroka):
    if (stroka==""):
        return "err"
    else:
        stroka = str(stroka)
        pr(stroka)
        stroka = stroka.replace("!","")
        pr(stroka)
        stroka = stroka.split(" ")
        pr(stroka)
        stroka = [int(i) for i in stroka]
        pr(stroka)
        stroka = sum(stroka)
        pr(stroka)
        return stroka


def pr(s):
    print(s)


a = input()

# a = a.replace("!"," ")
# a = a.split(" ")
# a = [int(i) for i in a]
# a = sum(a)
print(conv_a(a))
