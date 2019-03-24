# [é gordinho?, tem perninha curta?, faz auau?]
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]
resultado = modelo.predict(teste)
print(resultado)

marcacoes_teste = [-1, 1, -1]

#  1  1 =>  1 -  1 =  0
# -1 -1 => -1 - -1 =  0
# -1  1 => -1 -  1 = -2
#  1 -1 =>  1 - -1 =  2


diferencas = resultado - marcacoes_teste
print("Diferenças")
print(diferencas)

acertos = [d for d in diferencas if d == 0]
print("Acertos")
print(acertos)
total_de_acertos = len(acertos)
total_de_elementos = len(teste)
taxa_de_acertos = 100.0 * (total_de_acertos / total_de_elementos)
print(f"Elementos: {total_de_elementos}; acertos: {total_de_acertos}; taxa de acertos: {taxa_de_acertos}")