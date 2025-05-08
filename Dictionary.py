Percy_Jackson = {
   "Name": "Percy Jackson",
   "Age": 17,
   "Class": "Demigod",
}

print(Percy_Jackson["Name"])
Percy_Jackson["Weapon"] = "Riptide (Anaklusmos)"
Percy_Jackson.pop("Class")
Percy_Jackson["Age"] = 18

exit1 = True
while exit1 == False:
    for key in Percy_Jackson:
        if key == "Class":
            print("Class is in dictionary")
            exit1 = True
    if exit1 == False:
        print("Class not in dictionary")
        exit1 = True

exit2 = False
while exit2 == False:
    for key in Percy_Jackson:
        if Percy_Jackson.get(key) == "Percy Jackson":
            print("Percy Jackson is in dictionary under ", key)
            exit2 = True
    if exit2 == False:
        print("Percy Jackson not in dictionary")
        exit2 = True

