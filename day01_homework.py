from itertools import zip_longest

### Day 01 Homework ###

def shopping():
    my_vegetables = []
    my_fruit = []
    my_cold_items = []
    my_proteins = []
    my_boxed_items = []
    my_paper_products = []
    my_toiletry_items = []
    myGroceryList = ["apples", "bananas", "milk", "eggs", "bread", "hamburgers", "hotdogs", "ketchup", "grapes",
                    "tilapia", "sweet potatoes", "cereal", "paper plates", "napkins", "cookies", "ice cream", 
                    "cherries", "shampoo"]

    for val, item in enumerate(myGroceryList):
        if item == "sweet potatoes":
            my_vegetables.append(item)
        elif item == "apples" or item == "bananas" or item == "grapes" or item == "cherries":
            my_fruit.append(item)
        elif item == "milk" or item == "ice cream" or item == "cookies":
            my_cold_items.append(item)
        elif item == "eggs" or item == "tilapia" or item == "hamburgers" or item == "hotdogs":
            my_proteins.append(item)
        elif item == "bread" or item == "ketchup" or item == "cereal":
            my_boxed_items.append(item)
        elif item == "paper plates" or item == "napkins":
            my_paper_products.append(item)
        else:
            my_toiletry_items.append(item)
    
    print(f"Vegetables: {my_vegetables}")
    print(f"Fruits: {my_fruit}")
    print(f"Cold Items: {my_cold_items}")
    print(f"Proteins: {my_proteins}")
    print(f"Boxed Items: {my_boxed_items}")
    print(f"Paper Products: {my_paper_products}")
    print(f"Toiletry: {my_toiletry_items}")


if __name__=="__main__":
    shopping()