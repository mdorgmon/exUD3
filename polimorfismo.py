class EquiFigura:

  def __init__(self, longitudLados):
    self.__longitudLados = longitudLados

  def getLongitudLados(self):
    return self.__longitudLados

  def setLongitudLados(self, longitudLados):
    self.__longitudLados = longitudLados

  def toString(self):
    return f"Figura equilátera - Longitud de los lados: {self.getLongitudLados()}"

class TrianguloEquilatero(EquiFigura):
  def __init__(self, longitudLados):
    super().__init__(longitudLados)

  def getPerimetro(self):
    return 3 * self.getLongitudLados()

  def getArea(self):
    longitudLado = self.getLongitudLados()
    return (3 ** 0.5 * longitudLado * longitudLado) / 4

class Cuadrado(EquiFigura):
  def __init__(self, longitudLados):
   super().__init__(longitudLados)

  def getPerimetro(self):
     return 4 * self.getLongitudLados()

  def getArea(self):
    return (float)(self.getLongitudLados() ** 2)

def getPerimetroFigura(figura):
  return figura.getPerimetro()

def getAreaFigura(figura):
  return figura.getArea()


te1 = TrianguloEquilatero(3)
cu1 = Cuadrado(4)

print("Triángulo equilátero te1:")
print(f"  - Perímetro: {getPerimetroFigura(te1)}")
print(f"  - Área: {getAreaFigura(te1)}")
print(" Cuadrado cu1: ")
print(f"  - Perímetro: {getPerimetroFigura(cu1)}")
int(f"  - Área: {getAreaFigura(cu1)}") #debería poner 16 también pero salta un error que no considgo resolver