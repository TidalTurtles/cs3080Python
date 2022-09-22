# Homework_2_2
# Noah_Holt
# Due: 23 sept 2022
# Collartz2 Program
#   Add try catch to part 1
#
# Getting that weird thing where it runs the function
# then runs the whole program cant remember how to fix it though

def collartz2(number):

    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number +1


# add try catch here
canConvert = True

while canConvert:
    changeThis = input("Give me an Input!")
    try:
        changeThis= int(changeThis)
        canConvert = False
    except ValueError:
        print("improper input! Integer expected")


while changeThis != 1:
    changeThis = collartz2(int(changeThis))
    print(changeThis)
