
def checkout(items):
    itemPrice = {"A": 50, "B": 30, "C": 20, "D": 15}
    specialPrice = {"A": 130, "B": 45}
    itemsCount = {}
    price = []
    items = list(items)
    for item in items:
        if item in itemsCount:
            itemsCount[item] += 1
        else:
            itemsCount[item] = 1
    for item in itemsCount:
        if item == "A" and itemsCount[item] % 3 == 0:
            totalA = itemsCount[item]//3
            price.append(totalA*specialPrice["A"])
        elif item == "A" and itemsCount[item] % 3 != 0:
            culster = itemsCount[item]//3
            price.append(culster*specialPrice["A"])
            remainder = itemsCount[item] % 3
            price.append(remainder*itemPrice["A"])
        elif item == "B" and itemsCount[item] % 2 == 0:
            totalA = itemsCount[item]//2
            price.append(totalA*specialPrice["B"])
        elif item == "B" and itemsCount[item] % 2 != 0:
            culster = itemsCount[item]//2
            price.append(culster*specialPrice["B"])
            remainder = itemsCount[item] % 2
            price.append(remainder*itemPrice["B"])
        else:
            price.append(itemsCount[item]*itemPrice[item])
    print(sum(price))


# checkout("DABABA")


def seactAllocation(numberofseats):
    firstRow = {"1a": 0, "1b": 0, "1c": 0, "1d": 0,
                "1e": 0, "1f": 0, "1g": 0, "1h": 0}
    secondRow = {"2a": 0, "2b": 0, "2c": 0,
                 "2d": 0, "2e": 0, "2f": 0, "2g": 0, "2h": 0}
    thirdRow = {"3a": 0, "3b": 0, "3c": 0, "3d": 0,
                "3e": 0, "3f": 0, "3g": 0, "3h": 0}

    for seat in firstRow:
        print(seat)


seactAllocation(3)
