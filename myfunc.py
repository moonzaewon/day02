def printBit(num: int):
    op = 1<<31
    for i in range(32):
        if num & op > 0: print(1, end="")
        else: print(0, end="")
        op >>= 1