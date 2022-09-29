from zipfile import LargeZipFile
from labirinto import Labirinto
from random import randrange
import random

def main():

    populacao_inical = []
    num_geracao = 1

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
    geracao = populacao_inical
    geracao_aux = []
    num_geracao = 0

    while num_geracao < 200:

        elitismo_cromo = geracao[0]
        n = 0
        while n < len(geracao):
            aptidao = geracao[n][len(geracao[i])-1]
            if aptidao == 0:
                print('Solução encontrada: {}'.format(geracao[i])-1)
                exit(1)
            if aptidao < melhor_aptidao:
                elitismo_cromo = geracao[n]
                melhor_aptidao = aptidao
            n += 1


        geracao_aux.append(elitismo_cromo)
        for i in range(len(geracao)//2):
            (pai, mae) = torneio(geracao)
            corte = randrange(len(pai))
            filho1, filho2 = crossover(pai[:-1], mae[:-1], corte)
            aptidao1 = calcula_aptidao(filho1)
            aptidao2 = calcula_aptidao(filho2)
            filho1.append(aptidao1)
            filho2.append(aptidao2)
            geracao_aux.append(filho1)
            geracao_aux.append(filho2)

        ocorre_mutacao = randrange(5)
        if(ocorre_mutacao == 0):
            mutacao(geracao)

        index = 0
        for individuo in geracao_aux:
            print('Cromossomo {}: {}'.format(index,individuo))
            index += 1
        print('GERAÇÃO: {}'.format(num_geracao))
        
        geracao = geracao_aux
        geracao_aux = []
        num_geracao += 1
        


def crossover(a, b, index):
    return b[:index] + a[index:], a[:index] + b[index:]

def mutacao(populacao):
    random_ind = randrange(len(populacao))
    random_index = randrange(len(populacao[random_ind]) - 1)
    random_gene = randrange(7)
    populacao[random_ind][random_index] = random_gene

def torneio(populacao):
    # for individuo in populacao:
    #     print(individuo)
    indices = random.sample(range(len(populacao)), 4)
    # print(indices)
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
