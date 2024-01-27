class Computador:
    def __init__(self, marca, tipo, ram, cpu, gpu):
        self.marca = marca
        self.tipo = tipo
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu

    pass


computador1 = Computador(
    "Dell", "Notebook", "8gb ddr4 3200mhz", "intel core i5 1135g7", "intel iris xe"
)
computador2 = Computador(
    "Custom", "Desktop", "32gb ddr4 3200mhz", "Amd ryzen 7", "Geforce Rtx 3060ti"
)


print(
    computador1.marca,
    computador1.tipo,
    computador1.ram,
    computador1.cpu,
    computador1.gpu,
    computador2.marca,
    computador2.tipo,
    computador2.ram,
    computador2.cpu,
    computador2.gpu,
)
