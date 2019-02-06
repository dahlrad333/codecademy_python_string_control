letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {each:every for each, every in zip(letters, points)}
letters_to_points[" "] = 0

print(letters_to_points)

def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letters_to_points.get(letter)
  return point_total
    
player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}

player_to_points = {}

def update_points(dictionary):
  for player, words in dictionary.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
    
update_points(player_to_words)
print(player_to_points)

def play_word(player, word):
  player_to_words[player] += word
  
play_word("player1", "combat")
play_word("wordNerd", "comatose")
play_word("Lexi Con", "unearthed")
play_word("Prof Reader", "periodical")

update_points(player_to_words)
print(player_to_points)