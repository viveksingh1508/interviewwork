
from re import S


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


def seactAllocation():

    seats = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
             ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]

    ticket = input("Book Tickets? (y/n)")

    while ticket == 'y':

        number_of_seats = int(input("seats to be booked: "))

        if number_of_seats == 4:
            middle_seats = ['c', 'd', 'e', 'f']
            corner_seats = ['a', 'b', 'g', 'h']
            k = 0
            seat = 0

            for seat in range(0, 3):
                print(seat)
                available = all(x in seats[seat] for x in middle_seats)
                if available:
                    print("Tickets")
                    for alloted_seats in middle_seats:
                        print(str(seat+1)+alloted_seats[k])
                    for remove_seat in range(len(middle_seats)):
                        seats[seat].remove(middle_seats[remove_seat])
                    print(seats)
                    break

                elif all(x in seats[seat] for x in corner_seats):
                    print('Tickets')
                    for alloted_seats in corner_seats:
                        print(str(seat+1)+alloted_seats[k])
                    for remove_seat in range(len(corner_seats)):
                        seats[seat].remove(corner_seats[remove_seat])
                    break

        elif number_of_seats == 3:

            middle_seats = ['c', 'd', 'e']
            k = 0

            for seat in range(0, 3):
                available = all(x in seats[seat] for x in middle_seats)
                if available:
                    for alloted_seats in middle_seats:
                        print(str(seat+1)+alloted_seats[k])
                    for remove_seat in range(len(middle_seats)):
                        seats[seat].remove(middle_seats[remove_seat])
                    break

        elif number_of_seats == 2:
            right_corner = ['a', 'b']
            left_corner = ['g', 'h']
            k = 0

            for seat in range(0, 3):
                available = all(x in seats[seat] for x in right_corner)
                if available:
                    for alloted_seats in right_corner:
                        print(str(seat+1)+alloted_seats[k])
                    for remove_seat in range(len(right_corner)):
                        seats[seat].remove(right_corner[remove_seat])
                    break

                elif all(x in seats[seat] for x in left_corner):
                    for alloted_seats in left_corner:
                        print(str(seat+1)+alloted_seats[k])
                    for remove_seat in range(len(left_corner)):
                        seats[seat].remove(left_corner[remove_seat])
                    break

        elif number_of_seats == 1:
            for seat in range(0, 3):
                if len(seats[seat]):
                    print(str(seat+1)+str(seats[seat][0]))
                    break

            print(seats)


seactAllocation()
