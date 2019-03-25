from collections import Counter
import pandas as pd

df = pd.read_csv('busca2.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies = pd.get_dummies(X_df)
Ydummies = Y_df

# print("elementos do Y do qual no índice do X é zero:")
# print(X_df[Y_df==0])

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

acertos = (resultado == teste_marcacoes)
total_de_acertos = sum(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(f"Taxa de acerto = {taxa_de_acerto}")

# a eficacia do algoritmo que chuta tudo o mesmo valor
maior_acerto = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = 100.0 * maior_acerto / len(teste_marcacoes)
print(f"Taxa de acerto base {taxa_de_acerto_base}")
