name = input("give the name:")
count=0
for letter in name:
    if letter in  "aeiouAEIOU":
        count=count+1
print(count)

