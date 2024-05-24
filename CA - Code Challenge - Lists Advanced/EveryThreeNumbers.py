#Write your function here

def every_three_nums(start):
    list = []
    while start <= 100:
        list.append(start)
        start += 3
    return list


def more_efficent(start): return list(range(start, 101, 3))
#Uncomment the line below when your function is done
print(every_three_nums(91))