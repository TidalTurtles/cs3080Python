# Homework_2_3
# Noah_Holt
# Due: 23 sept 2022
# List manipulation Program
#
# 1)  make list of strings, and print with one liner
# 2)  sort() and print again
# 3)  print only 1st item
# 4)  using slicing, print all but first
# 5)  print last with neg index
# 6)  print Keys index with index()
# 7)  append "Tablet", print list
# 8)  insert "Mask" as second item, print list
# 9)  remove "Phone", print list
# 10) reverse and print
# 11) make function strList(), takes list as arg
#       prints in special format for any list

# 11
def strList(formatMe):
    

# 1
everydayItems = ["Wallet", "Phone", "Keys"]
print(everydayItems)
# 2
everydayItems.sort()
print(everydayItems)
# 3
print(everydayItems[0])
# 4
print(everydayItems[1:])
# 5
print(everydayItems[-1])
# 6
print(everydayItems.index('Keys'))
# 7
everydayItems.append('Tablet')
print(everydayItems)
# 8
everydayItems[2] = 'Mask'
print(everydayItems)
# 9
everydayItems.remove('Phone')
print(everydayItems)
# 10
everydayItems.reverse()
print(everydayItems)

