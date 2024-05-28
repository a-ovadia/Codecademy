#Write your function here

def max_num(nums):
    max = nums[0]
    for number in nums:
        if number >= max: max = number
    return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))