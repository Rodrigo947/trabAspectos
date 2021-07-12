# Trabalho Aspectos Teoricos da Computação 

## Execução do programa
### Requisitos
  1. Instalado o python 3.7 ou acima.
  2. Instalado o gerenciador de ambientes virtuais do python. <code>$ pip install pipenv</code>
### Como desenvolvedor

```
$ pipenv install --dev
$ pipenv shell
$ python main.py
```
### Como cliente
- Windows: dentro da pasta windows_build execute o arquivo main.exe
- Linux: dentro da pastas linux_build execute o comando <code>$ ./main</code>

## Criando as pastas de build
As pastas build servem para rodar o programa em qualquer computador sem necessidade de instalar o python
## Windows
```
$ pipenv install --dev
$ pipenv shell
$ cxfreeze main.py --target-dir windows_build
```

## Linux
```
$ sudo apt-get install patchelf
$ pipenv install --dev
$ pipenv shell
$ cxfreeze main.py --target-dir linux_build
```
