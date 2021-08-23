# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Utils.Logs import Logs
# TODO A pessoa pode especificar qual caminho salvar e ler
# TODO arquivo de saida tem que ter um formato de impressão igual ao formato de entrada


class EscritaArquivos(object):
  __file = None
  __escrevendo = False

  # Método de escrita de instância para multiplas escritas em mesmo arquivo
  def escrever(self, arquivo: str, conteudo: str):
    try:
      if self.__file is None:
        self.__file = open(arquivo, 'w')
      self.__file.write(conteudo)
      self.__escrevendo = True
    except IOError:
      Logs.error('Erro ao escrever arquivo!')

  def fechar_arquivo(self):
    if self.__escrevendo:
      self.__file.close()

  # Método de escrita estático para escritas individuais (sem reescrita ou adição de escrita)
  @staticmethod
  def escrever_static(arquivo: str, conteudo: str):
    try:
      file = open(arquivo, 'w')
      file.write(conteudo)
      file.close()
      Logs.info(f'O arquivo {arquivo} foi salvo!')
    except IOError:
      Logs.error('Erro ao escrever arquivo!')
