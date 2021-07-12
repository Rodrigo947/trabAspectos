# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Utils.Logs import Logs


class LeituraArquivos(object):
  @staticmethod
  def ler(arquivo: str):
    try:
      file = open(arquivo, 'r')
      read_data = file.readlines()
      file.close()
      return read_data
    except IOError:
      Logs.error(f'Arquivo \"{arquivo}\" não encontrado!')
      return False
