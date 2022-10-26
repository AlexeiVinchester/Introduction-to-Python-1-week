import random
import statistics

list_of_nums = list()
for i in range(16):
    list_of_nums.append(random.randint(1, 60))
print(list_of_nums)
list_of_nums.sort()

half_size = len(list_of_nums) // 2
median = None
print(half_size)

if len(list_of_nums) % 2 == 1:
    median = list_of_nums[half_size]
else:
    median = sum(list_of_nums[half_size - 1 : half_size + 1]) / 2
print("Median: ", median)

print("statistics: ", statistics.median(list_of_nums))