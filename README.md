import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico
plt.plot(x, y)
plt.title('Gráfico de Exemplo')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Salvar como imagem
plt.savefig('grafico_exemplo.png')
plt.show()
