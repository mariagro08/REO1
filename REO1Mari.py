######  APRESENTAÇÃO REO1   #####
########################################################################################################################
# DATA: 17/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# ALUNA: MARIANA ANDRADE DIAS


##### Pacotes utilizados #####
import numpy as np

print('EXERCÍCIO 01')

##### Questão 1.a #####
print('a) Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.')
print('Resposta:')
lista = (43.5, 150.30, 17, 28, 35, 79, 20, 99.07, 15)
print(type(lista))
vetor = np.array(lista)
print('Vetor: ' + str(vetor))
print('O vetor é do tipo: ' + str(type(vetor)))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.b #####
print('b) Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.')
print('Resposta:')
dim_vetor = len(vetor)
media_vetor = np.mean(vetor)
val_max = max(vetor)
val_min = min(vetor)
var_vetor = np.var(vetor)
print('A dimensão do vetor é:' + str(dim_vetor))
print('A média do vetor é:' + str(media_vetor))
print('O máximo do vetor é:' + str(val_max))
print('O mínimo do vetor é:' + str(val_min))
print('A variância do vetor é:' + str(var_vetor))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.c #####
print('c) Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado na letra a e o valor da média deste.')
print('Resposta:')
media_vetor = np.mean(vetor)
novo_vetor = np.array((vetor-media_vetor)**2)
tipo_vetor = type(novo_vetor)
print(novo_vetor)
print('-----------------------------------------------------------------------------------------------------------------')
print('O vetor é do tipo:' + str(tipo_vetor))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.d #####
print('d) Obtenha um novo vetor que contenha todos os valores superiores a 30.')
print('Resposta:')
bool_maior_30 = vetor>30
print('Vetor: ' + str(vetor))
vetor_maior_30 = vetor[bool_maior_30]
print('Vetor com valores maiores que 30: ' + str(vetor_maior_30))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.e #####
print('e) Identifique quais as posições do vetor original possuem valores superiores a 30')
print('Resposta:')
pos_maior_30 = np.where(vetor>30)
print('Posições com valores maiores que 30: ' + str(pos_maior_30[0]))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.f #####
print('f) Apresente um vetor que contenha os valores da primeira, quinta e última posição.')
print('Resposta:')

vetor_novo_posições = np.array([vetor[0],vetor[4],vetor[8]])
print ("Valores da primeira, quinta e última posição: " + str(vetor_novo_posições))
print('-----------------------------------------------------------------------------------------------------------------')


##### Questão 1.g #####
print('g) Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as iterações')
print('Resposta:')
it = 0
print('Considerando que o Python pondera que a primeira posição é 0:')
for pos,valor in enumerate(vetor):
    it = it+1
    print('Iteração :' + str(it))
    print('Na posição ' + str(pos) + ': Há o elemento ' + str(valor))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.h #####
print('h) Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.')
print('Resposta:')
import time
def soma_de_quadrados (vetor):
    somador = 0
    it = 0
    for el in vetor:
        print('Elemento: ' + str(el))
        print('Somador: ' + str(somador))
        somador = somador + el**2
        it = it + 1
        print('Iteração ' + str(it) + ': Somatório: ' + str(somador))
        print('_'*10)
        print(' ')
    return somador
print(vetor)
soma_de_quadrados(vetor)
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.i #####
print('i) Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor')
print('Resposta:')
print('Será realizado uma contagem até que o valor apresentado seja diferente de 100, começando pela posição 0:')
pos = 0
while vetor[pos] != 100:
    print(vetor[pos])
    pos = pos+1
    if pos==(len(vetor)):
        print(' Na posição igual a ' +str(pos)+ ' a condição estabelecida retornou true, a função while é desabilitada')
        break
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.j #####
print('j) Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.')
print('Resposta:')
print('Sequência de valores: ' + str(list(range(1, len(vetor) +1, 1))))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 1.k #####
print('k) Concatene o vetor da letra a com o vetor da letra j.')
print('Resposta:')
nov_vetor = list(range(1, len(vetor) +1, 1))
vet_concat = np.concatenate((vetor, nov_vetor))
print(vet_concat)
print('-----------------------------------------------------------------------------------------------------------------')

