color_list1 = ["Red", "Green", "Blue", "Yellow"]
color_list2 = ["Blue", "Yellow", "Black"]

result = []

for color in color_list1:
    if color not in color_list2:
        result.append(color)
print("list 1 : ",color_list1)        
print("list 2 : ",color_list2)
print("Colors in color_list1 not in color_list2:", result)
