from germi_dtw import warping_path

#class Laberinto():

    #def __init__(self, dimension):
        #self.dimension = dimension

    #def crear_laberinto(self):
        #laberinto = array()
        #return laberinto

laberinto = [
    [0,1,1,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [1,0,0,0,0]
]

warping_path(laberinto)