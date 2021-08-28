# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Utils.Logs import Logs
from src.Core.Automato import Automato
from src.Grafo.No import No
from src.Grafo.Aresta import Aresta


class Automatos(object):
  __automatos = []

  def adiciona_automato(self, expressao: str):
    nome = 0
    pilha = []
    charAnterior = ''

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
              for noAux1 in auxPilha1.get_nos_finais():
                noAux1.adicionar_trasicao('ã', auxNoFinal)
              for noAux2 in auxPilha2.get_nos_finais():
                noAux2.adicionar_trasicao('ã', auxNoFinal)
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
              for noFinal in auxPilha2.get_nos_finais():
                auxPilha2.remove_no_final(noFinal)
                noFinal.adicionar_trasicao(
                    'ã', auxPilha1.get_nos_iniciais()[0])
              for noFinal in auxPilha1.get_nos_finais():
                auxPilha2.adiciona_no_final(noFinal)
              for no in auxPilha1.get_nos():
                auxPilha2.adiciona_no(no)
              pilha.append(auxPilha2)

        elif (char == '*'):
          if len(pilha) < 1:
            Logs.error('Erro ao converter ER para AFD')
            return False
          else:
            auxPilha1 = pilha.pop()
            for noFinal in auxPilha1.get_nos_finais():
              auxPilha1.remove_no_final(noFinal)
              for noInicial in auxPilha1.get_nos_iniciais():
                noFinal.adicionar_trasicao('ã', noInicial)
            for noInicial in auxPilha1.get_nos_iniciais():
              auxPilha1.adiciona_no_final(noInicial)
            pilha.append(auxPilha1)

        # Se não for nenhum caractere especial, insere normalmente na pilha
        else:
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

        charAnterior = char

    if len(pilha) == 1:
      self.__automatos.append(pilha[0])
      self.imprime_automato("AFN-Lambda", pilha[0])
      automatoAFN = self.remove_lambda(pilha[0])
      pilha.clear()
      self.imprime_automato("AFN", automatoAFN)

  def get_automato(self, indice: int):
    if indice >= 0 and indice < len(self.__automatos):
      return self.__automatos[indice]

  def imprime_automato(self, titulo: str, automato: Automato):
    print("\n"+titulo+": ")
    for no in automato.get_nos():
      inicial_e_final = ''
      if no in automato.get_nos_iniciais():
        inicial_e_final += '+'
      if no in automato.get_nos_finais():
        inicial_e_final += '-'
      for transicao in no.get_transicaoes():
        print(no.get_nome()+inicial_e_final+': '+transicao.get_simbolo() +
              ' -> '+transicao.get_no_destino().get_nome())
      if len(no.get_transicaoes()) == 0:
        print(no.get_nome()+inicial_e_final)

  def __alcanca_com_lambda(self, no, vetorAlcancaLambda):
    if no not in vetorAlcancaLambda:
      vetorAlcancaLambda.append(no)
    for transicao in no.get_transicaoes():
      if transicao.get_simbolo() == 'ã':
        if transicao.get_no_destino() not in vetorAlcancaLambda:
          vetorAlcancaLambda.append(transicao.get_no_destino())
          self.__alcanca_com_lambda(
              transicao.get_no_destino(), vetorAlcancaLambda)

  def __remove_transicao_para_no(self, automato, noAlvo):
    for no in automato.get_nos():
      a_remover = []
      for transicao in no.get_transicaoes():
        if transicao.get_no_destino() == noAlvo:
          a_remover.append(transicao)
      for transicao in a_remover:
        no.remove_trasicao(transicao)

  def remove_lambda(self, automato):
    fechoLambda = {}
    auxVetor = []
    print("\nFecho Lambda:")
    for no in automato.get_nos():
      auxVetor = []
      self.__alcanca_com_lambda(no, auxVetor)
      fechoLambda[no.get_nome()] = auxVetor

    for fechoL in fechoLambda:
      print('FL('+fechoL+'): ', end='')
      for st in fechoLambda[fechoL]:
        print(st.get_nome(), end=' ')
      print('')

    automatoAFN = Automato()
    for nov in automato.get_nos():
      automatoAFN.adiciona_no(No(nov.get_nome()))

    for non in automatoAFN.get_nos():
      auxNo = automato.get_no_por_nome(non.get_nome())
      for auxTransicao in auxNo.get_transicaoes():
        if auxTransicao.get_simbolo() != 'ã':
          non.adicionar_trasicao(auxTransicao.get_simbolo(), automatoAFN.get_no_por_nome(
              auxTransicao.get_no_destino().get_nome()))
          for noFecho in fechoLambda[auxTransicao.get_no_destino().get_nome()]:
            if noFecho.get_nome() != auxTransicao.get_no_destino().get_nome():
              non.adicionar_trasicao(auxTransicao.get_simbolo(
              ), automatoAFN.get_no_por_nome(noFecho.get_nome()))

    for nof in automato.get_nos_finais():
      automatoAFN.adiciona_no_final(
          automatoAFN.get_no_por_nome(nof.get_nome()))

    for noi in automato.get_nos_iniciais():
      for noFecho in fechoLambda[noi.get_nome()]:
        automatoAFN.adiciona_no_inicial(
            automatoAFN.get_no_por_nome(noFecho.get_nome()))

    # remove estados inuteis
    a_remover = []
    for no in automatoAFN.get_nos():
      if len(no.get_transicaoes()) == 0 and no not in automatoAFN.get_nos_finais():
        if no in automatoAFN.get_nos_iniciais():
          automatoAFN.remove_no_inicial(no)
        self.__remove_transicao_para_no(automatoAFN, no)
        a_remover.append(no)

    for no in a_remover:
      automatoAFN.remover_no(no)

    del automato
    return automatoAFN
