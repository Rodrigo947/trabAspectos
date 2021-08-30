# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Grafo.No import No


class Automato(object):
  __nosIniciais = []
  __nosFinais = []
  __nos = []
  __alfabeto = []

  # variáveis usadas para analizar strings
  __estado = True
  __noAtual = __nosIniciais

  def __init__(self):
    self.__nosIniciais = []
    self.__nosFinais = []
    self.__nos = []
    self.__alfabeto = []
    self.__estado = True
    self.__noAtual = self.__nosIniciais

  def get_nos_iniciais(self):
    return self.__nosIniciais

  def adiciona_no_inicial(self, no: No):
    self.__nosIniciais.append(no)

  def remove_no_inicial(self, no: No):
    if no in self.__nosIniciais:
      self.__nosIniciais.remove(no)

  def get_nos_finais(self):
    return self.__nosFinais

  def adiciona_no_final(self, no: No):
    self.__nosFinais.append(no)

  def remove_no_final(self, no: No):
    if no in self.__nosFinais:
      self.__nosFinais.remove(no)

  def adiciona_no(self, no):
    self.__nos.append(no)

  def remover_no(self, no):
    self.__nos.remove(no)

  def get_nos(self):
    return self.__nos

  def get_no_por_nome(self, nome: str):
    for no in self.__nos:
      if no.get_nome() == nome:
        return no
    return None

  def set_alfabeto(self, alfabeto):
    self.__alfabeto = alfabeto

  def get_alfabeto(self):
    return self.__alfabeto

  def get_estado(self):
    return self.__estado

  def set_estado(self, estado: str):
    self.__estado = estado

  def set_no_atual(self, no: No):
    self.__noAtual = no

  def reset(self):
    self.__noAtual = self.__noInicial
    self.__estado = True