print(' ')
print(' ')
print(' ')

print('EXERCÍCIO 02')

##### Questão 2.a #####
print('a) Declare a matriz com a biblioteca numpy.')
# 1 3 22
# 2 8 18
# 3 4 22
# 4 1 23
# 5 2 52
# 6 2 18
# 7 2 25
print('Resposta:')
matriz = np.array([[1, 3, 22], [2, 8, 18], [3, 4, 22], [4, 1, 23], [5, 2 , 52], [6, 2, 18], [7, 2, 25]])
print(matriz)
print(type(matriz))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 2.b #####
print('b) Obtenha o número de linhas e de colunas desta matriz')
print('Resposta:')
nl, nc = np.shape(matriz)
dim = np.shape(matriz)
print('A dimensão da matriz: ' + str(dim))
print('Número de linhas da matriz:' + str(nl))
print('Número de colunas da matriz: ' + str(nc))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 2.c #####
print('c) Obtenha as médias das colunas 2 e 3.')
print('Resposta:')
#Média coluna 2
col_2 = matriz[:,1]     #Lembrar que o Python inicia em 0
media2 = np.mean(col_2)
print('Media da coluna 2:' + str(media2))
#Média coluna 3
col_3 = matriz[:,2]
media3 = np.mean(col_3)
print('Media da coluna 3:' + str(media3))
print('-----------------------------------------------------------------------------------------------------------------')


##### Questão 2.d #####
print('d) Obtenha as médias das linhas considerando somente as colunas 2 e 3')
print('Resposta:')
submatriz_l1 = matriz[0,[1,2]]
media_matriz_l1 = np.average(submatriz_l1)
print('A média da linha 1 considerando coluna 2 e 3: ' +str(media_matriz_l1))
submatriz_l2 = matriz[1,[1,2]]
media_matriz_l2 = np.average(submatriz_l2)
print('A média da linha 2 considerando coluna 2 e 3: ' +str(media_matriz_l2))
submatriz_l3 = matriz[2,[1,2]]
media_matriz_l3 = np.average(submatriz_l3)
print('A média da linha 3 considerando coluna 2 e 3: ' +str(media_matriz_l3))
submatriz_l4 = matriz[3,[1,2]]
media_matriz_l4 = np.average(submatriz_l4)
print('A média da linha 4 considerando coluna 2 e 3: ' +str(media_matriz_l4))
submatriz_l5 = matriz[4,[1,2]]
media_matriz_l5 = np.average(submatriz_l5)
print('A média da linha 5 considerando coluna 2 e 3: ' +str(media_matriz_l5))
submatriz_l6 = matriz[5,[1,2]]
media_matriz_l6 = np.average(submatriz_l6)
print('A média da linha 6 considerando coluna 2 e 3: ' +str(media_matriz_l6))
submatriz_l7 = matriz[6,[1,2]]
media_matriz_l7 = np.average(submatriz_l7)
print('A média da linha 7 considerando coluna 2 e 3: ' +str(media_matriz_l7))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 2.e #####
print('e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.')
print('Resposta:')
print(matriz)
severidade = (matriz[:, 1])
menor5 = np.where(severidade<5)
print('As posições dos genótipos com notas inferiores a 5 são: ' + str(menor5[0]))
bool_notas_menor5 = severidade<5
genotipos = (matriz[:, 0])
genotipos_notas_menor5 = genotipos[bool_notas_menor5]
print('Os genótipos com notas inferiores a 5 são: ' + str(genotipos_notas_menor5))
print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 2.f #####
print('f) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.')
print('Resposta:')
peso = (matriz[:, 2])
maior22 = np.where(peso>=22)
print('As posições na matriz dos genótipos que possuem peso de 100 grãos superior ou igual a 22: ' + str(maior22[0]))
bol_peso_maior22 = peso>=22
genotipos = (matriz[:, 0])
genotipos_peso_maior22 = genotipos[bol_peso_maior22]
print('Os genótipos com peso de 100 grãos superior ou igual a 22: ' + str(genotipos_peso_maior22))

