
from optparse import OptionParser
from labirinto import Labirinto
from random import randrange
import random

def main():
    
    parser = OptionParser(usage='Usage: %prog <-r> <False or True>')
    parser.add_option('-r', '--exec-rapida', dest='rapido',
                      default=False, help="Execução rápida")
    (cfg, _) = parser.parse_args()

    populacao_inical = []
    num_geracao = 1
    TAMANHO_CROMOSSOMO = 100
    NUMERO_GERACOES = 200
    CHANCE_MUTACAO = 5      #[0 ou 1 ou 2 ou 3 ou 4]20% de chance 

    res_log = open('log.txt', 'w')

    for n in range(5):
        i = 0
        cromossomo = Labirinto()
        cromossomo_mov = []
        while i < TAMANHO_CROMOSSOMO:
            random = randrange(7)
            if cromossomo.pode_mover(random):
                cromossomo.mover(random)
                cromossomo_mov.append(random)
                i+=1
        # IMPORTANTE A ultima posicao do individuo e a sua aptidao
        aptidao = calcula_aptidao(cromossomo_mov)
        cromossomo_mov.append(aptidao)
        populacao_inical.append(cromossomo_mov)

    melhor_aptidao = 100000
    geracao = populacao_inical

    while num_geracao <= NUMERO_GERACOES:

        for cromossomo in geracao:
            if cromossomo[len(cromossomo)-1] == 0:
                print('Solução encontrada:')
                resposta = Labirinto()
                for mov in cromossomo:
                    resposta.mover(mov)
                    resposta.print_labirinto()
                exit(1)

        geracao_aux = []

        elitismo_cromo = geracao[0]
        for n in range(1, len(geracao)):
            # print('n: {}'.format(n))
            aptidao = geracao[n][len(geracao[n])-1]
            if aptidao < melhor_aptidao:
                elitismo_cromo = geracao[n]
                melhor_aptidao = aptidao
            n += 1


        geracao_aux.append(elitismo_cromo)
        # for i in range(len(geracao)//2):

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

        ocorre_mutacao = randrange(CHANCE_MUTACAO)
        if(ocorre_mutacao == 0):
            mutacao(geracao_aux)

        index = 0
        if not cfg.rapido:
            for individuo in geracao_aux:
                res_log.write('Cromossomo {}: {}\n'.format(index,individuo))
                index += 1
            res_log.write('GERAÇÃO: {}\n'.format(num_geracao))
        
        geracao = geracao_aux
        num_geracao += 1

    resposta = Labirinto()
    for mov in geracao[0]:
        resposta.mover(mov)
        resposta.print_labirinto()   


def crossover(a, b, index):
    filho1 = b[:index] + a[index:]
    filho2 = a[:index] + b[index:]
    labirinto = Labirinto()
    for i in range(index):
        labirinto.mover(filho1[i])
    for j in range(index, len(filho1)):
        if labirinto.pode_mover(filho1[j]):
            labirinto.mover(filho1[j])
        else:
            while not labirinto.pode_mover(filho1[j]):
                filho1[j] = randrange(7)
            labirinto.mover(filho1[j])

    labirinto = Labirinto()
    for i in range(index):
        labirinto.mover(filho2[i])
    for j in range(index, len(filho2)):
        if labirinto.pode_mover(filho2[j]):
            labirinto.mover(filho2[j])
        else:
            while not labirinto.pode_mover(filho2[j]):
                filho2[j] = randrange(7)
            labirinto.mover(filho2[j])
    return filho1, filho2

def mutacao(populacao):
    random_ind = randrange(len(populacao))
    random_index = randrange(len(populacao[random_ind]) - 1)
    random_gene = randrange(7)
    print('O cromossomo {} na posicao {} foi alteirado para {}'.format(random_ind, random_index, random_gene))
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
