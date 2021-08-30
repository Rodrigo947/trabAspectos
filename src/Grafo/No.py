# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Grafo.Aresta import Aresta
from src.Utils.Logs import Logs


class No(object):
  __transicoes = []
  __nome = None

  def __init__(self, nome: str):
    self.__nome = nome
    self.__transicoes = []

  def adicionar_trasicao(self, simbolo: str, no):
    self.__transicoes.append(Aresta(simbolo, no))

  def get_nome(self):
    return self.__nome

  def set_nome(self, nome: str):
    self.__nome = nome

  def get_transicaoes(self):
    return self.__transicoes

  def get_transicao(self, simbolo: str):
    for transicao in self.__transicoes:
      if transicao.get_simbolo() == simbolo:
        return transicao
    return None

  def remove_trasicao(self, transicao):
    self.__transicoes.remove(transicao)
