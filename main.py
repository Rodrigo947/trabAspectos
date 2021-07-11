# Arquivo principal (Main)
# TODO :c, :o, :l, :q, :s
from src.Utils.Logs import Logs
from src.Core.Tags import Tags
from src.Core.Analizador import Analizador
from src.LeituraEscritaArquivos.LeituraAquivos import LeituraArquivos
from src.LeituraEscritaArquivos.EscritaAquivos import EscritaArquivos

def interface():
    print("\nComando                            Descrição                            Exemplo")
    print(":d     realiza a divisao em tags da string do arquivo informado         :d entrada.txt") # ainda nao implementado, segunda parte.
    print(":c     carrega um arquivo com definicoes de tags                        :c tags.lex")
    print(":o     especifica o caminho do arquivo de saida para a divisao em tags  :o saida.txt")
    print(":p     realiza a divisao em tags da entrada informada                   :p x=420") # ainda nao implementado, segunda parte.
    print(":a     Lista as definicoes formais dos automatos em memoria             :a")   # ainda nao implementado, segunda parte.
    print(":l     Lista as definicoes de tag validas                               :l")
    print(":q     sair do programa                                                 :q")
    print(":s     salvar as tags                                                   :s file.txt\n")

def main():
  tags = Tags()
  analizador = Analizador() # segunda entrega.
  escrever_resul = EscritaArquivos()
  arq_saida = ''

  while True:
    interface()
    entrada = input().lower()
    # Primeira parte
    # Comando :c Carrega um arquivo com definicoes de tags
    if entrada.startswith(':c'):
      nome_arquivo = entrada[2:].strip() # remove a opcao :c, remove espaços iniciais e finais
      if ' ' in nome_arquivo:
        Logs.error('Nome de arquivo nao pode conter espaços!')
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
                Logs.error('Formato invalido de tag!')
            Logs.info('Todas as tags foram lidas!')
        else:
          Logs.error('Arquivo nao especificado')


    # Comando :o Especifica o caminho do arquivo de saida para a divisao em tags
    elif entrada.startswith(':o'):
      nome_arquivo = entrada[2:].strip()  # remove a opcao :o
      if ' ' in nome_arquivo:
        Logs.error('Nome de arquivo nao pode conter espaços!')
      else:
        if nome_arquivo:
          arq_saida = nome_arquivo
          Logs.info('Arquivo de saida especificado!')
        else:
          Logs.error('Arquivo de saida não fornecido!')

    # Comando :l Lista as definicoes de tag validas
    elif entrada.startswith(':l') :
      for tag in tags.get_todas_tags():
        print(f'{tag} {tags.get_tag(tag)}')


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

    elif entrada.startswith(':q') or entrada.startswith(':Q'):  # Sair do programa
      escrever_resul.fechar_arquivo()
      break


#A fazer, segunda parte
    elif entrada.startswith(':d'):
      Logs.warning('Comando sera implementado na parte 2 do trabalho.') 

      # Realiza a divisão em tags da entrada informada
    elif entrada.startswith(':p'):
      Logs.warning("Comando sera implementado na parte 2 do trabalho.") 


    # Lista as definições formais dos autômatos em memória
    elif entrada.startswith(':a'):
      Logs.warning("Comando sera implementado na parte 2 do trabalho.")


    elif entrada.startswith(':'):  # Entrada inválida
      Logs.info('Entrada invalida!')



    else:  # Inserção de tag
      if ': ' in entrada:
        # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
        tag = entrada.split(': ', 1)
        # remove possiveis espaços iniciais e finais
        tag = [i.strip() for i in tag]
        tags.adicionar_tag(tag[0].upper(), tag[1])
      else:
        Logs.error('Formato invalido de tag!')


if __name__ == "__main__":
  main()
