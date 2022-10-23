import sys

#Вычислить сумму чисел в строке, введенной с консоли
numbers = sys.argv[1]
sum = 0
for i in numbers:
    sum += int(i)
print(sum)