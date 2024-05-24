#Write your function here

def delete_starting_evens(my_list):
    while my_list and my_list[0] % 2 == 0:
        my_list.pop(0)  # Remove the first element if it's even
    return my_list  # Return the modified list

#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10, 5]))
