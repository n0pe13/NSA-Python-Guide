# 1 - 3, 7
def main():
    total = 0
    
    grocery_list = list(["peanut butter", "oatmeal", "honey", "chicken", "fruit"])
    for s in grocery_list:
        print(s + "\n")

    grocery_bill = [9.42, 5.67, 3.25, 13.40, 7.50]
    total = (sum(grocery_bill[:4]) + grocery_bill[-1] * 5)
    print(total)

# 4
def main2():
    print(len("blood-oxygenation level dependent functional magnetic resonance imaging"))

# 5
def main3():
    print("fruit " * 100)

# 6
def main4():
    print(dir(__name__))
    #print(help(str))
    print(help(int))

if __name__=='__main__':
    #main()
    #main2()
    #main3()
    #main4()