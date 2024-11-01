def lists(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
    return common_elements


list1 = [1, 7, 5, 10, 8]
list2 = [4, 5, 6, 7, 8]
result = lists(list1, list2)
print(result) 
