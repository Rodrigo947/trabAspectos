from colorama import Fore, Style


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
    print(Fore.GREEN + '[INFO] ' + Style.RESET_ALL + f'{mensagem}')

  @staticmethod
  def error(mensagem: str) -> None:
    '''
    Imprime a mensagem passada por parametro com
    a tag [ERROR] no começo da mensagem
    '''
    print(Fore.RED + '[ERROR] ' + Style.RESET_ALL + f'{mensagem}')

  @staticmethod
  def warning(mensagem: str) -> None:
    '''
    Imprime a mensagem passada por parametro com
    a tag [WARNING] no começo da mensagem
    '''
    print(Fore.YELLOW + '[WARNING] ' + Style.RESET_ALL + f'{mensagem}')
