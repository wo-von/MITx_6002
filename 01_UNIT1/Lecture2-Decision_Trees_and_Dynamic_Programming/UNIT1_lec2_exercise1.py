# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

testItem = ["sina", "kasra", "tara"]
testGen = powerSet(testItem)
while (True):
    try:
        print(testGen.__next__())
    except:
        break

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    """
    from "000" to "222" in ternary, 0 means in neither bag, 1 means in bag1 and 2 in bag 2

    """
    # Your code here
    N = len(items)
    for i in range(3**N):
        bag1=[]
        bag2=[]
        i_copy = i
        for j in range(N):
            if i_copy%3 == 0:
                pass
            elif i_copy%3 == 1:
                bag1.append(items[j])
            else:
                bag2.append(items[j])
            i_copy = (i_copy-i_copy%3)//3
        yield (bag1, bag2)
    # Solution
    # N = len(items)
    # # Enumerate the 3**N possible combinations   
    # for i in range(3**N):
    #     bag1 = []
    #     bag2 = []
    #     for j in range(N):
    #         if (i // (3 ** j)) % 3 == 1:
    #             bag1.append(items[j])
    #         elif (i // (3 ** j)) % 3 == 2:
    #             bag2.append(items[j])
    #     yield (bag1, bag2)

        