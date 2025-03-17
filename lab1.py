from statistics import median
def spisok ():

    min_v = int(input("Vveditte min_v: "))
    max_v = int(input("Vveditte max_v: "))
    step = int(input("Vveditte shag: "))


    numbers = list (range(min_v, max_v +1, step))
    count_numbers_7 =  len(list(filter(lambda x: x % 7 == 0, numbers)))
    med = median(numbers)
    result = count_numbers_7 - med

    if result < 0:
        return  numbers[::-1]
    else:
        itog = [result] + numbers[:]
    return itog
mm = spisok()
print (mm)