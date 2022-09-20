# Homework_2_1
# Noah_Holt
# Due: 23 sept 2022
# Collartz Program
#   Receive integer input from users, if even print num // 2 and return
#   if odd print and return 3 * num + 1

# Thoughts:
#   write while loop to call function until return from function is 1
#   ie while number != 1 call collartz function and change number

do {
    changeThis = input('Which number?')
    changeThis = collartz(changeThis)
} while(changeThis != 1);

def collartz(number):

    if(number % 2 == 0):
        return (number // 2)
    else:
        return 3 * number +1

