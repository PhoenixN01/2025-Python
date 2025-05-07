input = ["level", "power", "deed", "fight", "meme", "run"]
output = [item for item in input if item == item[::-1]]
print(output)