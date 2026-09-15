class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Blanco"
        self.gasolina = 0
    @classmethod
    def crear_auto(cls, marca, modelo, color, gasolina):
        auto = cls(marca, modelo)
        auto.color = color
        auto.gasolina = gasolina
        return auto
    
    def __pos__(self):
        self.gasolina += 5
        return self
    def __add__(self, nuevo_color):
        self.color = nuevo_color
        return self
    def __sub__(self,otro):
        return self.gasolina + otro.gasolina
    def mostrar(self):
        print("Marca: ", self.marca)     
        print("Modelo: ", self.modelo)
        print("Color: ", self.color)
        print("Gasolina: ", self.gasolina, "litros")

auto1 = Auto("Toyota","Corolla")
auto2 = Auto.crear_auto("Ford", "Mustang", "Rojo", 20)

#b)
print("AUTO 1") 
auto1.mostrar()
print("______________________________________")
print("AUTO 2")
auto2.mostrar()

#c)
print("______________________________________")
print("c) Auto con el ++: ")
auto1.__pos__()
auto1.mostrar()

#d)
print("______________________________________")
print("d) AUTO 2 despues de cambiar el color: ")
auto2.__add__("azul")
auto2.mostrar()

#e)
print("______________________________________")
total = auto1.__sub__(auto2)
print("e) Gasolina: ", total, "litros")

