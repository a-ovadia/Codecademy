#Write your function here

def larger_sum(lst1, lst2):
    sum1, sum2 = 0, 0
    for n in lst1:
        sum1 += n
    for n in lst2:
        sum2 += n
    if sum1 >= sum2: return lst1
    else: return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))