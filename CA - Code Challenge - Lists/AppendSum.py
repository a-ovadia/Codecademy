#Write your function here
def append_sum(my_list):
    for i in range(3):
        my_list.append(my_list[-1] + my_list[-2])
    return my_list
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))