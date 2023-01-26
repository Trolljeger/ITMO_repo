#===================
# Task 1

str1 = "Python is the best programming language in the world"
print(str1[5:-7], "\n")

#===================
# Task 2

str2 = "Guido van Rossum is the benevolent dictator for life"
print(str2[2::3], "\n")

#===================
# Task 3

str3 = "You have a problem with authority, Mr. Anderson."
print(str3)

char_set = set(str3) #����� ���������� �������� � ������
#print(char_set)
#print(list(map(str3.count, char_set)))

dctr = dict(zip(char_set, map(str3.count, char_set)))
print(dctr)




