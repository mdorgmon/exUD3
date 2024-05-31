import jugador
import game

#Antonio esto sería la estructura pero no tengo ni idea de como hacer que sean funciones 
#equivalentes al static de Java.
class Test:

  def test1(self):
    testPlayer = Player(0, "x")
    if (testPlayer.getEnergy() != 50):
      print(f"Error, el valor inicial de energia es {testPlayer.getEnergy()} y debería ser 50")
    else:
      print("Valor correcto de Energy.")

  def test2(self):
    testPlayer = Player(0, "x")
    if (testPlayer.boost(-100) != MIN_ENERGY):
      print(f"Error, el valor de Energy debería ser 0 y es {testPlayer.getEnergy()}")
    else:
      print("Prueba exitosa, el valor de Energy coincide con MIN_ENERGY")

  def test3(self):
    testPlayer = Player(0, "x")
    if (testPlayer.boost(200) != MAX_ENERGY):
      print(f"Error, el valor de Energy debería ser 100 y es {testPlayer.getEnergy()}")
    else:
      print("Prueba exitosa, el valor de Energy coincide con MAX_ENERGY")

  def test4(self):
    p1 = Player(1, "a")
    p2 = Player(2, "b")

    g1 = Game(p1, p2, 3)
    print("p1: ", p1.toString())
    print("p2: ", p2.toString())

    g1.play()


t1= Test
t1.test1()
t1.test2()
t1.test3()
#t1.test4()