
# Criando e escrevendo em um arqiuvo

if 'teste.txt' == True:
    print('O arquivo já existe!')
else:
    with open('teste.txt', 'w') as file:
        file.write('Esta é a primeira linha do arquivo! \n')
        file.write('Conteúdo adicionado depois!\n')