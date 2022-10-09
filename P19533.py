from RPSLS_player import RPSLS_player
import random
list = ["scissors", "paper", "rock", "lizard", "spock"]
class P19533(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    return list[random.randint(0,4)]
  
  def update(self, result: str, competitor_shot: str):
    counter = 0
    i = 0
    if counter == 0:
      i = random.randint(0,4)
      if result=="draw":
        counter=counter+1
    elif counter>0 and counter<3 and result=="draw":
      i = (i+4)%5
      counter=counter+1
    elif counter==3 and result=="draw":
      counter=0
