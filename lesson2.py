import random
import datetime

### Exercise Set 1 ###

# 1
def main():
    grocery_bill = list([9.42, 5.67, 3.25, 13.40, 7.50])
    print(min(grocery_bill))
    print(max(grocery_bill))

# 2
def main2():
    #print(help(random.randint))

    print("fruit" * random.randint(0, 99))

# 3 - 4
def main3():
    grocery_list = random.choice(list(["peanut butter", "oatmeal", "honey", "chicken", "fruit"]))
    grocery_bill = int(random.choice(list([9.42, 5.67, 3.25, 13.40, 7.50])))
    #print(dir(random))
    #print(grocery_list)
    print(grocery_bill)

# 5
def main4():
    wallet = 10
    grocery_bill = random.choice(list([9.42, 5.67, 3.25, 13.40, 7.50]))
    if grocery_bill < wallet:
        wallet -= grocery_bill
        print(wallet)
    else:
        wallet = wallet + (grocery_bill - wallet)
        print(wallet)


### Exercise Set 2 ###

# 1 - 3
def all_the_snacks(snack, spacer, num):
    print((snack + spacer) * num)

# 4
def in_grocery_list(grocery_item):
    grocery_list = list(["peanut butter", "oatmeal", "honey", "chicken", "fruit"])
    if grocery_item in grocery_list:
        print(True)
    else:
        print(False)

# 5 - 6
def price_matcher():
    grocery_bill = random.choice(list([9.42, 5.67, 3.25, 13.40, 7.50]))
    grocery_list = random.choice(list(["peanut butter", "oatmeal", "honey", "chicken", "fruit"]))
    #print(f"{grocery_list}: ${grocery_bill}")
    return grocery_bill, grocery_list

# 6
def free_change():
    wallet = 10
    wallet = abs(wallet - (price_matcher()[0]))
    print(list([wallet, price_matcher()[1]]))


### Exercise Set 3 ###

# 1 - 2
def main5():
    my_color = input("Your favorite color? ")
    neighbor_color = input("Neighbors favorite color? ")

    my_num = int(input("Your favorite number? "))
    print(2 + my_num)

# 3
def color_swapper(my_color, neighbor_color):
    my_color, neighbor_color = neighbor_color, my_color
    print(my_color, neighbor_color)
  

# 4
my_color = "blue"
neighbor_color = "red"
def global_color_swapper():
    global my_color
    global neighbor_color
    my_color, neighbor_color = neighbor_color, my_color
    print(my_color, neighbor_color)


### Review ###

# 1
def Volume(w, l, h):
    return w * l * h

# 2
def Volume2(w, l, h=1):
    return w * l * h

# 3
def main6():
    now = datetime.datetime.now()
    print(now)


### Function Exercises ###

def isDivisibleBy7(num):
    if num % 7 == 0:
        print(True)
    else:
        print(False)

def isDivisibleBy(num, divisor):
    if num % divisor == 0:
        print(True)
    else:
        print(False)

def shout(word):
    return f"{word.upper()}!"

def introduce():
    name = input("What is your name? ")
    return shout(name)


if __name__=='__main__':
    #main()
    #main2()
    #main3()
    #main4()
    #all_the_snacks("fruit", " ", 5)
    #in_grocery_list("cake")
    #price_matcher()
    #free_change()
    #main5()
    #color_swapper("blue", "red")
    #global_color_swapper()
    #print(Volume(2, 2, 2))
    #print(Volume2(2, 2))
    #main6()
    #isDivisibleBy7(7)
    #isDivisibleBy(21,7)
    #print(shout("hello"))
    #print(introduce())
