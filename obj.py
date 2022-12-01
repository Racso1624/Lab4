#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Lab 4

class Obj(object):

    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.tvertices = []
        self.nvertices = []
        self.faces = []
        self.read()

    def read(self):
        for line in self.lines:
            if not line or line.startswith('#'):
                pass
            else:
                prefix, value = line.split(' ', 1)
            
                if prefix == 'v':
                    self.vertices.append(
                        list(map(float, value.strip().split(' ')))
                    )
                elif prefix == 'vt':
                    self.tvertices.append(
                        list(map(float, value.strip().split(' ')))
                    )
                elif prefix == 'vn':
                    self.nvertices.append(
                        list(map(float, value.strip().split(' ')))
                    )
                elif prefix == 'f':
                    self.faces.append(
                        [list(map(int, face.strip().split('/'))) for face in value.strip().split(' ')]
                    )