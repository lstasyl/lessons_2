my_list = [12, 13, 15]

if my_list == "":
    my_list[:]
    my_list.insert(0,"")
elif (my_list):
    elem_pop = len(my_list) - 1
    elem_insert = my_list[elem_pop:]
    my_list.pop(elem_pop)
    my_list.insert(0, elem_insert)


print(my_list)
