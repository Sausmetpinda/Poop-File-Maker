print("making poop file")
for i in range(1, 20):
    f = open("./PoopFile%d.txt" %i, "w+")
    for i in range(1, 100):
        f.write("poop\n")
    f.close()
print("hahaha get pooped on")

