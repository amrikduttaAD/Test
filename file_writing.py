#  "w" mode  means write mode which deletes the previous data and writes the new one
# f = open("amrik.txt", "w")
# f.write("amrik to bjw chele")
# f.close()


# if we want to add text in the previous then append mode
# f = open("amrik.txt", "a")
# f.write("amrik bhalo cheke\n")
# f.close


# in this if we want to know the number of character
# f = open("amrik.txt", "w")
# a = f.write("amrik bhai bohut achhe hai")
# print(a)
# f.close()



# handle read and write both
f = open("amrik.txt", "r+")
print(f.read())
f.write("thank u\n")