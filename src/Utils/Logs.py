# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

class Logs(object):
  '''
  Classe responsável pela impressão de avisos no terminal
  '''
  @staticmethod
  def info(mensagem: str) -> None:
    '''
    Imprime a mensagem passada por parametro com
    a tag [INFO] no começo da mensagem
    '''
    print('\033[32m' + '[INFO] ' + '\033[39m' + f'{mensagem}')

  @staticmethod
  def error(mensagem: str) -> None:
    '''
    Imprime a mensagem passada por parametro com
    a tag [ERROR] no começo da mensagem
    '''
    print('\033[31m' + '[ERROR] ' + '\033[39m' + f'{mensagem}')

  @staticmethod
  def warning(mensagem: str) -> None:
    '''
    Imprime a mensagem passada por parametro com
    a tag [WARNING] no começo da mensagem
    '''
    print('\033[33m' + '[WARNING] ' + '\033[39m' + f'{mensagem}')
