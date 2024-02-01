
# Importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Carregando os dados do arquivo CSV
dados_gasolina = pd.read_csv('gasolina.csv')

#Configurando o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=dados_gasolina, marker='o', color='b')

# Adicionando título e rótulos aos eixos
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

#Adicionando legenda
plt.legend()

#Adicionando grade
plt.grid(True)

# Salvando o gráfico como uma imagem PNG
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()