print('-----------------------------------------------------------------------------------------------------------------')


##### Questão 2.g #####
print('g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100grãos igual ou superior a 22.')
print('Resposta:')
severidade = (matriz[:,1])
sev_menorigual_3 = np.where(severidade<=3)
bol_sev_menorigual_3 = severidade<=3
genotipos = (matriz[:, 0])
genotipos_notas_menorigual_3 = genotipos[bol_sev_menorigual_3]
print('Posições dos genótipos que possuem nota inferior ou igual a 3 são: ' +str(sev_menorigual_3[0]))
print('Posições dos genótipos com peso de 100 grãos superior ou igual a 22: ' +str(maior22[0]))
genotipos_q2g = genotipos[bol_peso_maior22 & bol_sev_menorigual_3]
print('Genótipos com peso de 100 grãos superior ou igual a 22 e nota de severidade de doença inferior ou igual a 3: ' +str(genotipos_q2g))


print('-----------------------------------------------------------------------------------------------------------------')

##### Questão 2.h #####
print('h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido. Apresente a seguinte mensagem a cada iteração "Na linha X e na coluna Y ocorre o valor: Z". Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25')
print('Resposta:')
import time
matriz_nova = []
contador = 0
for i in np.arange(0, nl, 1):
    for j in np.arange(0, nc, 1):
        contador += 1
        print('Iteração: ' + str(contador))
        print('Na linha ' + str(i+1) +
              ' e coluna ' + str(j+1) +
              ' ocorre o valor: ' + str(matriz[int(i), int(j)]))
        matriz_pesomaior_25 = (matriz[:, 2] >= 25)
        matriz_25 = (matriz[matriz_nova])
print('----------------------------------------------------------------------------------------------------')
print('Os genótipos ' + str(matriz_25[:, 0]) + ' apresentam peso de 100 grãos maior ou igual a 25')
print('-----------------------------------------------------------------------------------------------------------------')


print(' ')
print(' ')
print(' ')

# EXERCÍCIO 03:
print('a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor qualquer, baseada em um loop (for).')
print('Resposta:')
print("Outro arquivo .py chamado questao_3_mari")
print('-----------------------------------------------------------------------------------------------------------------')

print('b) Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 e variância 2500. Pesquise na documentação do numpy por funções de simulação.')
print('Resposta:')
import numpy as np
mean, desvio = 100, 50
vetor10 = np.random.normal(mean,desvio,10)
vetor100 = np.random.normal(mean,desvio,100)
vetor1000 = np.random.normal(mean,desvio,1000)

print('Vetor com 10 elementos:')
print(vetor10)
#print('Vetor com 100 elementos:')
#print(vetor100)
#print('Vetor com 1000 elementos:')
#print(vetor1000

print('-----------------------------------------------------------------------------------------------------------------')

print('c) Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.')
print('Resposta:')
from questao_3_mari import media, var_amostral

print('Vetor com 10 amostras: ')
print('média: ' +str(media(vetor10)))
print('variância: ' +str(var_amostral(vetor10)))
print('-----------------------------------------------------------------------------------------------------------------')
print('Vetor com 100 amostras: ')
print('media: ' +str(media(vetor100)))
print('variancia: ' +str(var_amostral(vetor100)))
print('-----------------------------------------------------------------------------------------------------------------')
print('Vetor com 1000 amostras: ')
print('media: ' +str(media(vetor1000)))
print("variancia: " +str(var_amostral(vetor1000)))

print('-----------------------------------------------------------------------------------------------------------------')
print('d) Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000.')
print('Resposta:')
mean, desvio = 100, 50
vetor100000 = np.random.normal(mean,desvio,100000)
#print('Vetor com 100000 elementos:')
#print(vetor100000)
print(' ')
print("Gráficos simulados com valores de 10, 100, 1000 e 100000")
from matplotlib import pyplot as plt

plt.style.use('dark_background')                    #estilo gráfico- fundo escuro
fig, axs = plt.subplots(nrows=2, ncols=2)           #figura com 4 eixos, duas linhas e duas colunas
ax0, ax1, ax2, ax3 = axs.flatten()                  #ordem dos gráficos nos eixos

