#___________________________________#
#Title: Basic Math Script
#Dev: SMalakar
#Date: July 15, 2023
#ChangeLog: (Who, When, What)
#SMalakar, 7/15/2023, Created Script
#___________________________________#

#Get User Input data
numerouno = int(input("Enter number 1 value: ")) #this value is being saved as a reference (defining a variable as an integer)
numerodos = int(input("Enter number 2 value: ")) #this value is being saved as a reference (defining a variable as an integer)

print(type(numerouno)) #should print out the data type
print(type(numerodos)) #should print out the data type

#Process the data
sum = numerouno + numerodos #adding the two values
difference = numerouno - numerodos #subtracting the two values
product = numerouno * numerodos #multiplying the two values
quotient = numerouno / numerodos #dividing the two values 

#Display the data
print(sum)
print (difference)
print (product)
print (quotient)
