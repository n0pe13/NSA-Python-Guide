

### Exercise Set 1 ###

# 1
def main():
    print(sum([i for i in range(1, 1001) if i % 3 == 0 or i % 5 == 0]))

# 2
def dups(*args):
    d_lst = []
    d_lst.append(args)
    to_lst = []
    
    unique = []

    for d in d_lst:
        for x in d:
            to_lst.append(x)
    
    for i in to_lst:
        if to_lst.count(i) > 1:
            if i not in unique:
                unique.append(i)
    
    print(unique)

# 3
def convert_classification(marking):

    if marking[0] == "U":
        return "UNCLASSIFED//FOR OFFICIAL USE ONLY"
    else:
        return "SECRET//REL TO USE, FVEY"



if __name__=='__main__':
    #main()
    #dups(1, 1, 2, 3, 4, 4)
    print(convert_classification("U//FOUO"))