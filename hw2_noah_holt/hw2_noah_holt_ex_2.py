# Homework_2_2
# Noah_Holt
# Due: 23 sept 2022
# Collartz Program
#   Add try catch to part 1

def collartz(number):


    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number +1


#add try catch here


changeThis = input("Give me an Input!")

while changeThis != 1:
    changeThis = collartz(int(changeThis))
    print(changeThis)
