tabela = [[1,'adm', '123', 'ativo']]
indice = 1

def inserirRegistro(user, senha):
    global tabela
    global indice
    indice = indice + 1
    linha = [indice, user, senha, 'ativo']
    tabela.append(linha)   

def listarTodos():
    for linhas in tabela:
        print(' '.join(map(str, linhas)))

def atualizarRegistro(id, usuario, senha):
    for linhas in tabela:
        for campos in linhas:
            if campos == id:
                indice = tabela.index(linhas)
                tabela[indice] = [id, usuario, senha, 'ativo']
                break

def excluiRegistro(id):
    for linhas in tabela:
        for campos in linhas:
            if campos == id:
                indice = tabela.index(linhas)
                tabela.remove(tabela[indice])
                break