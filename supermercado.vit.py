from produto import produto
def adicional():
    qnt = int(input('Quantidade de produtos:'))
    for i in range (0, qnt):
        nome = input("Digite o nome do produto:")
        quantidade = input("Digite a quantidade do produto:")
        preco = input("Digite o preço do produto:")
        peso = input("Digite o peso do produto:")
        prod = produto(nome, quantidade, preco, peso)
        lista.append(prod)
        

lista = list()
continuar = True
while continuar == True:
    print('O que voce deseja fazer?')
    print ('1-Cadastrar')
    print ('2-Recuperar')
    print ('3-Deletar')
    print ('4-Sair')
    x = input("Escolha:")
    if x == '1':
        adicional()
    elif x == '2':
        b = input("Qual produto deseja recuperar?")
        for prod in lista:
            if b == prod.get_nome():
                prod.recuperar() 
        
    elif x == '3':
        a = input('Qual o produto a ser deletado?')
        for pos, prod in enumerate(lista):
            if a == prod.get_nome():         
                lista.pop(pos)
                print ("O produto %s foi deletado!" %(a) )
    elif x == '4':
        continuar = False
    else:
        print("Opção inválida!")
    
                
