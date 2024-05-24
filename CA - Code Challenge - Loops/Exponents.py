#Write your function here

def exponents(bases, powers):
    result = []
    for b in bases:
        for p in powers:
            result.append(b ** p)
    return result

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))