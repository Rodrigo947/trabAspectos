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
  __nomeTag = ''

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

  def get_nome_tag(self) -> str:
    return self.__nomeTag

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

  def set_nome_tag(self, nomeTag: str):
    self.__nomeTag = nomeTag

  def reset(self):
    self.__noAtual = self.__noInicial
    self.__estado = True

  '''
  Para cada No inicial verifica se eh possivel chegar em um No final
  '''

  def processar_texto(self, texto: str) -> bool:
    for noInicial in self.get_nos_iniciais():
      proximoNo = noInicial
      i = 0
      while (proximoNo and i < len(texto)):
        proximoNo = proximoNo.verificaTransicoes(texto[i])
        i = i+1
        # Caso o proximo No seja um no final e todos os simbolos foram
        # processados, o automato reconhece o texto
        if (proximoNo in self.get_nos_finais() and i == len(texto)):
          return True

    return False

  # Imprime definição formal de um automato

  def definicao_formal(self, nome: int):

    # Nos inicais
    definicaoNoInicial = ""
    for nosiniciais in self.get_nos_iniciais():
      definicaoNoInicial = definicaoNoInicial + nosiniciais.get_nome() + ","
    definicaoNoInicial = definicaoNoInicial[:-1]

    # demais nos
    allNos = ""
    for no in self.get_nos():
      allNos = allNos + no.get_nome() + ","
    allNos = allNos[:-1]

    # alfabeto
    alfabeto = ""
    for letra in self.__alfabeto:
      alfabeto = alfabeto + letra + ","
    alfabeto = alfabeto[:-1]

    # nosfinais
    definicaoNoFinal = ""
    for nosfinais in self.get_nos_finais():
      definicaoNoFinal = definicaoNoFinal + nosfinais.get_nome() + ","
    definicaoNoFinal = definicaoNoFinal[:-1]

    # impressao
    print(f'M{nome} = ( { {allNos}  }, {  {alfabeto}  }, ã{nome} , {definicaoNoInicial}, {  {definicaoNoFinal}  })')
