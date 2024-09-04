
my_list = [10, 20, 30, 40, 50]

#Accessing elements by index
first_element = my_list[0]  
last_element = my_list[-1]  
print("First element:", first_element)
print("Last element:", last_element)

#Modifying an element
my_list[1] = 25 
print("List after modification:", my_list)

#Adding elements
my_list.append(60)  
print("List after appending 60:", my_list)

#Removing elements
my_list.remove(30)  
print("List after removing 30:", my_list)

#Finding the length of the list
list_length = len(my_list)
print("Length of the list:", list_length)
