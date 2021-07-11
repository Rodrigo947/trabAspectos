# Arquivo principal (Main)
# TODO :c, :o, :l, :q, :s
from src.Utils.Logs import Logs
from src.Core.Tags import Tags
from src.Core.Analizador import Analizador
from src.LeituraEscritaArquivos.LeituraAquivos import LeituraArquivos
from src.LeituraEscritaArquivos.EscritaAquivos import EscritaArquivos

def interface():
    print("\nComando                            Descrição                            Exemplo")
    print(":d     realiza a divisão em tags da string do arquivo informado         :d entrada.txt") # ainda não implementado, segunda parte.
    print(":c     carrega um arquivo com definições de tags                        :c tags.lex")
    print(":o     especifica o caminho do arquivo de saída para a divisão em tags  :o saida.txt")
    print(":p     realiza a divisão em tags da entrada informada                   :p saida.txt") # ainda não implementado, segunda parte.
    print(":a     Lista as definições formais dos autômatos em memória             :a")   # ainda não implementado, segunda parte.
    print(":l     Lista as definições de tag válidas                               :l")
    print(":q     sair do programa                                                 :q")
    print(":s     salvar as tags                                                   :s file.txt\n")

def main():
  interface()
  tags = Tags()
  analizador = Analizador()
  escrever_resul = EscritaArquivos()
  arq_saida = ''

  while True:
    entrada = input().lower()
    # Realiza a divisão em tags da string do arquivo informado - Parte 2
    if entrada.startswith(':d'):
      Logs.warning('Comando será implementado na parte 2 do trabalho.') 

    # Carrega um arquivo com definições de tags
    elif entrada.startswith(':c'):
      nome_arquivo = entrada[2:]  # remove a opção :c
      nome_arquivo = nome_arquivo.strip()  # remove espaços iniciais e finais
      if ' ' in nome_arquivo:
        Logs.error('Nome de arquivo não pode conter espaços!')
      else:
        if nome_arquivo:
          arquivo_tags = LeituraArquivos.ler(nome_arquivo)
          if arquivo_tags:
            for linha in arquivo_tags:
              if ': ' in linha:
                # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
                tag = linha.split(': ', 1)
                # remove possiveis espaços iniciais e finais
                tag = [i.strip() for i in tag]
                tags.adicionar_tag(tag[0].upper(), tag[1])
              else:
                Logs.error('Formato inválido de tag!')
            Logs.info('Todas as tags foram lidas!')
        else:
          Logs.error('Arquivo não especificado!')


    # Especifica o caminho do arquivo de saída para a divisão em tags
    elif entrada.startswith(':o'):
      nome_arquivo = entrada[2:].strip()  # remove a opção :o
      nome_arquivo = nome_arquivo.strip()  # remove espaços iniciais e finais
      if ' ' in nome_arquivo:
        Logs.error('Nome de arquivo não pode conter espaços!')
      else:
        if nome_arquivo:
          arq_saida = nome_arquivo
          Logs.info('Arquivo de saída especificado!')
        else:
          Logs.error('Arquivo de saida não fornecido!')

    # Realiza a divisão em tags da entrada informada
    elif entrada.startswith(':p'):
      Logs.warning("Comando será implementado na parte 2 do trabalho.") 

    # Lista as definições formais dos autômatos em memória
    elif entrada.startswith(':a'):
      Logs.warning("Comando será implementado na parte 2 do trabalho.")

    # Lista as definições de tag válidas
    elif entrada.startswith(':l') :
      for tag in tags.get_todas_tags():
        print(f'{tag} {tags.get_tag(tag)}')

    elif entrada.startswith(':s'):  # Salvar as tags
      nome_arquivo = entrada[2:]  # remove a opção :s
      nome_arquivo = nome_arquivo.strip()  # remove espaços iniciais e finais
      if nome_arquivo:
        conteudo_saida = ''
        for tag in tags.get_todas_tags():
          conteudo_saida += tag + ' ' + tags.get_tag(tag) + '\n'
        EscritaArquivos.escrever_static(nome_arquivo, conteudo_saida)
      else:
        Logs.error('Arquivo de saida não fornecido!')

    elif entrada.startswith(':q') or entrada.startswith(':Q'):  # Sair do programa
      escrever_resul.fechar_arquivo()
      break

    elif entrada.startswith(':'):  # Entrada inválida
      Logs.info('Entrada inválida!')

    else:  # Inserção de tag
      if ': ' in entrada:
        # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
        tag = entrada.split(': ', 1)
        # remove possiveis espaços iniciais e finais
        tag = [i.strip() for i in tag]
        tags.adicionar_tag(tag[0].upper(), tag[1])
      else:
        Logs.error('Formato inválido de tag!')


if __name__ == "__main__":
  main()
