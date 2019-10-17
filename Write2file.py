
filename = input ("filename: ") #asks for filename to create
with open (filename, 'w') as f: #opens file in write mode
    f.write (input("Enter favorite number: ")) # writes user input into file
    f.close() # closes file.

