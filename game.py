import random

class Game:
  def __init__(self, player1, player2, rounds):
    self.player1 = player1
    self.player2 = player2
    self.rounds = rounds

  def playRound(self):

    charge1 = random.randint(-25, 25)
    charge2 = random.randint(-25, 25)

    boost_results1 = self.player1.boost(charge1)
    boost_results2 = self.player2.boost(charge2)

    return [(charge1, boost_results1[1]), (charge2, boost_results2[1])]

  def winner(self):
    if self.player1.getEnergy() > self.player2.getEnergy():
      return self.player1
    else:
      return self.player2

  def play(self):
    for round_num in range(1, self.rounds + 1):
      print(f"Round {round_num}: {self.playRound()}")

    winner = self.winner()
    print(f"\n¡Ganador! Jugador: {winner.getNickName()} - Energía: {winner.getEnergy()}")


