#Write your function here

def double_index(my_list, index):
    if index < len(my_list):
        my_list[index] *= 2;
    return my_list

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))