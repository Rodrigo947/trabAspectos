# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Utils.Logs import Logs
from src.Core.Automato import Automato
from src.Grafo.No import No


class Automatos(object):
  __automatos = []

  def adiciona_automato(self, nomeTag: str, expressao: str):
    nome = 0
    pilha = []
    charAnterior = ''
    alfabeto = []

    # Percorre a tag e constroi o AFN-Lambda
    for char in expressao:
      auxNoInicial = None
      auxNoFinal = None
      automato = None
      auxPilha1 = None
      auxPilha2 = None

      if(charAnterior == '\\'):
        automato = Automato()
        auxNoInicial = No('q'+str(nome))
        automato.adiciona_no_inicial(auxNoInicial)
        automato.adiciona_no(auxNoInicial)
        nome = nome + 1
        auxNoFinal = No('q'+str(nome))
        nome = nome + 1
        automato.adiciona_no_final(auxNoFinal)
        automato.adiciona_no(auxNoFinal)
        auxNoInicial.adicionar_trasicao(char, auxNoFinal)
        pilha.append(automato)
        charAnterior = ''
        if char not in alfabeto:
          alfabeto.append(char)

      else:
        if (char == '.' or char == '+'):
          if len(pilha) < 2:
            Logs.error('Erro ao converter ER para AFD')
            return False
          else:
            if char == '+':
              auxPilha1 = pilha.pop()
              auxPilha2 = pilha.pop()
              automato = Automato()
              auxNoInicial = No('q'+str(nome))
              nome = nome + 1
              auxNoFinal = No('q'+str(nome))
              nome = nome + 1
              auxNoInicial.adicionar_trasicao(
                  'ã', auxPilha1.get_nos_iniciais()[0])
              auxNoInicial.adicionar_trasicao(
                  'ã', auxPilha2.get_nos_iniciais()[0])
              auxPilha1.get_nos_finais()[0].adicionar_trasicao('ã', auxNoFinal)
              auxPilha2.get_nos_finais()[0].adicionar_trasicao('ã', auxNoFinal)
              automato.adiciona_no_inicial(auxNoInicial)
              automato.adiciona_no_final(auxNoFinal)
              automato.adiciona_no(auxNoInicial)
              automato.adiciona_no(auxNoFinal)
              for no1 in auxPilha1.get_nos():
                automato.adiciona_no(no1)
              for no2 in auxPilha2.get_nos():
                automato.adiciona_no(no2)
              del auxPilha1
              del auxPilha2
              pilha.append(automato)
            else:
              auxPilha1 = pilha.pop()
              auxPilha2 = pilha.pop()
              auxPilha2.get_nos_finais()[0].adicionar_trasicao(
                  'ã', auxPilha1.get_nos_iniciais()[0])
              auxPilha2.remove_no_final(auxPilha2.get_nos_finais()[0])
              auxPilha2.adiciona_no_final(auxPilha1.get_nos_finais()[0])
              for no in auxPilha1.get_nos():
                auxPilha2.adiciona_no(no)
              pilha.append(auxPilha2)

        elif (char == '*'):
          if len(pilha) < 1:
            Logs.error('Erro ao converter ER para AFD')
            return False
          else:
            auxPilha1 = pilha.pop()
            auxPilha1.get_nos_finais()[0].adicionar_trasicao(
                'ã', auxPilha1.get_nos_iniciais()[0])
            auxPilha1.remove_no_final(auxPilha1.get_nos_finais()[0])
            auxPilha1.adiciona_no_final(auxPilha1.get_nos_iniciais()[0])
            pilha.append(auxPilha1)

        # Se não for nenhum caractere especial, insere normalmente na pilha
        else:
          # Cria autômato para um caractere
          if(char != '\\'):
            automato = Automato()
            auxNoInicial = No('q'+str(nome))
            automato.adiciona_no_inicial(auxNoInicial)
            automato.adiciona_no(auxNoInicial)
            nome = nome + 1
            auxNoFinal = No('q'+str(nome))
            nome = nome + 1
            automato.adiciona_no_final(auxNoFinal)
            automato.adiciona_no(auxNoFinal)
            auxNoInicial.adicionar_trasicao(char, auxNoFinal)
            pilha.append(automato)
            if char not in alfabeto:
              alfabeto.append(char)

        charAnterior = char

    # Se sobrou apenas um autômato na pilha
    if len(pilha) == 1:
      pilha[0].set_alfabeto(alfabeto)
      self.imprime_automato("AFN-Lambda", pilha[0])
      automatoAFN = self.remove_lambda(pilha[0])
      pilha.clear()
      self.imprime_automato("AFN", automatoAFN)
      automatoAFD = self.gerar_AFD(automatoAFN)
      self.imprime_automato("AFD", automatoAFD)
      automatoAFD.set_nome_tag(nomeTag)
      self.__automatos.append(automatoAFD)

  # Retorna um autômato específico
  def get_automato(self, indice: int):
    if indice >= 0 and indice < len(self.__automatos):
      return self.__automatos[indice]

  # Retorna todos os autômatos na memória
  def get_automatos(self):
    return self.__automatos

  # Função para imprimir o autômato
  def imprime_automato(self, titulo: str, automato: Automato):
    print("\n"+titulo+": ")
    for no in automato.get_nos():
      inicial_e_final = ''
      if no in automato.get_nos_iniciais():
        inicial_e_final += '+'
      if no in automato.get_nos_finais():
        inicial_e_final += '-'
      for transicao in no.get_transicoes():
        print(no.get_nome()+inicial_e_final+': '+transicao.get_simbolo() +
              ' -> '+transicao.get_no_destino().get_nome())
      if len(no.get_transicoes()) == 0:
        print(no.get_nome()+inicial_e_final)

  # Função auxiliar para descobrir quais nós é possível alcançar com transições lambdas a partir de um nó
  def __alcanca_com_lambda(self, no, vetorAlcancaLambda):
    if no not in vetorAlcancaLambda:
      vetorAlcancaLambda.append(no)
    for transicao in no.get_transicoes():
      if transicao.get_simbolo() == 'ã':
        if transicao.get_no_destino() not in vetorAlcancaLambda:
          vetorAlcancaLambda.append(transicao.get_no_destino())
          self.__alcanca_com_lambda(
              transicao.get_no_destino(), vetorAlcancaLambda)

  # Função auxiliar para remover todas as transições para um nó (usado quando se vai apagar um nó)
  def __remove_transicao_para_no(self, automato, noAlvo):
    for no in automato.get_nos():
      a_remover = []
      for transicao in no.get_transicoes():
        if transicao.get_no_destino() == noAlvo:
          a_remover.append(transicao)
      for transicao in a_remover:
        no.remove_trasicao(transicao)

  # Função para remover transições lambdas, retornando um AFN
  def remove_lambda(self, automato):
    # Set para armazenar os fechos lambdas
    fechoLambda = {}
    auxVetor = []

    # Constroi fecho lambda para cada nó
    for no in automato.get_nos():
      auxVetor = []
      self.__alcanca_com_lambda(no, auxVetor)
      fechoLambda[no.get_nome()] = auxVetor

    # Imprime fecho lambda
    print("\nFecho Lambda:")
    for fechoL in fechoLambda:
      print('FL('+fechoL+'): ', end='')
      for st in fechoLambda[fechoL]:
        print(st.get_nome(), end=' ')
      print('')

    # Cria o AFN básico com todos os nós do AFN-Lambda anterior
    automatoAFN = Automato()
    for nov in automato.get_nos():
      automatoAFN.adiciona_no(No(nov.get_nome()))

    automatoAFN.set_alfabeto(automato.get_alfabeto())

    # Cria todas as transições do AFN com base no AFN-Lambda e nos fechos lambdas
    for non in automatoAFN.get_nos():
      auxNo = automato.get_no_por_nome(non.get_nome())
      for auxTransicao in auxNo.get_transicoes():
        if auxTransicao.get_simbolo() != 'ã':
          non.adicionar_trasicao(auxTransicao.get_simbolo(), automatoAFN.get_no_por_nome(
              auxTransicao.get_no_destino().get_nome()))
          for noFecho in fechoLambda[auxTransicao.get_no_destino().get_nome()]:
            if noFecho.get_nome() != auxTransicao.get_no_destino().get_nome():
              non.adicionar_trasicao(auxTransicao.get_simbolo(
              ), automatoAFN.get_no_por_nome(noFecho.get_nome()))

    # Insere os nós Finais no novo AFN
    for nof in automato.get_nos_finais():
      automatoAFN.adiciona_no_final(
          automatoAFN.get_no_por_nome(nof.get_nome()))

    # Insere os nós Iniciais no novo AFN
    for noi in automato.get_nos_iniciais():
      for noFecho in fechoLambda[noi.get_nome()]:
        automatoAFN.adiciona_no_inicial(
            automatoAFN.get_no_por_nome(noFecho.get_nome()))

    # remove estados inuteis
    a_remover = []
    for no in automatoAFN.get_nos():
      if len(no.get_transicoes()) == 0 and no not in automatoAFN.get_nos_finais():
        if no in automatoAFN.get_nos_iniciais():
          automatoAFN.remove_no_inicial(no)
        self.__remove_transicao_para_no(automatoAFN, no)
        a_remover.append(no)

    for no in a_remover:
      automatoAFN.remover_no(no)

    # Deleta o AFN-Lambda e retorna o AFN
    del automato
    return automatoAFN

  # Função auxiliar que gera a string dos estados para ser utilizado nos sets dos estados
  def __gerar_string_nos(self, nos):
    vetor_string = []
    string_final = "{"
    for no in nos:
      vetor_string.append(no.get_nome())
    vetor_string = sorted(vetor_string)
    for str in vetor_string:
      string_final += str + ","
    string_final = string_final.rstrip(',')
    string_final += "}"
    return string_final

  # Função auxiliar para gerar os estados, utilizado na conversão do AFN para AFD
  def __gerar_estados(self, estados, nos, alfabeto):
    stringNos = self.__gerar_string_nos(nos)
    if stringNos not in estados:
      transicoes = {}
      for char in alfabeto:
        aux_transicoes = []
        for no in nos:
          for transicao in no.get_transicoes():
            if transicao.get_simbolo() == char:
              aux_transicoes.append(transicao.get_no_destino())
        transicoes[char] = aux_transicoes
      nTransicoes = []
      for aux in transicoes:
        nTransicoes.append(transicoes[aux])
      estados[stringNos] = nTransicoes

      for nNos in estados[stringNos]:
        if len(nNos) > 0:
          self.__gerar_estados(estados, nNos, alfabeto)

  # Função para criar o AFD a partir de um AFN
  def gerar_AFD(self, automato):
    # Set para armazenar os estados
    estados = {}
    alfabeto = automato.get_alfabeto()
    self.__gerar_estados(
        estados, automato.get_nos_iniciais(), alfabeto)

    # Cria o AFD básico com base nos estados gerados
    automatoAFD = Automato()
    automatoAFD.set_alfabeto(alfabeto)
    for nomeNo in estados:
      automatoAFD.adiciona_no(No(nomeNo))

    # Cria transições
    for no in estados:
      for i in range(len(alfabeto)):
        if len(estados[no][i]) > 0:
          automatoAFD.get_no_por_nome(no).adicionar_trasicao(
              alfabeto[i], automatoAFD.get_no_por_nome(self.__gerar_string_nos(estados[no][i])))

    # Adiciona o nó Inicial e os nós finais ao AFD
    automatoAFD.adiciona_no_inicial(automatoAFD.get_no_por_nome(
        self.__gerar_string_nos(automato.get_nos_iniciais())))
    for noAFD in automatoAFD.get_nos():
      for noAFN in automato.get_nos_finais():
        if (noAFN.get_nome()+"," in noAFD.get_nome() or noAFN.get_nome()+"}" in noAFD.get_nome()) and noAFD not in automatoAFD.get_nos_finais():
          automatoAFD.adiciona_no_final(noAFD)

    # Renomeia os nós
    nome = 0
    for no in automatoAFD.get_nos():
      no.set_nome('q'+str(nome))
      nome = nome + 1

    # Deleta o AFN e retorna o AFD
    del automato
    return automatoAFD

  # Imprime definição formal de todos os automatos registrados na memória
  def listardefinicoes(self):
    count = 0
    if(len(self.__automatos) > 0):
      for automato in self.__automatos:
        automato.definicao_formal(count)
        count = count + 1
    else:
      Logs.warning("Nao há algum autômato registrado na memória!")
