# a -> append - adiciona conteudo ao fim do arquivo
# r -> read - abre o arquivo somente para leitura
# r+ -> read more - abre o arquivo para leitura e escrita
# w -> write - abre o arquivo para escrita

# ABRE O ARQUIVO PARA ESCRITA
# APAGANDO QUALQUER CONTEUDO QUE JA EXISTIR
# arquivo = open("pessoas.txt", "w")
# arquivo.write("NOME;IDADE;CIDADE\n")
# arquivo.write("CICERO;31;ALFENAS\n")
# arquivo.write("MARIA;26;SÃO PAULO\n")
# arquivo.write("LARISSA;29;RIO DE JANEIRO")

# arquivo = open("pessoas.txt", "r")
# for pessoa in arquivo:
#   print(pessoa)
#   print("---")

# arquivo = open("pessoas.txt", "r+")
# for pessoa in arquivo:
#   print(pessoa)
# arquivo.write("FIM DA EXECUCAO")

arquivo = open("pessoas.txt", "a")
arquivo.write("JOAO;30;MANAUS\n")
arquivo.write("KIKO;30;MANAUS\n")
arquivo.write("ROBERTO;30;MANAUS\n")