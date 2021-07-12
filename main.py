# Trabalho de Aspectos Teoricos da Computacao
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

# Arquivo principal (Main)
from colorama import init
from src.Utils.Logs import Logs
from src.Core.Tags import Tags
from src.Core.Analizador import Analizador
from src.LeituraEscritaArquivos.LeituraAquivos import LeituraArquivos
from src.LeituraEscritaArquivos.EscritaAquivos import EscritaArquivos


def interface():
  print("\nComando                            Descricao                            Exemplo")
  # ainda nao implementado, segunda parte.
  print(":d     Realiza a divisao em tags da string do arquivo informado         :d entrada.txt")
  print(":c     Carrega um arquivo com definicoes de tags                        :c tags.lex")
  print(":o     Especifica o caminho do arquivo de saida para a divisao em tags  :o saida.txt")
  # ainda nao implementado, segunda parte.
  print(":p     Realiza a divisao em tags da entrada informada                   :p x=420")
  # ainda nao implementado, segunda parte.
  print(":a     Lista as definicoes formais dos automatos em memoria             :a")
  print(":l     Lista as definicoes de tag validas                               :l")
  print(":q     Sair do programa                                                 :q")
  print(":s     Salvar as tags                                                   :s file.txt")
  print(":h     Lista os comandos aceitos                                        :h \n")


def main():
  tags = Tags()
  analizador = Analizador()  # TODO segunda entrega.
  escrever_resul = EscritaArquivos()
  arq_saida = ''
  interface()

  while True:
    entrada = input().lower()
    # Primeira parte
    # Comando :o Especifica o caminho do arquivo de saida para a divisao em tags
    if entrada.startswith(':o'):
      nome_arquivo = entrada[2:].strip()  # remove a opcao :o
      if ' ' in nome_arquivo:
        Logs.error('Nome de arquivo nao pode conter espacos!')
      else:
        if nome_arquivo:
          arq_saida = nome_arquivo
          Logs.info('Arquivo de saida especificado!')
        else:
          Logs.error('Arquivo de saida nao fornecido!')

    # Comando :c Carrega um arquivo com definicoes de tags
    if entrada.startswith(':c'):
      # remove a opcao :c, remove espacos iniciais e finais
      nome_arquivo = entrada[2:].strip()
      if ' ' not in nome_arquivo:
        if nome_arquivo:
          arquivo_tags = LeituraArquivos.ler(nome_arquivo)
          if arquivo_tags:
            for linha in arquivo_tags:
              if ': ' in linha:
                # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
                tag = linha.split(': ', 1)
                # remove possiveis espacos iniciais e finais
                tags.adicionar_tag(tag[0].upper(), tag[1])
              else:
                Logs.error('Formato invalido de tag!')
            Logs.info('Todas as tags foram lidas!')
        else:
          Logs.error('Arquivo nao especificado')
      else:
        Logs.error('Nome de arquivo nao pode conter espacos!')

    # Comando :l Lista as definicoes de tag validas
    elif entrada.startswith(':l'):
      for tag in tags.get_todas_tags():
        print(tag+': '+tags.get_tag(tag))

    # Comando :s Salvar tags.
    elif entrada.startswith(':s'):
      nome_arquivo = entrada[2:].strip()  # remove a opcao :s
      if nome_arquivo:
        conteudo_saida = ''
        for tag in tags.get_todas_tags():
          conteudo_saida += tag + ' ' + tags.get_tag(tag) + '\n'
        EscritaArquivos.escrever_static(nome_arquivo, conteudo_saida)
      else:
        Logs.error('Arquivo de saida nao fornecido!')

    elif entrada.startswith(':q'):  # Sair do programa
      escrever_resul.fechar_arquivo()
      break

    # Comando :h Lista os comandos aceitos.
    elif entrada.startswith(':h'):
      interface()

    # TODO comdanso da segunda parte :d, :p, :a
    elif entrada.startswith(':d'):
      Logs.warning('Comando sera implementado na parte 2 do trabalho.')

      # Realiza a divisao em tags da entrada informada
    elif entrada.startswith(':p'):
      Logs.warning("Comando sera implementado na parte 2 do trabalho.")

    # Lista as definicoes formais dos automatos em memoria
    elif entrada.startswith(':a'):
      Logs.warning("Comando sera implementado na parte 2 do trabalho.")

    elif entrada.startswith(':'):  # Entrada invalida
      Logs.info('Entrada invalida!')

    else:  # Insercao de tag
      if ': ' in entrada:
        # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
        tag = entrada.split(': ', 1)
        # remove possiveis espacos iniciais e finais
        tags.adicionar_tag(tag[0].upper(), tag[1])
      else:
        Logs.error('Formato invalido de tag!')


if __name__ == "__main__":
  init()
  main()
