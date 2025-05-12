sentence = "Play the new game now"
word_list = []
new_word = ""
validWords = []

for i in sentence:
    if not i == " ":
        new_word += i
    else:
        word_list.append(new_word)
        new_word = ""

if new_word:
    word_list.append(new_word)

for word in word_list:
    if len(word) >= 4:
        validWords.append(word)

print(validWords)