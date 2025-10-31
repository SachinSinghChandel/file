
# # "r" read mode for read the file
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()

# # "w"write mode for over write the text
# f=open("demo.txt","w")
# f.write("6.0 cgpa")
# f.close()

# # for "a" append mode (add at the end)
# f=open("demo.txt","a")
# f.write("in bachlors")
# f.close()
# deleting file
# import os
# os.remove("demo.txt")
#hi everyone
#  we ase learning file I/O
#  using python.
#  I like programming in python.

f=open("practice.txt","w")
f.write("hi everyone \n we ase learning file I/O \n using java.\n I like programming in java.")
f=open("practice.txt","r")
data=f.read()
new_data = data.replace("java","python")
print(new_data)
f= open("practice.txt","w")
f.write(new_data)
f.close()








