import jugador
import game

p1 = Player(1,"a")
p2 = Player(2, "b")

g1 = Game(p1, p2, 3)
print("p1: ",p1.toString())
print("p2: ",p2.toString())

g1.play()


