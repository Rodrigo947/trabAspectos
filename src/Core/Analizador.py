# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.LeituraEscritaArquivos.EscritaAquivos import EscritaArquivos
from src.Core.Automatos import Automatos
from src.LeituraEscritaArquivos.LeituraAquivos import LeituraArquivos
from src.Utils.Logs import Logs


class Analizador(object):

  def analizar(self, automatos: Automatos, texto: str, escritaArquivos: EscritaArquivos) -> bool:

    arrayAutomatos = automatos.get_automatos()
    if len(arrayAutomatos) == 0:
      Logs.error('Nenhuma tag valida foi definida!')
      return False

    '''
    Estrategia usada foi pecorrer o texto de tras para frente.
    Caso nao exista nenhum automato que reconheca a palavra, a posicao
    final eh retirada e a substring eh novamente analisada por todos
    os automatos
    '''
    tagsIdentificadas = []
    charInicial = 0
    charFinal = len(texto)
    textoProcessado = False
    automatoReconhecido = False

    while charFinal >= charInicial:
      # Verificado se algum automato processa o texto
      for automato in arrayAutomatos:
        if automato.processar_texto(texto[charInicial:charFinal]):
          tagsIdentificadas.append(automato.get_nome_tag())
          charInicial = charFinal
          charFinal = len(texto)
          automatoReconhecido = True
          break

      # Se nenhum automato reconhecer o texto,
      # o caractere final eh retirado
      if not automatoReconhecido:
        charFinal = charFinal - 1
        if charFinal == charInicial:
          textoProcessado = False
          break
      else:
        if charFinal == charInicial:
          textoProcessado = True
          break
        automatoReconhecido = False

    if textoProcessado:
      str = f"Tags identificadas da entrada {texto}: " + \
          ' '.join(tagsIdentificadas)
      escritaArquivos.escrever(str+'\n')
      Logs.info(str)
      return True

    Logs.error(f"{texto} nao foi totalmente processado!")
    return False

  def analizarArquivo(self, automatos: Automatos, nome_arquivo: str, arq_saida: str):
    data_textos = LeituraArquivos.ler(nome_arquivo)
    if data_textos:
      for linha in data_textos:
        self.analizar(automatos, linha.rstrip('\n'), arq_saida)

    else:
      Logs.error('Arquivo nao especificado!')
