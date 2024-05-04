file = open('Hello.txt', 'r')
numbers = file.readlines()

sum=0
for num in numbers:
    sum += int(num.strip())

print(sum)
file.close