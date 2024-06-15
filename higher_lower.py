import random

from art import logo, vs
from game_data import data

print(logo)

#comparacion 1
name_A = random.choice(data)
count_A = name_A['follower_count']
name_B = random.choice(data)
count_B = name_B['follower_count']
score = 0
end_game = False


def game():

  def comparacion1():
    name = name_A['name']
    description = name_A['description']
    country = name_A['country']
    print(f"Compare A:{name}, a {description}, from {country}")

  comparacion1()

  #logo vs

  print(vs)

  #comparacion 2

  def comparacion2():
    name = name_B['name']
    description = name_B['description']
    country = name_B['country']
    print(f"Compare B:{name}, a {description}, from {country}")

  comparacion2()


while not end_game:
  game()
  choose = input("Who has more followers? Type 'A' or 'B': ")

  if count_A > count_B and choose == "A" or count_A < count_B and choose == "B":
    print("You're right! Current score: 1.")
    score += 1
  elif count_A < count_B and choose == "A" or count_A > count_B and choose == "B":
    print(f"You're wrong! Current score: {score}")
    end_game = True
