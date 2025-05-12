sentence = "I played Fortnite and Roblox yesterday"
word_list = []
new_word = ""

for i in sentence:
    if not i == " ":
        new_word += i
    else:
        word_list.append(new_word)
        new_word = ""

if new_word:
    word_list.append(new_word)

word_list.insert(2, "***")
word_list.pop(3)
word_list.insert(4, "***")
word_list.pop(5)

print(*word_list, sep=" ")
