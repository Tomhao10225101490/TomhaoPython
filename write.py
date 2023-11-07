f = open("writeme.txt", "a")
txt = "You are mine"
for i in range(5):
    print(len(txt),end = ' ')
    print(f.write(txt))
f = open("writeme.txt")
txt = f.read(21)
print(txt)