jarjar = {
    "Name": "Jar Jar Binks",
    "Age": 86
}

jarjar["Class"] = "Traitor"
jarjar["Location"] = ["Naboo", "Coruscant", "Gungan City"]
jarjar["Weapons"] = ["Clumsy", "3rd Sith"]
jarjar["Tasks"] = {"Obvious Task": "Be Clumsy", "Revealed Task": "Represent Naboo", "Actual Task": "Assist the creation of The Empire"}

print("Jar Jar Binks' Actual task was to: ", jarjar["Tasks"]["Revealed Task"], "and", jarjar["Tasks"]["Actual Task"])


def printDictItems(dict_in):
    for key in dict_in:
        if isinstance(dict_in[key], str):
            print(key, ":", dict_in[key])
        elif isinstance(dict_in[key], list):
            print(key, ":")
            for n in range(0, len(dict_in[key])):
                print("  ", dict_in[key][n])
        elif isinstance(dict_in[key], dict):
            new_dict = dict_in[key]
            printDictItems(new_dict)

printDictItems(jarjar)