array= [46,14,65,56,54,49,85,86,65,15,44,54]
#Accessing elements by index
first_element = array[0]  
print("1st_element:", first_element)

#Modifying an element
array[2] = 33 
print("Array after modification:", array)

#Adding elements
array.append(89) 
print("Array after appending 89:", array)

#Removing element
array.remove(54)  
print("Array after removing 54:", array)

#Finding the length of the array
array_length = len(array)
print("Length of the array:", array_length)

#Iterating over the array
print("Iterating over the array:")
for element in array:
    print(element)

#Slicing the array 
sub_array = array[1:4] 
print("Subarray:", sub_array)
