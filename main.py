# Trabalho de Aspectos Teoricos da Computacao
#
# Lucas Lino do Carmo Freitas   201876034
# Rodrigo Torres Rego           201876029
# Wiliam Rocha dos Santos       201876031

# Arquivo principal (Main)
from src.Core.Automato import Automato
from src.Utils.Logs import Logs
from src.Core.Tags import Tags
from src.Core.Analizador import Analizador
from src.Core.Automatos import Automatos
from src.LeituraEscritaArquivos.LeituraAquivos import LeituraArquivos
from src.LeituraEscritaArquivos.EscritaAquivos import EscritaArquivos


def interface():
  print("\nComando                            Descricao                            Exemplo")

  print(":d     Realiza a divisao em tags da string do arquivo informado         :d entrada.txt")
  print(":c     Carrega um arquivo com definicoes de tags                        :c tags.lex")
  print(":o     Especifica o caminho do arquivo de saida para a divisao em tags  :o saida.txt")
  print(":p     Realiza a divisao em tags da entrada informada                   :p x=420")
  print(":a     Lista as definicoes formais dos automatos em memoria             :a")
  print(":l     Lista as definicoes de tag validas                               :l")
  print(":q     Sair do programa                                                 :q")
  print(":s     Salvar as tags                                                   :s file.txt")
  print(":h     Lista os comandos aceitos                                        :h \n")


def main():
  tags = Tags()
  analizador = Analizador()
  automatos = Automatos()
  escrever_resul = EscritaArquivos()
  interface()

  while True:
    entrada = input().lower()

    # COMANDO :c Carrega um arquivo com definicoes de tags
    if entrada.startswith(':c '):
      # remove a opcao :c, remove espacos iniciais e finais
      nome_arquivo = entrada[3:].strip()
      if ' ' not in nome_arquivo:
        if nome_arquivo:
          arquivo_tags = LeituraArquivos.ler(nome_arquivo)
          if arquivo_tags:
            for linha in arquivo_tags:
              if ': ' in linha:
                # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
                tag = linha.split(': ', 1)

                if tags.adicionar_tag(tag[0].upper(), tag[1].rstrip('\n')):
                  automatos.adiciona_automato(
                      tag[0].upper(), tag[1].rstrip('\n'))
              else:
                Logs.error('Formato invalido de tag!')
            Logs.info('Todas as tags foram lidas!')
        else:
          Logs.error('Arquivo nao especificado')
      else:
        Logs.error('Nome de arquivo nao pode conter espacos!')

    # COMANDO :o Especifica o caminho do arquivo de saida para a divisao em tags
    elif entrada.startswith(':o '):
      nome_arquivo = entrada[3:].strip()  # remove a opcao :o
      if ' ' in nome_arquivo:
        Logs.error('Nome de arquivo nao pode conter espacos!')
      else:
        if nome_arquivo:
          escrever_resul.abrirArquivo(nome_arquivo)
          Logs.info('Arquivo de saida especificado!')
        else:
          Logs.error('Arquivo de saida nao fornecido!')

    # COMANDO :l Lista as definicoes de tag validas
    elif entrada.startswith(':l'):
      for tag in tags.get_todas_tags():
        print(tag+': '+tags.get_tag(tag))

    # COMANDO :s Salvar tags
    elif entrada.startswith(':s '):
      nome_arquivo = entrada[3:].strip()  # remove a opcao :s
      if nome_arquivo:
        conteudo_saida = ''
        for tag in tags.get_todas_tags():
          conteudo_saida += tag + ': ' + tags.get_tag(tag) + '\n'
        EscritaArquivos.escrever_static(nome_arquivo, conteudo_saida)
      else:
        Logs.error('Arquivo de saida nao fornecido!')

    # COMANDO :q Sair do programa
    elif entrada.startswith(':q'):
      escrever_resul.fechar_arquivo()
      break

    # Comando :h Lista os comandos aceitos.
    elif entrada.startswith(':h'):
      interface()

    # COMANDO :d Realiza a divisao em tags da string do arquivo informado
    elif entrada.startswith(':d '):
      nome_arquivo = entrada[3:].strip()  # remove a opcao :d
      if ' ' in nome_arquivo:
        Logs.error('Nome de arquivo nao pode conter espacos!')
      else:
        if nome_arquivo:
          analizador.analizarArquivo(automatos, nome_arquivo, escrever_resul)
        else:
          Logs.error('Arquivo de saida nao fornecido!')

    # COMANDO :p Realiza a divisao em tags da entrada informada
    elif entrada.startswith(':p '):
      string_entrada = entrada[3:]  # remove a opcao :p
      if string_entrada == '':
        Logs.error("Nenhuma entrada informada!")
      else:
        analizador.analizar(automatos, string_entrada, escrever_resul)

    # COMANDO :a Lista as definicoes formais dos automatos em memoria
    elif entrada.startswith(':a '):
      automatos.listardefinicoes()
      #Logs.warning("Comando sera implementado na parte 2 do trabalho.")

    else:  # Insercao de tag
      if ': ' in entrada:
        # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
        tag = entrada.split(': ', 1)

        if tags.adicionar_tag(tag[0].upper(), tag[1]):
          automatos.adiciona_automato(tag[0].upper(), tag[1])

      else:
        Logs.error('Comando nao reconhecido')


if __name__ == "__main__":
  main()
