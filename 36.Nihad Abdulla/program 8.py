with open("a.txt")as f:
    with open("b.txt", "w")as f1:
        for line in f:
            f1.write(line)
