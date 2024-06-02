def unique_values(my_dictionary):
    unique_list = []
    for value in my_dictionary.values():
        if value not in unique_list:
            unique_list.append(value)
    return len(unique_list)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1