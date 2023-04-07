PetName = []

name = "e"
while name != "quit":
    print("what is ur pet called?")
    name = input()
    if name != "quit":
        PetName.append(name)
    

PetName.sort()
print("List: ", PetName) 
