# Trabalho de Aspectos Teóricos da Computação
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

from src.Utils.Logs import Logs


class EscritaArquivos(object):
  __file = None
  __escrevendo = False
  __arquivo_saida = ''

  # Método de escrita de instância para multiplas escritas em mesmo arquivo
  def escrever(self, conteudo: str):
    if(self.__escrevendo):
      try:
        self.__file.write(conteudo)
      except IOError:
        Logs.error('Erro ao escrever arquivo!')

  def fechar_arquivo(self):
    if self.__escrevendo:
      self.__escrevendo = False
      self.__file.close()

  def abrirArquivo(self, arquivo: str):
    self.fechar_arquivo()
    self.__arquivo_saida = arquivo
    if self.__file is None:
      self.__escrevendo = True
      self.__file = open(self.__arquivo_saida, 'w')

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
