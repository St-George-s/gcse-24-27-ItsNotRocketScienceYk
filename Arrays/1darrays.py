#Question 1 - Create an array of five integers [1, 2, 3, 4, 5]. Print the array. 
# numbers = [1, 2, 3, 4, 5]
# for counter in range (len(numbers)):
#     print(numbers[counter])

#Question 2 - Given the array [10, 20, 30, 40, 50], print the first and last elements of the array. 
# numbers = [10, 20, 30, 40, 50]
# # for counter in range (1): not needed :P
# print(numbers[0]) 
# print(numbers [4])

#Question 3 - Given the array [10, 20, 30, 40, 50], change the element at index 2 to 100. Print the modified array. 
# myNumbers = [10, 20, 30, 40, 50]
# myNumbers[2] = 100
# print(myNumbers)

#Question 4 - Given the array [5, 10, 15, 20, 25], print all elements of the array using a loop. 
# devandersNumbers = [5, 10, 15, 20, 25]
# for devanders in range(len(devandersNumbers)):
#     print(devandersNumbers[devanders]) 

#Question 5 - Given the array [2, 4, 6, 8, 10], calculate the sum of all elements. Print the result. 
numerosSum = [2, 4, 6, 8, 10]
total = 0
for counter in range(len(numerosSum)):
    total = total + numerosSum[counter]
print(total)
