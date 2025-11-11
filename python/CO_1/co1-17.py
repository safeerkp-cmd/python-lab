my_dict = {'banana': 3, 'apple': 5, 'cherry': 2, 'date': 4}

asc_dict = dict(sorted(my_dict.items()))
desc_dict = dict(sorted(my_dict.items(), reverse=True))

print("Original dictionary:", my_dict)
print("Ascending order:", asc_dict)
print("Descending order:", desc_dict)
