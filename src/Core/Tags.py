# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Utils.Logs import Logs

# TODO Imprimir definições de tags quando estiver validando
class Tags(object):
  __tags = {}

  def adicionar_tag(self, nomeTag: str, expressaoTag: str):
    if self.valida_tag(nomeTag, expressaoTag):
      self.__tags[nomeTag] = expressaoTag

  def remover_tag(self, nomeTag):
    if nomeTag in self.__tags:
      del self.__tags[nomeTag]

  def get_tag(self, nomeTag):
    if nomeTag in self.__tags:
      return self.__tags[nomeTag]
    else:
      Logs.info(f'Tag {nomeTag} nao foi definida.')

  def get_todas_tags(self):
    return self.__tags

  # TODO verificar \n\\*
  # TODO Verifica se existe a mesma tag antes de validar. Alguma pergunta do tipo:
  # "deseja sobrescrever?"
  def valida_tag(self, nomeTag: str, expressaoTag: str):
    pilha = []
    expressao = ''
    charAnterior = ''
    charsEscape = ['n', '\\', '*', '.', '+', 'l']
    expressaoTag = expressaoTag.rstrip('\n')  # Removendo o ENTER do input
    # Pecorrendo cada char da expressao
    for char in expressaoTag:

      # Se char atual for um escape definido ele é adicioando na pilha
      if(charAnterior == '\\'):
        if (char in charsEscape):
          expressao = pilha.pop() + char
          pilha.append(expressao)
          charAnterior = ''
        else:
          Logs.error(
              f'Tag {nomeTag} nao recohecida: expressao invalida. Caractere escape nao reconhecido')
          return False

      else:
        if (char == '.' or char == '+'):
          if len(pilha) < 2:
            Logs.error(
                f'Tag {nomeTag} nao recohecida: expressao invalida. Operador + ou . precisa de dois elementos')
            return False
          else:
            expressao = pilha.pop() + char + pilha.pop()
            pilha.append(expressao)

        elif (char == '*'):
          if len(pilha) < 1:
            Logs.error(
                f'Tag {nomeTag} nao recohecida: expressao invalida. Operador * precisa de um elemento')
            return False
          else:
            expressao = pilha.pop() + char
            pilha.append(expressao)

        # Se não for nenhum caractere especial, insere normalmente na pilha
        else:
          if(char != '\\'):
            pilha.append(char)

        charAnterior = char

    # Ao passar por cada posição da expressao, verifica se a pilha possui apenas
    # uma elemento, se verdadeiro a tag e valida
    if len(pilha) == 1:
      Logs.info(f'Tag {nomeTag} foi reconhecida.')
      return True
    else:
      Logs.error(f'Tag {nomeTag} nao recohecida: expressao invalida')
      return False
