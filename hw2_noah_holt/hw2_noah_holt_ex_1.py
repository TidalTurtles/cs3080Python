# Homework_2_1
# Noah_Holt
# Due: 23 sept 2022
# Collartz Program
#   Receive integer input from users, if even print num // 2 and return
#   if odd print and return 3 * num + 1


def collartz(number):

    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number +1


changeThis = input("Give me an Int!\n")

while changeThis != 1:
    changeThis = collartz(int(changeThis))
    print(changeThis)