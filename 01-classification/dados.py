import csv


def carregar_acessos():
    X = []
    Y = []
    arquivo = open('acesso.csv', 'r')

    leitor = csv.reader(arquivo)
    next(leitor)  # remove first line because title doesn't matter

    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append(int(comprou))

    return X, Y


# run at shell: python
#   from X import carregar_acessos
#   X, Y = carregar_acessos()

def carregar_buscas():
    X = []
    Y = []
    arquivo = open('busca.csv', 'r')

    leitor = csv.reader(arquivo)
    next(leitor)  # remove first line because title doesn't matter

    for home, busca, logado, comprou in leitor:
        X.append([int(home), busca, int(logado)])
        Y.append(int(comprou))

    return X, Y
