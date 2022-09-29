'''Classe que representa um labiirinto'''

from traceback import print_last


class Labirinto:

    def __init__(self):
        self.labi = []
        arquivo = open('labirinto1.txt', 'r')
        self.tamanho_labirinto = int(arquivo.readline())
        # print('tamanho do labirinto: {}'.format(self.tamanho_labirinto))
        for linha in arquivo:
            pos = linha.split(' ')
            pos[self.tamanho_labirinto-1] = pos[self.tamanho_labirinto-1].strip()
            self.labi.append(pos)
        self.x = 0
        self.y = 0
        self.comidas = self.tamanho_labirinto // 2
        

    def get_comidas(self):
        return self.comidas

    def print_labirinto(self):
        for i in range(0,10):
            for casa in self.labi[i]:
                print('{}'.format(casa), end=' ')
            print('')
        print('--------------------------------------------------')

    def mover(self, movimento):
        ''' 0: up
            1: down
            2: right
            3: left
            4: up right
            5: up left
            6: down right
            7: down left '''
        if movimento == 0:
            if (self.y-1 >= 0) and (self.labi[self.y-1][self.x] != '1'):
                self.labi[self.y][self.x] = '0'
                self.y = self.y - 1
        elif movimento == 1:
            if (self.y+1 < 10) and (self.labi[self.y+1][self.x] != '1'):
                self.labi[self.y][self.x] = '0'
                self.y = self.y + 1
        elif movimento == 2:
            if (self.x+1 < 10) and (self.labi[self.y][self.x+1] != '1'):
                self.labi[self.y][self.x] = '0'
                self.x = self.x + 1
        elif movimento == 3:
            if (self.x-1 >= 0) and (self.labi[self.y][self.x-1] != '1'):
                self.labi[self.y][self.x] = '0'
                self.x = self.x - 1
        elif movimento == 4:
            if (self.y-1 >= 0) and (self.x+1 < 10) and (self.labi[self.y-1][self.x+1] != '1'):
                self.labi[self.y][self.x] = '0'
                self.y = self.y - 1
                self.x = self.x + 1
        elif movimento == 5:
            if (self.y-1 >= 0) and (self.x-1 >= 0) and (self.labi[self.y-1][self.x-1] != '1'):
                self.labi[self.y][self.x] = '0'
                self.y = self.y - 1
                self.x = self.x - 1
        elif movimento == 6:
            if (self.y+1 < 10) and (self.x+1 < 10) and (self.labi[self.y+1][self.x+1] != '1'):
                self.labi[self.y][self.x] = '0'
                self.y = self.y + 1
                self.x = self.x + 1
        elif movimento == 7:
            if (self.y+1 < 10) and (self.x-1 >= 0) and (self.labi[self.y+1][self.x-1] != '1'):
                self.labi[self.y][self.x] = '0'
                self.y = self.y + 1
                self.x = self.x - 1
        if(self.labi[self.y][self.x] == 'C'):
            self.comidas -= 1
        self.labi[self.y][self.x] = 'E'

    def pode_mover(self, movimento):
        ''' 0: up
            1: down
            2: right
            3: left
            4: up right
            5: up left
            6: down right
            7: down left '''
        if movimento == 0:
            if (self.y-1 >= 0) and (self.labi[self.y-1][self.x] != '1'):
                return True
            return False
        elif movimento == 1:
            if (self.y+1 < 10) and (self.labi[self.y+1][self.x] != '1'):
                return True
            return False
        elif movimento == 2:
            if (self.x+1 < 10) and (self.labi[self.y][self.x+1] != '1'):
                return True
            return False
        elif movimento == 3:
            if (self.x-1 >= 0) and (self.labi[self.y][self.x-1] != '1'):
                return True
            return False
        elif movimento == 4:
            if (self.y-1 >= 0) and (self.x+1 < 10) and (self.labi[self.y-1][self.x+1] != '1'):
                return True
            return False
        elif movimento == 5:
            if (self.y-1 >= 0) and (self.x-1 >= 0) and (self.labi[self.y-1][self.x-1] != '1'):
                return True
            return False
        elif movimento == 6:
            if (self.y+1 < 10) and (self.x+1 < 10) and (self.labi[self.y+1][self.x+1] != '1'):
                return True
            return False
        elif movimento == 7:
            if (self.y+1 < 10) and (self.x-1 >= 0) and (self.labi[self.y+1][self.x-1] != '1'):
                return True
            return False

    def tem_comida(self):
        if self.labi[self.y][self.x] == 'C':
            return True
        return False