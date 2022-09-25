'''Classe que representa um labiirinto'''

class labiirinto:
    def __init__(self):
        self.labi = []
        arquivo = open('labiirinto.txt', 'r')
        i = 1
        for linha in arquivo:
            pos = linha.split(',')
            pos.pop()
            self.labi.append(pos)
            i += 1
        self.x = 0
        self.y = 0

    def print_labiirinto(self):
        for i in range(0,10):
            print(self.labi[i])
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
        self.labi[self.y][self.x] = ' '
        if movimento == 0:
            self.y = self.y - 1
        elif movimento == 1:
            self.y = self.y + 1
        elif movimento == 2:
            self.x = self.x + 1
        elif movimento == 3:
            self.x = self.x - 1
        elif movimento == 4:
            self.y = self.y + 1
            self.x = self.x + 1
        elif movimento == 5:
            self.y = self.y - 1
            self.x = self.x - 1
        elif movimento == 6:
            self.y = self.y + 1
            self.x = self.x + 1
        elif movimento == 7:
            self.y = self.y + 1
            self.x = self.x - 1
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

labi = labiirinto()
labi.print_labiirinto()
print(labi.pode_mover(0))