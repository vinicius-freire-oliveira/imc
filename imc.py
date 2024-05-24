# Definindo a classe IMC
class IMC:
    # Método de inicialização da classe, recebe peso em kg e altura em metros como parâmetros
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
    # Exibir apresentação
    print("\n==================== Cálculo de IMC ====================")
    # Método para calcular o Índice de Massa Corporal (IMC)
    def calcula_imc(self):
        imc = self.peso / (self.altura ** 2)
        print("Seu IMC é: {:.2f}".format(imc))
        return imc

    # Método para classificar o IMC de acordo com os valores padrão da OMS
    def classifica_imc(self, imc):
        if imc < 18.5:
            print("Classificação - Baixo peso")
        elif 18.5 <= imc < 25:
            print("Classificação - Peso ideal")
        elif 25 <= imc < 30:
            print("Classificação - Sobrepeso")
        else:
            print("Classificação - Obesidade")

    # Método para calcular os pesos ideais mínimo e máximo de acordo com os valores padrão da OMS
    def calcular_pesos_ideais(self):
        peso_ideal_min = 18.5 * (self.altura ** 2)
        peso_ideal_max = 24.99 * (self.altura ** 2)
        return peso_ideal_min, peso_ideal_max

# Exemplo de uso da classe:
# Criando um objeto da classe IMC com os valores de peso e altura informados
calculadora = IMC(70, 1.75)

# Chamando o método calcula_imc para calcular e imprimir o IMC
imc = calculadora.calcula_imc()

# Chamando o método classifica_imc para classificar o IMC obtido
calculadora.classifica_imc(imc)

# Chamando o método calcular_pesos_ideais para calcular os pesos ideais mínimo e máximo
pesoIdeal1, pesoIdeal2 = calculadora.calcular_pesos_ideais()

# Imprimindo os pesos ideais mínimo e máximo
print("Seu peso ideal deverá estar entre: {:.2f} Kg e {:.2f} Kg".format(pesoIdeal1, pesoIdeal2))
