
def append_to_list(val, lst=[]):
    lst.append(val)
    return lst

l1 = append_to_list(1)
l2 = append_to_list(2)
l3 = append_to_list(3, [])

print(l1, l2, l3)

