ages = [56,72,24,46]

total = 0 

for i in ages:
    total += i

average = total/len(ages)
print(average)
#49.5



letters = ['a','b','c','d']

print(letters[0:2])

print(letters)  #no changes to original

print("b" in letters) #true