#Write your function here

#Assume both lists are of equal length
def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if not lst1[index] == lst2[len(lst1) - index -1]:
            return False
    return True



#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))