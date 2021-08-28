# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031


class Aresta(object):
  __simbolo = None
  __NoDestino = None

  def __init__(self, simbolo: str, NoDestino):
    self.__simbolo = simbolo
    self.__NoDestino = NoDestino

  def get_simbolo(self):
    return self.__simbolo

  def get_no_destino(self):
    return self.__NoDestino
