# To read from a file
with open("data.txt") as file:
    contents = file.read()
    print(contents)

# To write to a file
with open("data.txt", mode='w') as file:
    contents = file.write('New Text')
    print(contents)
