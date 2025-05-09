games = ["Zelda", "Mario", "Tomb Raider", "Halo", "God of War"]
game_lengths = []
o_list = []
reversed_list = []
game_first_letter = []
words_without_of = []

for n in range(0, len(games)):
    game_lengths.append(len(games[n]))
    if "o" in games[n]:
        o_list.append(games[n])
    reversed = games[n][::-1]
    reversed_list.append(reversed)
    game_first_letter.append(games[n][0])
    no_of = games[n].replace(" of", "")
    words_without_of.append(no_of)
    games[n] = games[n].upper()
    if len(games[n]) > 5:
        games[n] = games[n] + "(long name)"


    


print(game_lengths)
print(o_list)
print(reversed_list)
print(game_first_letter)
print(words_without_of)
print(games)


