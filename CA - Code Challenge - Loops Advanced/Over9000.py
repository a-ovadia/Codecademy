#Write your function here

def over_nine_thousand(lst):
    sum = 0
    for i in range(len(lst)):
        if sum < 9000:
            sum += lst[i]
        else: break
    return sum
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))