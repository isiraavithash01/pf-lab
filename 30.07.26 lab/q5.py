nums=[12,7,25,18,4,7,30]

print(nums)

highest=max(nums)

print("Highest number is:", highest)

lowest=min(nums)

print("Lowest number is:", lowest)


count=nums.count(7)
print("Number 7 appears", count, "times.")


tot=sum(nums)
avg=tot/ len(nums)

print("Total:", tot)
print("Average:", avg)


for num in reversed(nums):
    print(num)

print("--------------")

print(nums[::-1])
