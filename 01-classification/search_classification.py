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

porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1

tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = int(porcentagem_de_teste * len(Y))
tamanho_de_validacao = len(Y) - tamanho_de_treino - tamanho_de_teste

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

fim_de_teste = tamanho_de_treino + tamanho_de_teste
teste_dados = X[tamanho_de_treino:fim_de_teste]
teste_marcacoes = Y[tamanho_de_treino:fim_de_teste]

validacao_dados = X[fim_de_teste:]
validacao_marcacoes = Y[fim_de_teste:]

def fit_and_predict(name, modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    # treinar
    modelo.fit(treino_dados, treino_marcacoes)

    # prevendo
    resultado = modelo.predict(teste_dados)

    acertos = (resultado == teste_marcacoes)
    total_de_acertos = sum(acertos)
    total_de_elementos = len(teste_dados)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

    print(f"Taxa de acerto calculado {name} = {taxa_de_acerto}")
    return taxa_de_acerto

from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier

modelo_multinomial = MultinomialNB()
resultado_multiNomial = fit_and_predict("MultinomialNB", modelo_multinomial, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)
modelo_adaBoost = AdaBoostClassifier()
resultado_adaBoost = fit_and_predict("AdaBoost", modelo_adaBoost, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

if resultado_adaBoost >= resultado_multiNomial:
    modelo_vencedor = modelo_adaBoost
    nome_vencedor = "AdaBoost"
else:
    modelo_vencedor = modelo_multinomial
    nome_vencedor = "Multinomial"

resultado_do_vencedor = modelo_vencedor.predict(validacao_dados)

acertos_do_vencedor = (resultado_do_vencedor == validacao_marcacoes)
total_de_acertos_do_vencedor = sum(acertos_do_vencedor)
total_de_elementos_do_vencedor = len(validacao_dados)
taxa_de_acerto_vencedor = 100.0 * total_de_acertos_do_vencedor / total_de_elementos_do_vencedor

print(f"Taxa de acerto vencedor {nome_vencedor} = {taxa_de_acerto_vencedor}")

# a eficacia do algoritmo que chuta tudo o mesmo valor
maior_acerto = max(Counter(validacao_marcacoes).values())
taxa_de_acerto_base = 100.0 * maior_acerto / len(validacao_marcacoes)
print(f"Taxa de acerto base = {taxa_de_acerto_base}")
print(f"Total de testes = {len(validacao_dados)}")
