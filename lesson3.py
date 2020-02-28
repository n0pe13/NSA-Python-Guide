import random
import datetime

### Exercise Set 1 ###

# 1, 4
def you_won():
    wallet = 10
    price = random.choice(list([9.42, 5.67, 3.25, 13.40, 7.50]))
    if price > wallet:
        print(f"You won! You would have owed ${price - wallet}. Keep your $10 and your change for a total of ${wallet + (price - wallet)}")
    else:
        print(f"You lose! You owe ${wallet - price}")

# 2
def snack_check(snack):
    if snack == "fruit":
        print(True)
    else:
        print(False)


### Exercise Set 2 ###

# 1
def snack_check2(snack):
    if snack == "fruit":
        print("This is my favorite snack")
    else:
        print("Not my favorite snack")

# 2 - 3
def in_grocery_list(grocery_item):
    grocery = list(["peanut butter", "oatmeal", "honey", "chicken", "fruit"])
    
    if type(grocery_item) == str:
        if grocery_item in grocery:
            print(f"{grocery_item} is on the list")
        else:
            print(f"{grocery_item} isnt on the list")
    else:
        print("Invalid input, enter a string")

# 5
def current_time():
    now = datetime.datetime.now()
    
    str_now = now.strftime("%H:%M")
 
    if str_now >= "12:00" and str_now < "17:00":
        print("Good afternoon")
    elif str_now >= "17:00" and str_now < "00:00":
        print("Good evening")
    else:
        print("Good morning")


### Exercise Set 3 ###

# 1
def while_ex():
    while random.randint(0, 9):
        print("fruit\n")

# 2
def while_ex2():
    x = 1
    while x <= 10:
        print(f"{x}. fruit\n")
        x += 1

# 3
def while_ex3():
    
    x = 1
    while x <= 100:
        print("fruit")
        x += 1


### Exercise Set 4 ###

# 1, 5
def for_ex():
    for_str = "blood-oxygenation level dependent functional magnetic resonance imaging".split()

    for s in for_str:
        print(s)

# 2 - 4
def for_ex2():
    grocery = list(["peanut butter", "oatmeal", "fruit", "honey", "chicken"])
    
    #for g in grocery:
        #print(f"Note to self, buy: {g}")

    for i, x in enumerate(grocery):
        if x == "fruit":
            print(f"{i+1}. {x}")
            break


### Exercise Set 5 ###

# 1 - 3
def for_ex3():
    grocery = list(["peanut butter", "oatmeal", "fruit", "honey", "chicken"])

    #for g in range(0, len(grocery)):
        #print(f"{g+1}. {grocery[g]}")

    #for x, i in enumerate(grocery):
        #print(f"{x+1}. {i}")

    for g in range(0, 10):
        print(grocery)

# 4
def guess_game():
    guess_ctr = 1
    rand_num = random.randint(0, 10)
    
    while guess_ctr <= 3:
        user_guess = int(input("What number do you guess? "))
        if user_guess != rand_num:
            print("Incorrect")
            guess_ctr += 1
        else:
            print("Correct!")
            break


if __name__=='__main__':
    #you_won()
    #snack_check("fruit")
    #snack_check2("fruit")
    #in_grocery_list(5)
    #current_time()
    #while_ex()
    #while_ex2()
    #while_ex3()
    #for_ex()
    #for_ex2()
    #for_ex3()
    #guess_game()











