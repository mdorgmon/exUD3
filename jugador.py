
MAX_ENERGY = 100
MIN_ENERGY = 0

class Player:

  def __init__(self, idPlayer: int, nickName: str):
    self.__idPlayer = idPlayer
    self.__nickName = nickName
    self.__energy = (MAX_ENERGY - MIN_ENERGY) // 2

  def getIdPlayer(self):
    return self.__idPlayer

  def setIdPlayer(self, idPlayer):
    self.__idPlayer = idPlayer

  def getNickName(self):
    return self.__nickName

  def setNickName(self, nickName):
     self.__nickName = nickName

  def getEnergy(self):
       return self.__energy

  def setEnergy(self, energy):
     self.__energy = energy

  def toString(self):
    return f"[idPlayer: {self.getIdPlayer()}, nickName: '{self.getNickName()}', energy: {self.getEnergy()}]"

  def boost(self, charge):
    if not isinstance(charge, int):
      charge = 0

    charge = int(charge)
    newEnergy = self.getEnergy() + charge
    newEnergy = max(MIN_ENERGY, min(newEnergy, MAX_ENERGY))
    self.setEnergy(newEnergy)

    return charge, newEnergy

player1 = Player(1,"name")

print(player1.boost(20))

print(player1.boost(60))

print(player1.boost(-20))

print(player1.boost("hola"))

print(player1.getEnergy())


class Test:

  def test1:
    testPlayer = Player(0, "x")
    if (testPlayer.getEnergy() != 50):
      print(f"Error, el valor inicial de energia es {testPlayer.getEnergy()} y debería ser 50")
    else: print("Valor correcto de Energy.")

  def test2:
    
