import pandas as pd
df = pd.read_csv('busca.csv')

X_df = df[['home', 'busca', 'logado', 'comprou']]
Y_df = df['comprou']

Xdummies = pd.get_dummies(X_df)
Ydummies = Y_df

X = Xdummies.values
Y = Ydummies.values

porcentagem_de_treino = 0.9
tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = len(Y) - tamanho_de_treino

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
# treinar
modelo.fit(treino_dados, treino_marcacoes)

# prevendo
resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acertos = 100.0 * (total_de_acertos / total_de_elementos)

print(f"Taxa de acertos = {taxa_de_acertos}")
print(f"Total de elementos = {total_de_elementos}")
