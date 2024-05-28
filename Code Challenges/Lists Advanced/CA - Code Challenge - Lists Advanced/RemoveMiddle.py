#Write your function here

# def remove_middle(my_list, start, end):
#     while start <= end:
#         my_list.pop(start)
#         start += 1
#     return my_list

def remove_middle(my_list, start, end): return my_list[: start ] + my_list[ end + 1 :]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))