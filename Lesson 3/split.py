a = "1?2?3?3?3?3?3?3".split("?")
print(a)
print(sum([int (i) for i in a])/len(a))
b = [int (i) for i in a]
print(b)
print(sum(map(int,a)))