#immutable -cannot be changed
name='shamitha shatty' # name is reference stored in memory
result=name.capitalize() #frst letter capital and if any space present in the str value it will be remains same
print(name)
print(result)

print(id(name)) #returns identity number if strng (address reference)
print(id(result))

print(name.swapcase())# to change the str from upper to lower, lower to upper( vise versa)

name="shamitha shetty"
print(name.title()) #it returns the strng with frst letter upper case

print(len(name)) # returns the total number of char present in value

#replace
text="hello world"
result=text.replace("world", "python")
print(result)
original_string="Hello python"
new_string = original_string.replace("Hello", "Hi")
print(new_string)

index=text.find("world") # it returns the popsition of the strng value
print(index)

name1="hello "
index1=name.find("world") # if the sub strnf is not availabl it returns the -1
print(index1)

#count-it returns the number of char's present in the stng value
name2="Hello Shamitha shetty"
count=name.count("h")
print(count)

val= None
#None is not same as false
#none is not empty
#none is not 0
#unsupported opreand
print(val)





