class Computador:
    def __init__(self):
        self.marca = "Dell"
        self.tipo = "notebook"
        self.ram = "8gb ddr4 3200mhz"
        self.cpu = "intel core i5"
        self.gpu = "intel iris Xe"

    pass


computador1 = Computador()

print(
    computador1.marca,
    computador1.tipo,
    computador1.ram,
    computador1.cpu,
    computador1.gpu,
)
