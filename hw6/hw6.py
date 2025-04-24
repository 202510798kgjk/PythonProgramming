for i in range(2):
    for k in range(1,10):
        for j in range(2,6):
            print(f"{j+i*4}*{k}={(j+i*4)*k}",end="\t")
        print()
    print()
