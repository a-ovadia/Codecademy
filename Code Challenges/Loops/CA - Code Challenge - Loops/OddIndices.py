#Write your function here

def odd_indices(my_list):
    new_list = []
    for index in range(len(my_list)):
        if index % 2 != 0: #odd
            new_list.append(my_list[index])
    return new_list
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))