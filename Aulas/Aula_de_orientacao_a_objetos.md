# Aula: Introdução à Programação Orientada a Objetos em Python

## O que é Programação Orientada a Objetos (POO)?

Programação Orientada a Objetos (POO) é um paradigma de programação baseado no conceito de "objetos", que podem conter dados na forma de campos (frequentemente conhecidos como atributos ou propriedades) e código na forma de procedimentos (métodos). POO é usada para estruturar programas de forma a agrupar dados e comportamentos relacionados.

---

## Conceitos Básicos da POO

### 1. Classes e Objetos

- **Classe**: Um modelo ou blueprint a partir do qual os objetos são criados. Define atributos e métodos.
- **Objeto**: Uma instância de uma classe.

### 2. Atributos e Métodos

- **Atributos**: Variáveis que pertencem a uma classe.
- **Métodos**: Funções que pertencem a uma classe.

### 3. Encapsulamento

- Agrupar os dados (atributos) e os métodos em uma unidade única, a classe, restringindo o acesso direto a alguns componentes.

### 4. Herança

- Uma classe pode herdar atributos e métodos de outra classe.

### 5. Polimorfismo

- A capacidade de utilizar uma interface para diferentes tipos de dados.

---

## Criando uma Classe em Python

Vamos criar uma classe simples chamada `Carro`.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}")
```

### Explicação:

- `__init__` é um método especial chamado de construtor. É chamado quando um objeto é criado a partir da classe.
- `self` refere-se à instância atual da classe.

## Criando um Objeto

```python
meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_detalhes()
```

---

## Encapsulamento

```python
class ContaBancaria:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def exibir_saldo(self):
        print(self.__saldo)
```

### Explicação:

- `__saldo` é um atributo privado, não acessível fora da classe.

---

## Herança

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}")

meu_carro = Carro("Honda", "Civic")
meu_carro.exibir_detalhes()
```

### Explicação:

- `Carro` herda de `Veiculo`.

---

## Polimorfismo

```python
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"

def som_do_animal(animal):
    print(animal.falar())

som_do_animal(Cachorro())
som_do_animal(Gato())
```

### Explicação:

- Métodos com o mesmo nome comportam-se de forma diferente com base no objeto.

---

Com esta introdução, você deve ter uma compreensão básica de como a Programação Orientada a Objetos funciona em Python, incluindo como criar e usar classes, objetos, e implementar conceitos fundamentais como encapsulamento, herança e polimorfismo.
