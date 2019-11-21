#reate a program that asks the user for a number and then prints out a list of all the divisors of that number
num = int(input("Enter a number to divide:"))

listRange = list(range(1,num+1))
#empty list [], empty dict {}, empty tuple()
divisorList= []

for number in listRange:
    if num % number ==0:
        divisorList.append(number)
print(divisorList)

#to find the sq of the list
# for numbers in divisorList:
#     num2 = pow(divisorList**divisorList)
#     divisorList.append(num2)

print(divisorList)