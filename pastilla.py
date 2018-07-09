class Pastilla:
    rowid = 0
    
    def __init__(self, name, mount, time):
        self.nombre = name
        self.cantidad = mount
        self.momento = time

    def toString(self):
        print("DATA: ", self.nombre, self.cantidad, self.momento)
