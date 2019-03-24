from dados import carregar_acessos
X, Y = carregar_acessos()

#print(Y)
#print(X)

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(X, Y)

resultado = modelo.predict(X)
diferencas = resultado - Y
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(X)
taxa_de_acertos = 100.0 * (total_de_acertos / total_de_elementos)

print(taxa_de_acertos)
print(total_de_elementos)