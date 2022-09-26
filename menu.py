from tabela import inserirRegistro, listarTodos, atualizarRegistro, excluiRegistro

sair = False
opcao = 0

print("Bem vindo ao sistema!!")
while sair == False:
    opcao = int(input("Digite a opção: "))
    match opcao:
        case 1:
            listarTodos()
        case 2: 
            user = input("Usuario: ")
            senha = input("Senha: ")
            inserirRegistro(user, senha)
            listarTodos()
        case 3:
            codigo = int(input("Codigo: "))
            user = input("Novo Usuario: ")
            senha = input("Nova Senha: ")
            atualizarRegistro(codigo, user, senha)
            listarTodos()
        case 4:
            codigo = int(input("Codigo: "))
            excluiRegistro(codigo)
        case 0:
            sair = True
            break


        