# vetor 10 elementos
ax0.hist(vetor10, color="tab:orange")                #comando para plotar o gráfico para o primeiro vetor, e cor
ax0.set_title('10 elementos')                       #título

#vetor 100 elementos
ax1.hist(vetor100, color="tab:green")
ax1.set_title('100 elementos')

#vetor 1000 elementos
ax2.hist(vetor1000, color="tab:pink")
ax2.set_title('1000 elementos')

#vetor 100000 elementos
ax3.hist(vetor100000, color="tab:red")
ax3.set_title('100000 elementos')

fig.tight_layout()                                  #Ajuste dos subquadrantes para fornecer preenchimento sem sobreposição
plt.show()                                          #mostrar o gráfico

print(' ')
print(' ')
print(' ')

# EXERCÍCIO 04:
print('EXERCÍCIO 04')
print('a) O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, apresente os dados e obtenha as informações de dimensão desta matriz.')
print('Resposta:')

dados = np.loadtxt('dados.txt')
print('Dados: ' + str(dados))
print('Número de linhas e colunas')
nl, nc = np.shape(dados)
print('Número de linhas: ' + str(nl))
print('Número de colunas: ' + str(nc))
print('-----------------------------------------------------------------------------------------------------------------')

print('b) Pesquise sobre as funções np.unique e np.where da biblioteca numpy')
print('Resposta:')
print('O comando responsavél por demonstrar a utilidade cada função é o: help')
#help (np.unique)
#help (np.where)
print('-----------------------------------------------------------------------------------------------------------------')

print('c) Obtenha de forma automática os genótipos e quantas repetições foram avaliadas')
print('Resposta:')

print ('Os genótipos são:' + str(np.unique(dados[:,0])))
print ('As repetições:' + str(np.unique(dados[:,1])))

print('-----------------------------------------------------------------------------------------------------------------')

print('d Apresente uma matriz contendo somente as colunas 1, 2 e 4')
print('Resposta:')
print('Dados contendo somente as colunas 1, 2 e 4: ')
matriz_nova = dados[:,[0,1,3]]
print(matriz_nova)
print(type(matriz_nova))
print('-----------------------------------------------------------------------------------------------------------------')

print('e)Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da coluna 4. Salve esta matriz em bloco de notas.')
print('Resposta:')
variaveis_novas = np.zeros((len(np.unique(matriz_nova[:, 0])), 5))
it = 0
for i in range(0, len(np.unique(matriz_nova[:, 0])), 1):
    it = it + 1
    print('----------------------------------------------------------------')
    print('Genotipo: ' + str(it))
    print("Max: " + str(np.max((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2])))
    print("Min: " + str(np.min((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2])))
    print("Media: " + str(np.around(np.mean((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2]), 2)))
    print("Var: " + str(np.around(np.var((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2]), 2)))
    variaveis_novas[i, 0] = i + 1
    variaveis_novas[i, 1] = np.max((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2])
    variaveis_novas[i, 2] = np.min((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2])
    variaveis_novas[i, 3] = np.around(np.mean((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2]), 2)
    variaveis_novas[i, 4] = np.around(np.var((matriz_nova[matriz_nova[:, 0] == i + 1])[:, 2]), 2)

np.savetxt('Resultado_Novo.txt',  variaveis_novas  )
print(' ')
print('-' * 50)
print('Sumario')
print('-' * 50)
print('     Gen       Max      Min     Mean     Var')
print(variaveis_novas)
print('-----------------------------------------------------------------------------------------------------------------')


print(' f) Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.')
media_nova_500 = variaveis_novas[:, 3] >= 500
maior_500 = variaveis_novas[media_nova_500]
print("Os genótipos que apresentam média maior que 500 são: " + str(maior_500[:, 0]) )

print('-----------------------------------------------------------------------------------------------------------------')


print( 'g) Apresente os seguintes graficos:  - Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura - Disperão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.')
import matplotlib.pyplot as plt

