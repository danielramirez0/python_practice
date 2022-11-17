with open("data.txt") as data:
    words = data.readlines()
file = open(r"new_data.txt", "w")
output = []
[output.append(word) for word in words if word not in output]
output.sort()

for word in output:
    file.write(word)
file.close()