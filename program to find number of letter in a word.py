##### program to count number of letters in word######

string = input("enter any word")
dict_1 = {}
for i in string:
    dict_1.update({i:string.count(i)})
print(dict_1)
