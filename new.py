# def machine(input):
#     global prices
#     start= input
#     input= input-1
#     user_value= prices[input]
#     print("Product: ", start, "Price: ",user_value)
#     return user_value
#
# prices = [10,14,22,33,44,13,22,55,66,77]
# print("Supermarket\n===========")
# totalsum = 0
# while True:
#     first_input= int(input("Please select product (1-10) 0 to Quit: "))
#     if first_input != 0:
#         user_value = machine(first_input)
#         totalsum = totalsum + user_value
#     else:
#         print("Total:",totalsum)
#         pay=int(input("Payment:"))
#         print("Change:",pay-totalsum)
#         break


# class Employee:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
#
#     def printout(self):
#         user = "Id: "+str(self.id)+" Name: "+self.name
#         return user
#
# mylist=[]
# idnumber= 1
#
# while True:
#     user_name = input("Please enter employee name (0 to quit):")
#     if user_name != str(0):
#         x= Employee(idnumber,user_name)
#         idnumber += 1
#         end_value=x.printout()
#         last_print=mylist.append(end_value)
#     else:
#         for i in mylist:
#             print(i)
#         break


# Python program for implementation of Bubble Sort

# def bubbleSort(arr):
#     n = len(arr)
#     # optimize code, so if the array is already sorted, it doesn't need
#     # to go through the entire process
#     swapped = False
#     # Traverse through all array elements
#     for i in range(n - 1):
#         # range(n) also work but outer loop will
#         # repeat one time more than needed.
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
#         if not swapped:
#             # if we haven't needed to make a single swap, we
#             # can just exit the main loop.
#             return
#
#
#
#
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
# print(bubbleSort(arr))
#
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("[",arr[i], end="]")



