import sys

#Нарисовать лестницу из #
amount = int(sys.argv[1])
for i in range(1, amount + 1):
    print(" "*(amount - i) + "#"*(i))