media1 = np.zeros((10,1))               # criei um vetor de zeros com 10 linhas e 1 coluna
media2 = np.zeros((10,1))               # Um é genótipo e os outros 4 as variáveis
media3 = np.zeros((10,1))
media4 = np.zeros((10,1))
media5 = np.zeros((10,1))
contador = 0
for i in np.arange(0,30,3):             #percorre as 30 linhas do vetor original de acordo com o numero de repetições
    media1[contador,0] = np.mean(dados[i:i + 3, 2], axis=0)
    media2[contador,0] = np.mean(dados[i:i + 3, 3], axis=0)
    media3[contador,0] = np.mean(dados[i:i + 3, 4], axis=0)
    media4[contador,0] = np.mean(dados[i:i + 3, 5], axis=0)
    media5[contador,0] = np.mean(dados[i:i + 3, 6], axis=0)
    contador = contador + 1
genotipos = np.unique(dados[0:30,0:1], axis=0)
tabel_medias = np.concatenate((genotipos, media1, media2, media3, media4, media5), axis=1)
print('Gráficos - Médias dos genótipos para cada variável')
plt.style.use('ggplot')            #estilo de gráfico
fig = plt.figure('Gráfico de Médias')        # comando pro título
plt.subplot(2,3,1)        #colocar as 4 tabelas dentro de uma figura, duas linhas e três colunas, o primeiro gráfico vai na posição 1
plt.bar(tabel_medias[:,0], tabel_medias[:,1])    # genotipos e a primeira variável, cada um em um eixo do gráfico
plt.title('Var 1')     #título do gráfico
plt.xticks(tabel_medias[:,0])           #indicar o nome dos genótipos(1, 2,3......10)
plt.subplot(2,3,2)             #o dois vai indicar que está na posiçao dois da figura
plt.bar(tabel_medias[:,0], tabel_medias[:,2]) # mudar pra segunda característica
plt.title('Var 2')           #mudar o nome da variável no título
plt.xticks(tabel_medias[:,0])
plt.subplot(2,3,3)
plt.bar(tabel_medias[:,0], tabel_medias[:,3])
plt.title('Var 3')
plt.xticks(tabel_medias[:,0])
plt.subplot(2,3,4)
plt.bar(tabel_medias[:,0], tabel_medias[:,4])
plt.title('Var 4')
plt.xticks(tabel_medias[:,0])
plt.subplot(2,3,5)
plt.bar(tabel_medias[:,0], tabel_medias[:,5])
plt.title('Var 5')
plt.xticks(tabel_medias[:,0])
fig.tight_layout()          #Ajuste dos subquadrantes para fornecer preenchimento sem sobreposição
plt.show()                   #mostrar o gráfico
nome = 'medias_barras'           #salvar o gráfico no computador
fig.savefig((nome+'.png'),bbox_inches='tight')
print('---------------------------------------------------------------------------- ')
print('Gráficos - Dispersão')
plt.style.use('ggplot') #tipo de gráfico
fig = plt.figure('Dispersão') # Título da figura
plt.subplot(2,2,1)                      # 1, 2 - delimitam como seria a figura    1 - posição do gráfico
plt.scatter(tabel_medias[:,1], tabel_medias[:,2], s=50, alpha=1, c='pink')    #coordenada x- [:,1] coordenada y- [:,2] tamanho- s=50 transparencia- alpha=1
plt.title('Dispersão') #título do gráfico
plt.xlabel('Var 1') #título dos eixos x e y
plt.ylabel('Var 2')
plt.subplot(2,2,2)
plt.scatter(tabel_medias[:,1], tabel_medias[:,3], s=50, alpha=1, c='pink')
plt.title('Dispersão')
plt.xlabel('Var 1')
plt.ylabel('Var 3')
plt.subplot(2,2,3)
plt.scatter(tabel_medias[:,2], tabel_medias[:,3], s=50, alpha=1, c='pink')
plt.title('Dispersão')
plt.xlabel('Var 2')
plt.ylabel('Var 3')
fig.tight_layout()
plt.show()

print('-----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
########################################################################################################################
########################################################################################################################