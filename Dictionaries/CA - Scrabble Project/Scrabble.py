letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key:value for key, value in zip(letters, points)}

letters_to_points[" "] = 0

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def score_word(word):
    point_total = 0
    for char in word:
        point_total += letters_to_points.get(char, 0)
    return point_total

def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word.upper())
    else:
        player_to_words[player] = [word.upper()]


def update_point_totals():
    for player in player_to_words:
        player_points = 0
        print(player_to_words[player])
        for word in player_to_words[player]:
            player_points += score_word(word)
        player_to_points[player] = player_points


def play_scrabble(name, word):
    play_word(name, word)
    update_point_totals()
    print(player_to_points)

brownie_points = score_word("BROWNIE")
print(brownie_points)


play_scrabble("Adam", "Green Day")