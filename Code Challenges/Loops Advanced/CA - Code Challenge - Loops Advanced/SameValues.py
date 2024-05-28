#Write your function here

# Assume both lists are of equal sizes
def same_values(lst1, lst2):
    same = []
    for iter in range(len(lst1)):
        if lst1[iter] == lst2[iter]:
            same.append(iter)

    return same

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))