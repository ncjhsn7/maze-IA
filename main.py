from zipfile import LargeZipFile
from labirinto import Labirinto
from random import randrange
import random

def main():

    populacao_inical = []

    i = 0
    for n in range(5):
        cromossomo = Labirinto()
        cromossomo_mov = []
        while i < 100:
            random = randrange(7)
            cromossomo.mover(random)
            cromossomo_mov.append(random)
            i+=1
        i = 0
        # IMPORTANTE A ultima posicao do individuo e a sua aptidao
        aptidao = calcula_aptidao(cromossomo_mov)
        cromossomo_mov.append(aptidao)
        populacao_inical.append(cromossomo_mov)

    melhor_aptidao = 100
    elitismo_cromo = []
    for n in range(len(populacao_inical)):
        aptidao = populacao_inical[i][len(populacao_inical[i])-1]
        if aptidao == 0:
            print('Solução encontrada: {}'.format(populacao_inical[i])-1)
            exit(1)
        if aptidao < melhor_aptidao:
            elitismo_cromo = populacao_inical[i]
            melhor_aptidao = aptidao

    populacao_intermediaria = []
    populacao_intermediaria.append(elitismo_cromo)
    for i in range(len(populacao_inical)//2):
        (pai, mae) = torneio(populacao_inical)
        corte = randrange(len(pai))
        filho1, filho2 = crossover(pai[:-1], mae[:-1], corte)
        aptidao1 = calcula_aptidao(filho1)
        aptidao2 = calcula_aptidao(filho2)
        filho1.append(aptidao1)
        filho2.append(aptidao2)
        populacao_intermediaria.append(filho1)
        populacao_intermediaria.append(filho2)

    mutacao(populacao_intermediaria)

    for individuo in populacao_intermediaria:
        print(individuo)


def crossover(a, b, index):
    return b[:index] + a[index:], a[:index] + b[index:]

def mutacao(populacao):
    random_ind = randrange(len(populacao))
    random_index = randrange(len(populacao[random_ind]) - 1)
    random_gene = randrange(7)
    populacao[random_ind][random_index] = random_gene

def torneio(populacao):
    indices = random.sample(range(len(populacao)), 4)
    pai = []
    aptidao1 = populacao[indices[0]][len(populacao[indices[0]]) - 1]
    aptidao2 = populacao[indices[1]][len(populacao[indices[1]]) - 1]
    if aptidao1 < aptidao2:
        pai = populacao[indices[0]]
    else:
        pai = populacao[indices[1]]
    mae = []
    aptidao1 = populacao[indices[2]][len(populacao[indices[2]]) - 1]
    aptidao2 = populacao[indices[3]][len(populacao[indices[3]]) - 1]
    if aptidao1 < aptidao2:
        mae = populacao[indices[2]]
    else:
        mae = populacao[indices[3]]
    return (pai, mae)


def calcula_aptidao(seq_movimentos):
    labi = Labirinto()
    for movimento in seq_movimentos:
        labi.mover(movimento)
    return labi.get_comidas()


if __name__ == '__main__':
    main()
