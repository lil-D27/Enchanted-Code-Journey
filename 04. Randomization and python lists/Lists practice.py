#Lists - Data structure
# list is used to store a group of data
# fruits = [item1, item2]
#items stored in string can be of any data type

list = [1, True, "Hello", 3.141]
print(list)

#list of states in US
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts"]

#list are ordered data structure
print(states_of_america[2]) #3rd item in the list
print (states_of_america[-1]) #last item in the list

#changing an item in the list
states_of_america[1] = "Pencilvania"
print (states_of_america)

#adding an item to the list
states_of_america.append("Angelaland")
print (states_of_america)

#adding a list to the list
states_of_america.extend(["Alaska", "Hawaii"])
print (states_of_america)
