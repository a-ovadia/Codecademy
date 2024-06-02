def sum_values(my_dictionary):
    counter = 0
    for entry in my_dictionary.values():
        counter += entry
    return counter

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))
