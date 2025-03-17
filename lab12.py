numbers_list = []
i = 0
while i <=15:
    numbers_list.append(i)
    i += 1
print ("5.1 Spisok ot 0 do 15 ", numbers_list)
numbers_set = set()
j = 0
while True:
    if j > 10:
        break
    numbers_set.add(j)
    j +=1
print ("5.2 Sozdat mnojestvo ot 0 do 10", numbers_set)


k = 0
while k < len(numbers_list):
    if numbers_list[k] < 11:
        del numbers_list[k]
    else:
        k += 1
print ("5.3 Noviy spisok s elementavb > 11", numbers_list)


my_tuple = (30, 40, 55, 60)
numbers_list.clear()
for element in my_tuple:
    if element >= 50:
        numbers_list.append(element +39)
    else:
        numbers_list.append(element *3)
print ("5.4 Kornechniy spisok s uchetom uslovija  >= 50", numbers_list)
numbers_list.extend(reversed(my_tuple))
print ("    Itogoviy spisok", numbers_list)