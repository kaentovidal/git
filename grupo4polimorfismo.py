class cliente():

    def __init__(self,nombre, idt, celular):
        self._nombre=nombre
        self._idt=idt
        self._celular=celular

    def getNombre(self):
        return(self._nombre)

    def getIdt(self):
        return (self._idt)

    def getCell(self):
        return (self._celular)


class paquete(cliente):

    def __init__(self, nombre, idt, celular, descuento):
        super().__init__(nombre, idt, celular)
        self.descuento=descuento

            
class vip(paquete):
    
    def __init__(self, nombre, idt, celular, descuento):
        super().__init__(nombre, idt, celular, descuento)

    
    def type(self):
        print("Cliente VIP")
    
    def mostrar(self):
        print("Descuento del 4%")

class corriente(paquete):
    
    def __init__(self, nombre, idt, celular, descuento):
        super().__init__(nombre, idt, celular, descuento)
    
    def type(self):
        print("Cliente CORRIENTE")

    def mostrar(self):
        print("Descuento del 2%")

class especial(paquete):
    
    def __init__(self, nombre, idt, celular, descuento):
        super().__init__(nombre, idt, celular, descuento)
    
    def type(self):
        print("Cliente ESPECIAL")

    def mostrar(self):
        print("Descuento del 3%")

def tipo(client):
    client.mostrar()

def tipe(clint):
    clint.type()
