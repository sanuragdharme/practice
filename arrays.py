# Arrays
# Arrays should have fixed type e.g. Array of Int, Array of Float
# Arrays here doesn't have fixed size.
# TypeCode      C Type      Python Type     Min. size in bytes
#   'b'     signed char         int             1
#   'B'     unsigned char       int             1
#   'u'     Py_UNICODE      Unicode Character   2
#   'h'     signed short        int             2
#   'H'     unsigned short      int             2
#   'i'     signed int          int             2
#   'I'     unsigned int        int             2
#   'l'     signed long         long            4
#   'L'     unsigned long       long            4
#   'f'         float           float           4
#   'd'         double          double          8


from array import *

# To create array of particular data type we need to provide type code

int_array = array("i", [4, 5, 3, 7, 2])
print(int_array)

# Address of an array and size of an array
print("Size of array:", int_array.buffer_info())

# Type code of an array
print("Type code of an array:", int_array.typecode)

# Add new integer
int_array.append(-4)
print("Array post append: ", int_array)

# Remove an integer
int_array.remove(5)
print("Array post Removal: ", int_array)

# Reverse an array
int_array.reverse()
print("Array post reverse: ", int_array)

# Display array
for i in range(len(int_array)):
    print(int_array[i], end=" ")
print("")

# Copy Array
new_int_array = array(int_array.typecode, (a for a in int_array))
# new_int_array = array(int_array.typecode, int_array)
print(new_int_array)
print("")

# User input Array
new_int_array = array("i", [])
size_of_array = int(input("Enter size of the array: "))
for i in range(size_of_array):
    new_value = int(input("Enter value: "))
    new_int_array.append(new_value)
print("New Integer array:", new_int_array)
print("")

search_flag = input("Do you want to search value's index? (Y/N): ")
if search_flag == "Y" or search_flag == "N":
    if search_flag == "Y":
        search_value = int(input("Enter the value for which you want to search: "))

        # Using built-in function - Part I
        print("The index of {}: {}".format(search_value, new_int_array.index(search_value)))

        # Using manually - Part II
        # for index, value in enumerate(new_int_array):
        #     if value == search_value:
        #         print("The index of {}: {}".format(search_value, index))
        #         break
else:
    print("Please enter only Y or N")

